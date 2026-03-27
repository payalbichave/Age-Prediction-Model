import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show():
    st.title("📊 Data Analysis")

    # ===== LOAD DATA =====
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.lower()
    df = df[df["agegroup35"] != 9]

    # ===== STYLE =====
    sns.set_theme(style="darkgrid")
    PALETTE = "Blues_d"

    # helper — renders chart + styled caption
    def plot_section(fig, caption_text):
        col1, col2, col3 = st.columns([0.5, 3, 0.5])   # centre + constrain width to ~75%
        with col2:
            st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        st.markdown(
            f"""
            <div style="
                background: #1e293b;
                border-left: 4px solid #0ea5e9;
                border-radius: 6px;
                padding: 12px 16px;
                margin: 6px 0 24px 0;
                color: #94a3b8;
                font-size: 14px;
                line-height: 1.6;
            ">
                💡 {caption_text}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.divider()

    # ===== GRAPH 1 =====
    st.subheader("1. Age Group Distribution")
    fig, ax = plt.subplots(figsize=(4, 2.5))
    sns.countplot(x="agegroup35", data=df, ax=ax, palette=PALETTE)
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Count")
    ax.set_title("Age Distribution")
    plt.tight_layout()
    plot_section(fig, "This graph shows how data is distributed between the two age groups.")

    # ===== GRAPH 2 =====
    st.subheader("2. Gender vs Age Group")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="gndr", hue="agegroup35", data=df, ax=ax, palette=PALETTE)
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")
    ax.set_title("Gender vs Age Group")
    plt.tight_layout()
    plot_section(fig, "This graph compares age groups across different genders.")

    # ===== GRAPH 3 =====
    st.subheader("3. Education vs Age Group")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="eisced", hue="agegroup35", data=df, ax=ax, palette=PALETTE)
    ax.set_xlabel("Education Level")
    ax.set_ylabel("Count")
    ax.set_title("Education vs Age Group")
    plt.tight_layout()
    plot_section(fig, "This graph shows how education levels vary between age groups.")

    # ===== GRAPH 4 =====
    st.subheader("4. Income vs Age Group")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="hincfel", hue="agegroup35", data=df, ax=ax, palette=PALETTE)
    ax.set_xlabel("Income Feeling")
    ax.set_ylabel("Count")
    ax.set_title("Income vs Age Group")
    plt.tight_layout()
    plot_section(fig, "This graph shows how income perception differs across age groups.")