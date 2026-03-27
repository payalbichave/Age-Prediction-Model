import streamlit as st
import plotly.graph_objects as go
import pandas as pd


# ===== SHARED PLOTLY THEME =====
PLOTLY_LAYOUT = dict(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(family="Inter, sans-serif", color="#94a3b8", size=12),
    xaxis=dict(gridcolor="#1e293b", linecolor="#334155", tickcolor="#475569"),
    yaxis=dict(gridcolor="#1e293b", linecolor="#334155", tickcolor="#475569"),
    margin=dict(l=16, r=16, t=20, b=16),
    height=380,
)


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Evaluation</div>
            <div class="page-header-title">Model Results</div>
            <div class="page-header-sub">
                Comparison of machine learning models trained on the age group classification task
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== CONTEXT =====
    st.markdown("""
        <div class="info-card">
            Five machine learning models were trained and evaluated on the same preprocessed dataset
            after applying SMOTE for class balancing. Accuracy was used as the primary comparison metric.
            Gradient Boosting achieved the best overall performance and was selected as the final model.
        </div>
    """, unsafe_allow_html=True)

    # ===== METRIC CARDS =====
    st.markdown('<div class="section-title">Accuracy by Model</div>', unsafe_allow_html=True)

    models  = ["KNN", "SVM", "Random Forest", "Extra Trees", "Gradient Boosting"]
    acc     = [0.72,  0.51,  0.62,            0.69,          0.74]

    cols = st.columns(5)
    for col, name, val in zip(cols, models, acc):
        highlight = "color:#3b82f6;" if name == "Gradient Boosting" else ""
        col.markdown(f"""
            <div class="metric-card metric-card-accent">
                <div class="metric-card-value" style="{highlight}">{val:.2f}</div>
                <div class="metric-card-label">{name}</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===== ACCURACY CHART =====
    st.markdown('<div class="section-title">Accuracy Comparison</div>', unsafe_allow_html=True)

    colors = ["#3b82f6" if m == "Gradient Boosting" else "#334155" for m in models]

    fig = go.Figure(
        go.Bar(
            x=models,
            y=acc,
            marker=dict(color=colors, line=dict(width=0)),
            text=[f"{v:.0%}" for v in acc],
            textposition="outside",
            textfont=dict(color="#94a3b8", size=12),
        )
    )
    _layout = {**PLOTLY_LAYOUT, "showlegend": False,
               "yaxis": dict(range=[0, 0.9], gridcolor="#1e293b",
                             linecolor="#334155", tickformat=".0%")}
    fig.update_layout(**_layout)
    st.plotly_chart(fig, use_container_width=True, key="accuracy_chart")

    st.divider()

    # ===== TABLE =====
    st.markdown('<div class="section-title">Detailed Results</div>', unsafe_allow_html=True)

    data = pd.DataFrame({
        "Model":    models,
        "Accuracy": [f"{v:.2f}" for v in acc],
        "Rank":     [sorted(acc, reverse=True).index(v) + 1 for v in acc],
    })

    st.dataframe(data, use_container_width=True, hide_index=True)