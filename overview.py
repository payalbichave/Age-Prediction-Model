import streamlit as st


def show():

    st.title("Overview")

    st.write("""
    Project: Age Group Prediction using Survey Data

    Goal:
    Predict whether a person belongs to age group under 35 or 35+

    Features:
    gndr
    eduyrs
    hincfel
    w4gq1
    w4gq2

    Final Model:
    Gradient Boosting
    """)