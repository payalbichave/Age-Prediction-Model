import streamlit as st


def show():

    st.title("Final Model")

    st.write("Final Model: Gradient Boosting")

    st.write("Accuracy: 0.76")
    st.write("Precision: 0.27")
    st.write("Recall: 0.22")

    st.write("""
    SMOTE was used to balance the dataset.
    Gradient Boosting gave best performance.
    """)