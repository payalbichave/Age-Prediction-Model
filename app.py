import streamlit as st

import overview
import data_analysis
import model_results
import final_model
import prediction
import conclusion


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Age Prediction Dashboard",
    layout="wide",
)


# ---------- CSS ----------
st.markdown(
    """
<style>

/* ===== REMOVE TOP SPACE ===== */

.block-container {
    padding-top: 1rem;
}


/* ===== SIDEBAR BACKGROUND ===== */

section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid #111827;
}


/* remove sidebar top gap */

section[data-testid="stSidebar"] > div {
    padding-top: 10px;
}


/* header text */

.sidebar-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 0px;
}

.sidebar-sub {
    font-size: 13px;
    color: #94a3b8;
    margin-bottom: 10px;
}


/* navigation label */

.nav-title {
    font-size: 11px;
    color: #64748b;
    margin-top: 10px;
    margin-bottom: 5px;
    letter-spacing: 1px;
}


/* ===== REMOVE RADIO CIRCLES ===== */

div[role="radiogroup"] label > div:first-child {
    display: none;
}


/* ===== STYLE NAV ITEMS ===== */

div[role="radiogroup"] label {
    padding: 8px;
    border-radius: 8px;
    margin-bottom: 4px;
    background: transparent;
}

div[role="radiogroup"] label:hover {
    background: #0f172a;
}

div[role="radiogroup"] label[data-selected="true"] {
    background: #0ea5e9;
    color: white;
    font-weight: 600;
}


/* remove extra margin in main */

.main > div {
    padding-top: 0rem;
}

</style>
""",
    unsafe_allow_html=True,
)


# ---------- TITLE ----------
st.title("Age Group Prediction Dashboard")


# ---------- SIDEBAR ----------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">Age Analytics</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-sub">Prediction Dashboard</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="nav-title">NAVIGATION</div>',
        unsafe_allow_html=True,
    )

    page = st.radio(
        "",
        [
            "Overview",
            "Data Analysis",
            "Model Results",
            "Final Model",
            "Prediction",
            "Conclusion",
        ],
    )


# ---------- ROUTING ----------
if page == "Overview":
    overview.show()

elif page == "Data Analysis":
    data_analysis.show()

elif page == "Model Results":
    model_results.show()

elif page == "Final Model":
    final_model.show()

elif page == "Prediction":
    prediction.show()

elif page == "Conclusion":
    conclusion.show()