import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

from imblearn.over_sampling import SMOTE


# ===== LOAD DATA =====
df = pd.read_csv("data.csv")   # change if name different

print(df.head())


# ===== SELECT FEATURES =====

X = df[["gndr", "eduyrs", "hincfel", "w4gq1", "w4gq2"]]
y = df["agegroup35"]


# ===== SPLIT =====

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ===== SCALE =====

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ===== SMOTE =====

smote = SMOTE(random_state=42)

X_res, y_res = smote.fit_resample(X_train_scaled, y_train)


# ===== MODEL =====

model = GradientBoostingClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=3
)

model.fit(X_res, y_res)


# ===== TEST =====

y_pred = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# ===== SAVE MODEL =====

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model saved")