import streamlit as st
import plotly.graph_objects as go
import pandas as pd


# ---------- CSS ----------
def apply_custom_css():
    st.markdown("""
    <style>

    .page-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .page-subtitle {
        color: #9aa0a6;
        margin-bottom: 10px;
    }

    /* metric box */
    .metric-box {
        background: #0f172a;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }

    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #22d3ee;
    }

    .metric-label {
        font-size: 13px;
        color: #94a3b8;
    }

    /* achievement box */
    .ach-box {
        background: #0f172a;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 14px;
    }

    /* step box */
    .step-box {
        background: #0f172a;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 10px;
    }

    .step-title {
        color: #22d3ee;
        font-size: 13px;
        font-weight: 600;
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

    # ---------- ACCURACY ----------
    st.subheader("Accuracy Comparison")

    models = [
        "KNN",
        "SVM",
        "RF",
        "ExtraTrees",
        "GradientBoosting",
    ]

    acc = [
        0.72,
        0.51,
        0.62,
        0.69,
        0.74,
    ]

    fig = go.Figure(
        go.Bar(
            x=models,
            y=acc,
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="acc_chart"
    )

    st.success("Project completed successfully")