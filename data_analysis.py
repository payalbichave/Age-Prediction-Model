import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ===== SHARED CHART STYLE =====
CHART_BG      = "#0f172a"
AXIS_COLOR    = "#475569"
LABEL_COLOR   = "#94a3b8"
BAR_PALETTE   = ["#3b82f6", "#1d4ed8"]

def _style_axes(ax, fig):
    fig.patch.set_facecolor(CHART_BG)
    ax.set_facecolor(CHART_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(AXIS_COLOR)
        spine.set_linewidth(0.6)
    ax.tick_params(colors=LABEL_COLOR, labelsize=10)
    ax.xaxis.label.set_color(LABEL_COLOR)
    ax.yaxis.label.set_color(LABEL_COLOR)
    ax.title.set_color("#e2e8f0")
    ax.title.set_fontsize(13)
    ax.title.set_fontweight("600")
    ax.grid(axis="y", color="#1e293b", linewidth=0.8)
    ax.set_axisbelow(True)


def _plot_section(fig, caption_text):
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    with col2:
        st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown(
        f'<div class="chart-caption">{caption_text}</div>',
        unsafe_allow_html=True,
    )
    st.divider()


def show():

    # ===== PAGE HEADER =====
    st.markdown("""
        <div class="page-header">
            <div class="page-header-tag">Exploratory Analysis</div>
            <div class="page-header-title">Data Analysis</div>
            <div class="page-header-sub">Visualising key distributions and feature relationships in the dataset</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== LOAD DATA =====
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.lower()
    df = df[df["agegroup35"] != 9]

    sns.set_theme(style="dark", rc={"axes.facecolor": CHART_BG, "figure.facecolor": CHART_BG})

    # ===== GRAPH 1 — Age Distribution =====
    st.markdown('<div class="section-title">Age Group Distribution</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="agegroup35", data=df, ax=ax, palette=BAR_PALETTE)
    ax.set_xlabel("Age Group (1 = Under 35, 2 = 35+)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Age Groups")
    _style_axes(ax, fig)
    plt.tight_layout()
    _plot_section(fig, "The dataset shows an imbalance between the two age groups, which is why SMOTE was applied during model training.")

    # ===== GRAPH 2 — Gender vs Age Group =====
    st.markdown('<div class="section-title">Gender vs Age Group</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="gndr", hue="agegroup35", data=df, ax=ax, palette=BAR_PALETTE)
    ax.set_xlabel("Gender (1 = Male, 2 = Female)")
    ax.set_ylabel("Count")
    ax.set_title("Gender Distribution by Age Group")
    _style_axes(ax, fig)
    legend = ax.get_legend()
    if legend:
        legend.get_frame().set_facecolor(CHART_BG)
        for text in legend.get_texts():
            text.set_color(LABEL_COLOR)
    plt.tight_layout()
    _plot_section(fig, "Both genders are represented across age groups with a broadly similar distribution pattern.")

    # ===== GRAPH 3 — Education vs Age Group =====
    st.markdown('<div class="section-title">Education Level vs Age Group</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="eisced", hue="agegroup35", data=df, ax=ax, palette=BAR_PALETTE)
    ax.set_xlabel("Education Level (EISCED)")
    ax.set_ylabel("Count")
    ax.set_title("Education Level by Age Group")
    _style_axes(ax, fig)
    legend = ax.get_legend()
    if legend:
        legend.get_frame().set_facecolor(CHART_BG)
        for text in legend.get_texts():
            text.set_color(LABEL_COLOR)
    plt.tight_layout()
    _plot_section(fig, "Higher education levels tend to have more representation in the older age group, suggesting a positive correlation.")

    # ===== GRAPH 4 — Income Feeling vs Age Group =====
    st.markdown('<div class="section-title">Income Perception vs Age Group</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x="hincfel", hue="agegroup35", data=df, ax=ax, palette=BAR_PALETTE)
    ax.set_xlabel("Income Feeling (1 = Living comfortably → 4 = Very difficult)")
    ax.set_ylabel("Count")
    ax.set_title("Income Perception by Age Group")
    _style_axes(ax, fig)
    legend = ax.get_legend()
    if legend:
        legend.get_frame().set_facecolor(CHART_BG)
        for text in legend.get_texts():
            text.set_color(LABEL_COLOR)
    plt.tight_layout()
    _plot_section(fig, "Income perception varies across age groups, with the middle range being most prevalent for both classes.")