import streamlit as st


def show():

    st.title("Model Results")

    st.write("Comparison of models")

    st.write("""
    Random Forest
    SVM
    Gradient Boosting
    KNN
    Extra Trees
    """)

    st.write("Final model selected after SMOTE")