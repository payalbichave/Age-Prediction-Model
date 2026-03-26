import streamlit as st
import pandas as pd


def show():

    st.title("Data Analysis")

    df = pd.read_csv("data.csv")

    st.write("Dataset shape:", df.shape)

    st.write("Columns:", df.columns)

    st.write(df.head())

    st.bar_chart(df["agegroup35"].value_counts())