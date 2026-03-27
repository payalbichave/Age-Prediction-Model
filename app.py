import streamlit as st
import overview
import data_analysis
import model_results
import final_model
import prediction
import conclusion

# ---------- PAGE CONFIG ---------- (must be first st command)
st.set_page_config(
    page_title="Age Prediction Dashboard",
    layout="wide",
)

# ---------- CSS ----------
st.markdown(
    """
<style>

/* ===== MAIN ===== */
.block-container {
    padding-top: 1rem;
    max-width: 1100px;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: #0b1120;
    border-right: 1px solid #1e293b;
    height: 100vh;
}

section[data-testid="stSidebar"] > div {
    height: 100vh;
    overflow: hidden;
    padding: 28px 18px 20px 18px;
    display: flex;
    flex-direction: column;
}

/* ===== LOGO / TITLE BLOCK ===== */
.sidebar-logo-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 18px 10px 22px 10px;
    margin-bottom: 10px;
    border-bottom: 1px solid #1e293b;
}

.sidebar-icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.sidebar-title {
    font-size: 22px;
    font-weight: 800;
    color: #f1f5f9;
    text-align: center;
    letter-spacing: 0.3px;
    margin-bottom: 3px;
}

.sidebar-sub {
    font-size: 12px;
    color: #64748b;
    text-align: center;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

/* ===== NAV LABEL ===== */
.nav-section-label {
    font-size: 10px;
    color: #475569;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 18px 4px 8px 4px;
    font-weight: 600;
}

/* ===== REMOVE RADIO CIRCLE ===== */
div[role="radiogroup"] label > div:first-child {
    display: none;
}

/* ===== NAV ITEMS ===== */
div[role="radiogroup"] {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

div[role="radiogroup"] label {
    width: 100%;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #94a3b8;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease;
    border: 1px solid transparent;
    white-space: nowrap;
}

/* hover */
div[role="radiogroup"] label:hover {
    background: #1e293b;
    color: #e2e8f0;
    border-color: #334155;
}

/* selected */
div[role="radiogroup"] label[data-selected="true"] {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
    color: #ffffff;
    font-weight: 700;
    border-color: #0ea5e9;
    box-shadow: 0 2px 12px rgba(14, 165, 233, 0.3);
}

/* ===== MAIN CONTENT ===== */
.main > div {
    padding-top: 0rem;
}

/* ===== STRADIO CONTAINER ===== */
div[data-testid="stRadio"] > label {
    display: none;
}

/* ===== FIX OVERSIZED CHARTS ===== */
div[data-testid="stPlotlyChart"] {
    max-width: 800px !important;
    margin: 0 auto;
}

div[data-testid="stImage"] img {
    max-width: 800px !important;
    width: 100% !important;
    height: auto !important;
    display: block;
    margin: 0 auto;
}

div[data-testid="stArrowVegaLiteChart"] {
    max-width: 800px !important;
    margin: 0 auto;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-logo-block">
            <div class="sidebar-icon">📊</div>
            <div class="sidebar-title">Age Insights</div>
            <div class="sidebar-sub">Prediction Dashboard</div>
        </div>
        <div class="nav-section-label">Navigation</div>
        """,
        unsafe_allow_html=True,
    )

    nav_items = {
        "Overview":      "🏠  Overview",
        "Data Analysis": "📈  Data Analysis",
        "Model Results": "🧪  Model Results",
        "Final Model":   "🤖  Final Model",
        "Prediction":    "🔮  Prediction",
        "Conclusion":    "✅  Conclusion",
    }

    page = st.radio(
        "",
        list(nav_items.keys()),
        format_func=lambda x: nav_items[x],
        key="main_nav",          # ← fixes duplicate ID error
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