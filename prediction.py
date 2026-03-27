import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.graph_objects as go


# ---------- LOAD MODEL ----------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


# ---------- LABELS ----------
AGE_GROUPS = {
    1: "Under 35",
    2: "35 and above",
}


# ---------- CSS ----------
def apply_css():
    st.markdown("""
    <style>

    .title {
        font-size: 30px;
        font-weight: 700;
    }

    .subtitle {
        color: gray;
        margin-bottom: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


# ---------- PAGE ----------
def show():

    apply_css()

    st.markdown('<div class="title">Age Group Prediction</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Enter user values to predict age group</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    col1, col2 = st.columns(2)

    # ---------- INPUT ----------
    with col1:

        gndr = st.selectbox("Gender", [1, 2])

        eduyrs = st.number_input(
            "Education Years",
            0,
            25,
            12,
        )

        hincfel = st.number_input(
            "Income Feeling (1–4)",
            1,
            4,
            2,
        )

        w4gq1 = st.number_input(
            "Agreement Level (1–5)",
            1,
            5,
            3,
        )

        w4gq2 = st.number_input(
            "Satisfaction Level (1–5)",
            1,
            5,
            3,
        )

        predict_clicked = st.button("Predict")

    # ---------- RESULT ----------
    with col2:

        if predict_clicked:

            input_data = np.array(
                [[gndr, eduyrs, hincfel, w4gq1, w4gq2]]
            )

            input_scaled = scaler.transform(input_data)

            pred = model.predict(input_scaled)[0]

            st.success(
                f"Predicted Age Group: {AGE_GROUPS[pred]}"
            )

        else:

            st.info("Enter values and click Predict")

    st.divider()

    # ---------- FEATURE IMPORTANCE ----------
    st.subheader("Feature Importance")

     

    feature_names = [
        "gndr",
        "eduyrs",
        "hincfel",
        "w4gq1",
        "w4gq2",
    ]

    importance = model.feature_importances_

    fig = go.Figure(
        go.Bar(
            x=feature_names,
            y=importance,
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="real_feature_chart",
    )

    