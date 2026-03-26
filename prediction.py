import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


def show():

    st.title("Prediction Page")

    gndr = st.number_input("Gender", 0, 2, 1)
    eduyrs = st.number_input("Education years", 0, 30, 10)
    hincfel = st.number_input("Income feeling", 0, 10, 5)
    w4gq1 = st.number_input("Opinion 1", 0, 10, 5)
    w4gq2 = st.number_input("Opinion 2", 0, 10, 5)

    if st.button("Predict"):

        data = pd.DataFrame(
            [[gndr, eduyrs, hincfel, w4gq1, w4gq2]],
            columns=["gndr", "eduyrs", "hincfel", "w4gq1", "w4gq2"]
        )

        data = scaler.transform(data)

        pred = model.predict(data)

        if pred[0] == 1:
            st.success("Under 35")
        else:
            st.success("35 and above")