import streamlit as st


def show():

    st.title("Conclusion")

    st.write("""
    Machine learning was used to predict age group.

    Dataset was imbalanced, so SMOTE was applied.

    Multiple models were tested.

    Gradient Boosting gave best performance.

    Dashboard allows prediction for new users.
    """)