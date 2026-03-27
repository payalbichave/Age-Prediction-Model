import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score, classification_report

from imblearn.over_sampling import SMOTE


# -----------------------
# LOAD DATA
# -----------------------

df = pd.read_csv("data.csv")

features = [
    "gndr",
    "eduyrs",
    "hincfel",
    "w4gq1",
    "w4gq2",
]

target = "agegroup35"

df = df[features + [target]].dropna()


X = df[features]
y = df[target]


# -----------------------
# SPLIT
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# -----------------------
# SCALE
# -----------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ===============================
# BEFORE SMOTE
# ===============================

print("\n=== BEFORE SMOTE ===")

model = GradientBoostingClassifier()

model.fit(X_train_scaled, y_train)

pred = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))


# ===============================
# AFTER SMOTE
# ===============================

print("\n=== AFTER SMOTE ===")

smote = SMOTE()

X_res, y_res = smote.fit_resample(
    X_train_scaled,
    y_train,
)

model2 = GradientBoostingClassifier()

model2.fit(X_res, y_res)

pred2 = model2.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, pred2))
print(classification_report(y_test, pred2))