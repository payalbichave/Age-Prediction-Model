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
    height=320,
    legend=dict(bgcolor="#0f172a", bordercolor="#334155", borderwidth=1),
)


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Summary</div>
            <div class="page-header-title">Conclusion</div>
            <div class="page-header-sub">Key takeaways, achievements, and interpretation of the project results</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== METRIC CARDS =====
    st.markdown('<div class="section-title">Project at a Glance</div>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    metrics = [
        ("5",     "Models Tested"),
        ("74%",   "Best Accuracy"),
        ("5",     "Input Features"),
        ("SMOTE", "Balancing"),
        ("GB",    "Final Model"),
    ]
    for col, (val, label) in zip([col1, col2, col3, col4, col5], metrics):
        col.markdown(f"""
            <div class="metric-card metric-card-accent">
                <div class="metric-card-value">{val}</div>
                <div class="metric-card-label">{label}</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===== TWO COLUMN SECTION =====
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-title">Key Achievements</div>', unsafe_allow_html=True)
        achievements = [
            "Performed exploratory data analysis on survey data",
            "Handled class imbalance via SMOTE oversampling",
            "Trained and benchmarked 5 ML algorithms",
            "Selected Gradient Boosting as the final model",
            "Built an interactive multi-page Streamlit dashboard",
            "Implemented live prediction with insight explanations",
        ]
        for text in achievements:
            st.markdown(f"""
                <div class="list-item">
                    <div class="list-item-dot"></div>
                    <span>{text}</span>
                </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-title">Accuracy Across Models</div>', unsafe_allow_html=True)
        models   = ["KNN", "SVM", "Random Forest", "Extra Trees", "Gradient Boosting"]
        accuracy = [0.72,  0.51,  0.62,            0.69,          0.74]
        colors   = ["#3b82f6" if m == "Gradient Boosting" else "#334155" for m in models]

        fig = go.Figure(go.Bar(
            x=models, y=accuracy,
            marker=dict(color=colors, line=dict(width=0)),
            text=[f"{v:.0%}" for v in accuracy],
            textposition="outside",
            textfont=dict(color="#94a3b8", size=11),
        ))
        layout = {**PLOTLY_LAYOUT, "showlegend": False,
                  "yaxis": dict(range=[0, 0.9], gridcolor="#1e293b",
                                linecolor="#334155", tickformat=".0%")}
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True, key="conclusion_accuracy_chart")

    st.divider()

    # ===== WORKFLOW =====
    st.markdown('<div class="section-title">Project Workflow</div>', unsafe_allow_html=True)

    steps = [
        ("1", "Data Collection"),
        ("2", "Data Cleaning"),
        ("3", "Exploratory Analysis"),
        ("4", "SMOTE Balancing"),
        ("5", "Model Training"),
        ("6", "Model Comparison"),
        ("7", "Final Model Selection"),
        ("8", "Dashboard Creation"),
    ]

    step_cols = st.columns(4)
    for i, (num, step) in enumerate(steps):
        with step_cols[i % 4]:
            st.markdown(f"""
                <div class="step-box">
                    <div class="step-index">Step {num}</div>
                    <div class="step-text">{step}</div>
                </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ===== INTERPRETATION =====
    st.markdown('<div class="section-title">Project Interpretation</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="interpret-box">
            The analysis demonstrates that demographic and opinion-based survey features carry meaningful
            signals for classifying individuals into age groups. Variables such as education level, income
            perception, and personal opinions collectively provide enough information for a machine learning
            model to distinguish between the &ldquo;under 35&rdquo; and &ldquo;35 and above&rdquo; cohorts
            with <strong style="color:#f1f5f9">74% accuracy</strong>.<br><br>
            The application of SMOTE was critical in improving generalisation — without it, the model
            defaulted to predicting the majority class. Gradient Boosting proved to be the most robust
            algorithm for this tabular, survey-based classification task, outperforming alternatives
            in both accuracy and the balance of precision and recall.
        </div>
    """, unsafe_allow_html=True)