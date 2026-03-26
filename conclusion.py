import streamlit as st
import plotly.graph_objects as go
import pandas as pd


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


# ✅ IMPORTANT
def show():

    apply_custom_css()

    st.markdown(
        '<div class="page-title">Conclusion</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Summary of the project</div>',
        unsafe_allow_html=True
    )

    st.divider()

    # metrics
    col1, col2, col3, col4, col5 = st.columns(5)

    metrics = [
        ("5", "Models"),
        ("0.89", "Best Accuracy"),
        ("5", "Features"),
        ("SMOTE", "Balancing"),
        ("GB", "Final Model"),
    ]

    for col, (v, l) in zip(
        [col1, col2, col3, col4, col5],
        metrics
    ):
        col.metric(l, v)

    st.divider()

    st.subheader("Key Achievements")

    st.write("""
    - Performed data analysis
    - Handled class imbalance using SMOTE
    - Tested multiple ML models
    - Selected Gradient Boosting
    - Built interactive dashboard
    - Implemented live prediction
    """)

    st.divider()

    st.subheader("Workflow")

    steps = [
        "Data collection",
        "Data cleaning",
        "EDA",
        "SMOTE balancing",
        "Model training",
        "Model comparison",
        "Final model selection",
        "Dashboard creation",
    ]

    for s in steps:
        st.write("•", s)

    st.divider()

    st.subheader("Accuracy Comparison")

    models = [
        "KNN",
        "SVM",
        "RF",
        "ExtraTrees",
        "GradientBoosting",
    ]

    acc = [
        0.76,
        0.82,
        0.85,
        0.86,
        0.89,
    ]

    fig = go.Figure(
        go.Bar(
            x=models,
            y=acc,
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Project completed successfully"
    )