import streamlit as st
import plotly.graph_objects as go
import pandas as pd


# ---------- CSS ----------
def apply_css():
    st.markdown(
        """
        <style>

        .title {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 0px;
        }

        .subtitle {
            color: #9aa0a6;
            margin-bottom: 10px;
        }

        .card {
            background-color: #0f172a;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }

        .card-value {
            font-size: 26px;
            font-weight: bold;
            color: #22d3ee;
        }

        .card-label {
            color: #94a3b8;
            font-size: 13px;
        }

        .reason-box {
            background-color: #0f172a;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-size: 14px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------- PAGE ----------
def show():

    apply_css()

    # ---------- TITLE ----------
    st.markdown('<div class="title">Final Model Selection</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Gradient Boosting selected as final model</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    # ---------- METRICS ----------
    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("Gradient Boosting", "Model"),
        ("0.76", "Accuracy"),
        ("0.27", "Precision"),
        ("0.22", "Recall"),
    ]

    for col, (v, l) in zip([c1, c2, c3, c4], cards):
        col.markdown(
            f"""
            <div class="card">
                <div class="card-value">{v}</div>
                <div class="card-label">{l}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # ---------- TWO COLUMN ----------
    left, right = st.columns([1, 1])

    # ---------- LEFT ----------
    with left:

        st.subheader("Why Gradient Boosting?")

        reasons = [
            "Works well after SMOTE balancing",
            "Handles survey data efficiently",
            "Best overall performance",
            "Balanced accuracy, precision & recall",
            "Stable predictions compared to others",
            "Performs well on imbalanced classification problems"
        ]

        for r in reasons:
            st.markdown(
                f"""
                <div class="reason-box">
                {r}
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ---------- RIGHT ----------
    with right:

        st.subheader("Model Comparison")

        models = ["Gradient Boosting", "Random Forest", "SVM"]

        accuracy = [0.76, 0.71, 0.84]
        precision = [0.27, 0.16, 0.00]
        recall = [0.22, 0.22, 0.00]
        f1 = [0.30, 0.18, 0.00]

        fig = go.Figure()

        fig.add_trace(
            go.Bar(name="Accuracy", x=models, y=accuracy)
        )

        fig.add_trace(
            go.Bar(name="Precision", x=models, y=precision)
        )

        fig.add_trace(
            go.Bar(name="Recall", x=models, y=recall)
        )

        fig.add_trace(
            go.Bar(name="F1", x=models, y=f1)
        )

        fig.update_layout(
            barmode="group",
            height=350,
            margin=dict(l=10, r=10, t=10, b=10),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="bar_chart_final_model",
        )

    st.divider()

    # ---------- SMOTE ----------
    st.subheader("SMOTE Effect")

    data = pd.DataFrame(
        {
            "Metric": ["Accuracy", "Precision", "Recall"],
            "Before": [0.83, 0.00, 0.00],
            "After": [0.73, 0.26, 0.26],
        }
    )

    st.dataframe(data, use_container_width=True)

    st.success("Final model ready for prediction")