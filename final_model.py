import streamlit as st
import plotly.graph_objects as go
import pandas as pd


PLOTLY_LAYOUT = dict(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(family="Inter, sans-serif", color="#94a3b8", size=12),
    xaxis=dict(gridcolor="#1e293b", linecolor="#334155"),
    yaxis=dict(gridcolor="#1e293b", linecolor="#334155", tickformat=".0%"),
    margin=dict(l=16, r=16, t=24, b=16),
    height=340,
    legend=dict(bgcolor="#0f172a", bordercolor="#334155", borderwidth=1),
)


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Selection</div>
            <div class="page-header-title">Final Model</div>
            <div class="page-header-sub">Gradient Boosting selected as the best-performing model for age group prediction</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== METRIC CARDS =====
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("Gradient Boosting", "Algorithm"),
        ("0.76",              "Accuracy"),
        ("0.27",              "Precision"),
        ("0.22",              "Recall"),
    ]
    for col, (val, label) in zip([c1, c2, c3, c4], cards):
        col.markdown(f"""
            <div class="metric-card metric-card-accent">
                <div class="metric-card-value">{val}</div>
                <div class="metric-card-label">{label}</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===== TWO COLUMNS =====
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-title">Why Gradient Boosting?</div>', unsafe_allow_html=True)
        reasons = [
            "Best overall accuracy among all tested models",
            "Performs well after SMOTE balancing",
            "Handles survey-based tabular data efficiently",
            "Provides stable predictions across folds",
            "Balanced accuracy, precision and recall",
            "Robust on imbalanced classification problems",
        ]
        for r in reasons:
            st.markdown(f"""
                <div class="list-item">
                    <div class="list-item-dot"></div>
                    <span>{r}</span>
                </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-title">Model Comparison</div>', unsafe_allow_html=True)

        comp_models = ["Gradient Boosting", "Random Forest"]
        accuracy    = [0.76, 0.71]
        precision   = [0.27, 0.16]
        recall      = [0.22, 0.22]
        f1          = [0.30, 0.18]

        colors_gb = ["#3b82f6", "#334155"]
        fig = go.Figure()

        for name, vals, color in [
            ("Accuracy",  accuracy,  "#3b82f6"),
            ("Precision", precision, "#0ea5e9"),
            ("Recall",    recall,    "#38bdf8"),
            ("F1 Score",  f1,        "#7dd3fc"),
        ]:
            fig.add_trace(go.Bar(name=name, x=comp_models, y=vals, marker_color=color))

        fig.update_layout(**PLOTLY_LAYOUT, barmode="group")
        st.plotly_chart(fig, use_container_width=True, key="bar_chart_final_model")

    st.divider()

    # ===== SMOTE TABLE =====
    st.markdown('<div class="section-title">SMOTE Effect on Performance</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card" style="margin-bottom:16px;">
            Before SMOTE, the model was biased toward the majority class, yielding high accuracy but near-zero
            precision and recall for the minority class. SMOTE balanced the training set, improving generalisation.
        </div>
    """, unsafe_allow_html=True)

    data = pd.DataFrame({
        "Metric":    ["Accuracy", "Precision", "Recall"],
        "Before SMOTE": ["0.83", "0.00", "0.00"],
        "After SMOTE":  ["0.73", "0.26", "0.26"],
        "Change":       ["−0.10", "+0.26", "+0.26"],
    })

    st.dataframe(data, use_container_width=True, hide_index=True)