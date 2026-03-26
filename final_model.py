import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


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

    .metric-card {
        background-color: #111827;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }

    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #00D4FF;
    }

    .metric-label {
        font-size: 12px;
        color: gray;
    }

    </style>
    """, unsafe_allow_html=True)


# ✅ IMPORTANT — must be show()
def show():

    apply_custom_css()

    st.markdown('<div class="page-title">Final Model Selection</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Gradient Boosting selected as final model</div>', unsafe_allow_html=True)

    # metrics
    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("Gradient Boosting", "Final Model"),
        ("0.76", "Accuracy"),
        ("0.27", "Precision"),
        ("0.22", "Recall"),
    ]

    for col, (val, lbl) in zip([c1, c2, c3, c4], cards):
        col.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{val}</div>
            <div class="metric-label">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Why Gradient Boosting?")

    st.write("""
    - Works well after SMOTE balancing  
    - Handles mixed survey data  
    - Best performance among tested models  
    - Balanced accuracy / precision / recall
    """)

    st.divider()

    st.subheader("Model Comparison")

    categories = ['Accuracy', 'Precision', 'Recall', 'F1']

    gb = [0.76, 0.27, 0.22, 0.30]
    rf = [0.71, 0.16, 0.22, 0.18]
    svm = [0.84, 0.0, 0.0, 0.0]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=gb + [gb[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='Gradient Boosting'
    ))

    fig.add_trace(go.Scatterpolar(
        r=rf + [rf[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='Random Forest'
    ))

    fig.add_trace(go.Scatterpolar(
        r=svm + [svm[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='SVM'
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("SMOTE Effect")

    data = pd.DataFrame({
        "Metric": ["Accuracy", "Precision", "Recall"],
        "Before": [0.83, 0.81, 0.78],
        "After": [0.89, 0.87, 0.86]
    })

    st.dataframe(data, use_container_width=True)

    st.success("Final model ready for prediction")