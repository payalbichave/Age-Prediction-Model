import streamlit as st
import plotly.graph_objects as go
import pandas as pd


# ---------- CSS ----------
def apply_custom_css():
    st.markdown("""
    <style>

    html, body, [class*="css"] {
        font-size: 15px;
    }

    .page-title {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .page-subtitle {
        color: #9aa0a6;
        margin-bottom: 10px;
        font-size: 15px;
    }

    /* metric box */
    .metric-box {
        background: #0f172a;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 15px;
    }

    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #22d3ee;
    }

    .metric-label {
        font-size: 15px;
        color: #94a3b8;
    }

    /* achievement box */
    .ach-box {
        background: #0f172a;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 15px;
    }

    /* step box */
    .step-box {
        background: #0f172a;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 10px;
        font-size: 15px;
    }

    .step-title {
        color: #22d3ee;
        font-size: 15px;
        font-weight: 600;
    }

    /* interpretation box */
    .interpret-box {
        background: #0f172a;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        line-height: 1.6;
    }

    </style>
    """, unsafe_allow_html=True)


# ---------- PAGE ----------
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

    # ---------- METRICS ----------
    col1, col2, col3, col4, col5 = st.columns(5)

    metrics = [
        ("5", "Models"),
        ("0.74", "Best Accuracy"),
        ("5", "Features"),
        ("SMOTE", "Balancing"),
        ("GB", "Final Model"),
    ]

    for col, (v, l) in zip(
        [col1, col2, col3, col4, col5],
        metrics
    ):
        col.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{v}</div>
                <div class="metric-label">{l}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # ---------- ACHIEVEMENTS ----------
    st.subheader("Key Achievements")

    achievements = [
        "Performed data analysis",
        "Handled class imbalance using SMOTE",
        "Tested multiple ML models",
        "Selected Gradient Boosting",
        "Built interactive dashboard",
        "Implemented live prediction",
    ]

    cols = st.columns(3)

    for i, text in enumerate(achievements):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="ach-box">
                    {text}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # ---------- WORKFLOW ----------
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

    cols = st.columns(4)

    for i, step in enumerate(steps):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="step-box">
                    <div class="step-title">
                        Step {i+1}<br>{step}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # ---------- INTERPRETATION ----------
    st.subheader("Project Interpretation")

    st.markdown(
        """
        <div class="interpret-box">

        The analysis shows that demographic and opinion-based features can be used to classify individuals into age groups with good accuracy.
        <br><br>
        The results indicate that factors such as education level, income perception, and personal opinions have a measurable relationship with age group.
        <br><br>
        This demonstrates that machine learning can identify hidden patterns in survey data and use them to predict demographic characteristics even when the actual age is not provided.

        </div>
        """,
        unsafe_allow_html=True,
    )