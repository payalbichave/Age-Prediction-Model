import streamlit as st


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Introduction</div>
            <div class="page-header-title">Age Group Prediction</div>
            <div class="page-header-sub">Classifying individuals into age groups using survey-based machine learning</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== PROJECT OVERVIEW =====
    st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            This project predicts whether a person belongs to the age group <strong style="color:#f1f5f9">Under 35</strong>
            or <strong style="color:#f1f5f9">35 and above</strong> based on survey responses.
            The model learns patterns from demographic and opinion-based features to perform binary classification.
        </div>
    """, unsafe_allow_html=True)

    # ===== DATASET OVERVIEW =====
    st.markdown('<div class="section-title">Dataset Overview</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title" style="font-size:13px;border:none;padding:0;margin-bottom:8px;">Input Features</div>', unsafe_allow_html=True)
        for feature in ["Gender", "Education Years", "Income Feeling", "Agreement Level (w4gq1)", "Satisfaction Level (w4gq2)"]:
            st.markdown(f"""
                <div class="list-item">
                    <div class="list-item-dot"></div>
                    <span>{feature}</span>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title" style="font-size:13px;border:none;padding:0;margin-bottom:8px;">Target Variable</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="info-card" style="margin-bottom:8px;">
                <strong style="color:#f1f5f9">agegroup35</strong>
            </div>
        """, unsafe_allow_html=True)
        for label in ["Class 1 — Under 35", "Class 2 — 35 and above"]:
            st.markdown(f"""
                <div class="list-item">
                    <div class="list-item-dot"></div>
                    <span>{label}</span>
                </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ===== MODEL INFORMATION =====
    st.markdown('<div class="section-title">Model Information</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            This is a <strong style="color:#f1f5f9">binary classification</strong> problem.
            Multiple machine learning algorithms were evaluated and compared.
            Class imbalance was addressed using <strong style="color:#f1f5f9">SMOTE</strong> (Synthetic Minority Oversampling Technique).
            <strong style="color:#f1f5f9">Gradient Boosting</strong> was selected as the final model based on its superior
            and balanced performance across accuracy, precision, and recall.
        </div>
    """, unsafe_allow_html=True)

    # ===== QUICK STATS =====
    st.markdown('<div class="section-title">At a Glance</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("5", "Models Tested"),
        ("5", "Features"),
        ("74%", "Best Accuracy"),
        ("SMOTE", "Balancing Method"),
    ]
    for col, (val, label) in zip([c1, c2, c3, c4], stats):
        col.markdown(f"""
            <div class="metric-card metric-card-accent">
                <div class="metric-card-value">{val}</div>
                <div class="metric-card-label">{label}</div>
            </div>
        """, unsafe_allow_html=True)