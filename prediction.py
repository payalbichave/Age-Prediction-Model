import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import random


def apply_custom_css():
    st.markdown("""
    <style>

    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    .page-title {
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .page-subtitle {
        color: gray;
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


# Dummy model
AGE_GROUPS = {
    0: "18–29",
    1: "30–44",
    2: "45–59",
    3: "60–74",
    4: "75+",
}


def predict_age_group(gndr, eduyrs, hincfel, w4gq1, w4gq2):

    score = eduyrs + w4gq1 + w4gq2 + hincfel

    idx = int(np.clip(score // 10, 0, 4))

    confidence = random.randint(75, 95)

    return idx, confidence


# ✅ IMPORTANT
def show():

    apply_custom_css()

    st.markdown(
        '<div class="page-title">Age Group Prediction</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="page-subtitle">Enter values and predict age group</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        gndr = st.selectbox("Gender", ["Male", "Female"])

        eduyrs = st.slider(
            "Education Years",
            0,
            25,
            12,
        )

        hincfel = st.slider(
            "Income Feeling",
            1,
            4,
            2,
        )

        w4gq1 = st.slider(
            "Question 1",
            1,
            5,
            3,
        )

        w4gq2 = st.slider(
            "Question 2",
            1,
            5,
            3,
        )

        predict_clicked = st.button("Predict")

    with col2:

        if predict_clicked:

            idx, confidence = predict_age_group(
                gndr,
                eduyrs,
                hincfel,
                w4gq1,
                w4gq2,
            )

            st.success(
                f"Predicted Age Group: {AGE_GROUPS[idx]}"
            )

            st.write(
                f"Confidence: {confidence}%"
            )

        else:

            st.info(
                "Enter values and click Predict"
            )

    st.divider()

    st.subheader("Feature Importance")

    importance = {
        "eduyrs": 0.38,
        "hincfel": 0.27,
        "w4gq1": 0.18,
        "w4gq2": 0.12,
        "gndr": 0.05,
    }

    fig = go.Figure(
        go.Bar(
            x=list(importance.keys()),
            y=list(importance.values()),
        )
    )

    st.plotly_chart(fig, use_container_width=True)