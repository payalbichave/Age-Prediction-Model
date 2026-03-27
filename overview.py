import streamlit as st

def show():

    # ===== CUSTOM STYLE =====
    st.markdown("""
        <style>
        .main-title {
            font-size: 40px;
            font-weight: 600;
            color: white;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #bbb;
            margin-bottom: 30px;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            background-color: #1e1e1e;
            border: 1px solid #333;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # ===== TITLE =====
    st.markdown('<div class="main-title">Age Group Prediction Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Predict age group using survey-based data</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ===== PROJECT OVERVIEW =====
    st.subheader("Project Overview")

    st.markdown("""
    <div class="card">
    This project aims to predict whether a person belongs to the age group <b>under 35</b> or <b>35+</b> 
    based on survey responses. 

    The model learns patterns from features like education, income feeling, and opinions to classify users.
    </div>
    """, unsafe_allow_html=True)

    # ===== DATASET OVERVIEW =====
    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <b>Features:</b><br>
        • Gender <br>
        • Education Years <br>
        • Income Feeling <br>
        • Opinion Questions
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <b>Target Variable:</b> agegroup35 <br><br>
        • 1 → Under 35 <br>
        • 2 → 35 and above
        </div>
        """, unsafe_allow_html=True)

    # ===== ML INFO =====
    st.subheader("Model Information")

    st.markdown("""
    <div class="card">
    This is a <b>classification problem</b>. Multiple models were tested, and after handling 
    class imbalance using SMOTE, <b>Gradient Boosting</b> was selected as the final model 
    due to its better and balanced performance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ===== FOOTER =====
    st.markdown("""
    <div style='text-align: center; color: gray;'>
    Machine Learning Project • Streamlit Dashboard
    </div>
    """, unsafe_allow_html=True)