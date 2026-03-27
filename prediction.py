import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go
import pandas as pd


# ---------- LOAD MODEL ----------
model  = pickle.load(open("model.pkl",  "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

AGE_GROUPS = {1: "Under 35", 2: "35 and above"}

PLOTLY_LAYOUT = dict(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(family="Inter, sans-serif", color="#94a3b8", size=12),
    xaxis=dict(gridcolor="#1e293b", linecolor="#334155"),
    yaxis=dict(gridcolor="#1e293b", linecolor="#334155", tickformat=".0%", range=[0, 0.55]),
    margin=dict(l=16, r=16, t=24, b=16),
    height=320,
    showlegend=False,
)

FEATURE_LABELS = {
    "gndr":    "Gender",
    "eduyrs":  "Education Years",
    "hincfel": "Income Feeling",
    "w4gq1":   "Agreement Level",
    "w4gq2":   "Satisfaction Level",
}


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Live Inference</div>
            <div class="page-header-title">Prediction</div>
            <div class="page-header-sub">Enter survey values to classify the respondent into an age group</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== INPUT FORM =====
    st.markdown('<div class="section-title">Input Parameters</div>', unsafe_allow_html=True)

    col_form, col_result = st.columns([1, 1], gap="large")

    with col_form:
        gndr    = st.selectbox("Gender", options=[1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
        eduyrs  = st.number_input("Education Years", min_value=0,  max_value=25, value=12, step=1)
        hincfel = st.number_input("Income Feeling (1 = Comfortable · 4 = Very difficult)", min_value=1, max_value=4, value=2, step=1)
        w4gq1   = st.number_input("Agreement Level  (1 = Strongly disagree · 5 = Strongly agree)", min_value=1, max_value=5, value=3, step=1)
        w4gq2   = st.number_input("Satisfaction Level  (1 = Not satisfied · 5 = Very satisfied)", min_value=1, max_value=5, value=3, step=1)

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        predict_clicked = st.button("Run Prediction")

    # ===== RESULT =====
    with col_result:
        if predict_clicked:
            # Create a dataframe with the exact feature names the model was trained on
            input_data = pd.DataFrame(
                [[gndr, eduyrs, hincfel, w4gq1, w4gq2]],
                columns=["gndr", "eduyrs", "hincfel", "w4gq1", "w4gq2"]
            )
            
            # Predict
            input_scaled = scaler.transform(input_data)
            
            # We are using pure scikit-learn defaults (50% boundary) to ensure mathematically 
            # accurate predictions directly from the trained Gradient Boosting model.
            pred         = model.predict(input_scaled)[0]
            proba        = model.predict_proba(input_scaled)[0]
            confidence   = max(proba)
                
            label = AGE_GROUPS[pred]

            # Result card
            icon  = "👤" if pred == 1 else "👥"
            color = "#1e9e7e" if pred == 1 else "#38bdf8"
            
            st.markdown(f"""
                <div class="result-box">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div>
                            <div class="result-box-label">Predicted Age Group</div>
                            <div class="result-box-value" style="color:{color};font-size:24px;">{icon} {label}</div>
                        </div>
                        <div style="text-align:right;">
                            <div class="result-box-label">Confidence Score</div>
                            <div style="font-size:18px; font-weight:700; color:#f8fafc;">{confidence:.1%}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Insights
            st.markdown('<div class="section-title" style="margin-top:16px;">Prediction Insights</div>', unsafe_allow_html=True)

            reasons = []
            if pred == 2:
                if eduyrs  > 15: reasons.append("More years of education strongly correlates with the 35+ demographic in this dataset.")
                if hincfel >= 3: reasons.append("Reporting financial difficulties (Income Feeling 3 or 4) is statistically common in the older demographic.")
                if w4gq1   <= 2: reasons.append("Lower agreement levels are frequently observed in the 35+ group.")
                if w4gq2   <= 2: reasons.append("Lower satisfaction scores align with the baseline of the older age group.")
            else:
                if eduyrs  <= 15: reasons.append("Fewer education years leans toward the younger under-35 group.")
                if hincfel <= 2: reasons.append("Reporting comfortable income levels aligns more with the younger demographic.")
                if w4gq1   >= 4: reasons.append("Higher agreement response aligns strongly with younger respondents.")
                if w4gq2   >= 4: reasons.append("Higher satisfaction scores are typically more common under age 35.")

            if not reasons:
                reasons.append("Prediction based on the combined pattern of all input features")

            for r in reasons:
                st.markdown(f"""
                    <div class="list-item">
                        <div class="list-item-dot"></div>
                        <span>{r}</span>
                    </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown("""
                <div class="info-card" style="color:#64748b;font-size:13px;text-align:center;padding:32px;">
                    Fill in the parameters and click <strong style="color:#94a3b8">Run Prediction</strong> to classify.
                </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ===== FEATURE IMPORTANCE =====
    st.markdown('<div class="section-title">Feature Importance</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card" style="margin-bottom:16px;">
            How much each feature contributed to the Gradient Boosting model's decisions across all training samples.
        </div>
    """, unsafe_allow_html=True)

    raw_names  = ["gndr", "eduyrs", "hincfel", "w4gq1", "w4gq2"]
    nice_names = [FEATURE_LABELS[n] for n in raw_names]
    importance = list(model.feature_importances_)

    sorted_pairs = sorted(zip(importance, nice_names), reverse=True)
    imp_sorted   = [p[0] for p in sorted_pairs]
    lbl_sorted   = [p[1] for p in sorted_pairs]

    fig = go.Figure(
        go.Bar(
            x=lbl_sorted,
            y=imp_sorted,
            marker=dict(
                color=["#3b82f6" if i == 0 else "#334155" for i in range(len(lbl_sorted))],
                line=dict(width=0),
            ),
            text=[f"{v:.3f}" for v in imp_sorted],
            textposition="outside",
            textfont=dict(color="#94a3b8", size=11),
        )
    )
    fig.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig, use_container_width=True, key="feature_importance_chart")