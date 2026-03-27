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

        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------- PAGE ----------
def show():

    apply_css()

    # ---------- TITLE ----------
    st.markdown(
        '<div class="title">Model Results</div>',
        unsafe_allow_html=True,
    )

    
    st.write(
        """
        Different machine learning models were trained and compared to find the best algorithm for predicting age group.
        All models were evaluated using the same dataset after preprocessing and SMOTE balancing.
        Accuracy was used as the main metric for  comparison.
        Gradient Boosting showed the best overall performance, so it was selected as the final model.
        """
    )
    st.divider()

    # ---------- METRIC CARDS ----------
    c1, c2, c3, c4, c5 = st.columns(5)

    cards = [
        ("KNN", "0.72"),
        ("SVM", "0.51"),
        ("RF", "0.62"),
        ("ExtraTrees", "0.69"),
        ("GB", "0.74"),
    ]

    for col, (name, val) in zip(
        [c1, c2, c3, c4, c5],
        cards,
    ):
        col.markdown(
            f"""
            <div class="card">
                <div class="card-value">{val}</div>
                <div class="card-label">{name}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # ---------- ACCURACY GRAPH ----------

    st.subheader("Accuracy Comparison")

    models = [
        "KNN",
        "SVM",
        "RF",
        "ExtraTrees",
        "GradientBoosting",
    ]

    accuracy = [
        0.72,
        0.51,
        0.62,
        0.69,
        0.74,
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=models,
            y=accuracy,
        )
    )

    fig.update_layout(
        height=450,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="accuracy_chart",
    )

    st.divider()

    # ---------- TABLE ----------
    st.subheader("Detailed Results")

    data = pd.DataFrame(
        {
            "Model": models,
            "Accuracy": accuracy,
        }
    )

    st.dataframe(
        data,
        use_container_width=True,
    )