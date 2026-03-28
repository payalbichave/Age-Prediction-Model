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
    initial_sidebar_state="collapsed",
)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "Overview"
if "sidebar_collapsed" not in st.session_state:
    st.session_state.sidebar_collapsed = False

# ---------- NAV ITEMS ----------
nav_items = [
    ("Overview",      "⊞"),
    ("Data Analysis", "◈"),
    ("Model Results", "◆"),
    ("Final Model",   "◉"),
    ("Prediction",    "⚡"),
    ("Conclusion",    "✓"),
]

collapsed = st.session_state.sidebar_collapsed
sidebar_width  = "68px"  if collapsed else "220px"
content_margin = "84px"  if collapsed else "236px"

# ---------- CSS ----------
st.markdown(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">',
    unsafe_allow_html=True,
)

st.markdown(f"""
<style>
html, body, .stApp {{
    font-family: 'Inter', sans-serif !important;
    background: #0f172a !important;
}}
section[data-testid="stSidebar"] {{ display: none !important; }}
header[data-testid="stHeader"] {{ background: transparent !important; z-index: 1 !important; }}
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}

.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: {content_margin} !important;
    padding-right: 1.5rem !important;
    max-width: 100% !important;
}}

/* ── Sidebar shell ── */
#csb {{
    position: fixed;
    top: 0; left: 0;
    height: 100vh;
    width: {sidebar_width};
    background: #0f172a;
    border-right: 1px solid #1e293b;
    display: flex;
    flex-direction: column;
    z-index: 9998;
    overflow: hidden;
}}

/* Brand row */
.csb-brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 18px 14px 16px 14px;
    border-bottom: 1px solid #1e293b;
    flex-shrink: 0;
    white-space: nowrap;
    overflow: hidden;
}}
.csb-icon {{
    width: 38px; height: 38px; min-width: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; flex-shrink: 0;
}}
.csb-title  {{ font-size: 14px; font-weight: 700; color: #f0fafa; }}
.csb-desc   {{ font-size: 10.5px; color: #94a3b8; margin-top: 1px; }}
.csb-text   {{ overflow: hidden; display: {"block" if not collapsed else "none"}; }}

/* Nav label */
.csb-label {{
    font-size: 9px; font-weight: 700;
    letter-spacing: 1.8px; text-transform: uppercase;
    color: #475569;
    padding: 14px 14px 4px 14px;
    white-space: nowrap;
    display: {"block" if not collapsed else "none"};
}}

/* Nav list */
.csb-nav {{
    flex: 1;
    overflow-y: auto; overflow-x: hidden;
    padding: 6px 8px;
    display: flex; flex-direction: column; gap: 2px;
    scrollbar-width: none;
}}
.csb-nav::-webkit-scrollbar {{ display: none; }}

/* Nav item */
.csb-item {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 10px;
    border-radius: 9px;
    cursor: pointer;
    color: #94a3b8;
    font-size: 13px; font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-decoration: none;
    justify-content: {"flex-start" if not collapsed else "center"};
    position: relative;
}}
.csb-item:hover {{ background: #1e293b; color: #e2e8f0; }}
.csb-item.active {{
    background: #172554;
    color: #93c5fd; font-weight: 600;
}}
.csb-item.active::before {{
    content: '';
    position: absolute;
    left: 0; top: 20%; height: 60%; width: 3px;
    border-radius: 2px; background: #3b82f6;
    display: {"block" if not collapsed else "none"};
}}
.csb-ico  {{ font-size: 15px; flex-shrink: 0; min-width: 18px; text-align: center; line-height: 1; }}
.csb-lbl  {{ display: {"inline" if not collapsed else "none"}; overflow: hidden; text-overflow: ellipsis; }}

/* Footer */
.csb-footer {{
    padding: 12px 14px;
    border-top: 1px solid #1e293b;
    font-size: 10px; color: #475569;
    text-align: center;
    white-space: nowrap; overflow: hidden;
    flex-shrink: 0;
}}

/* Toggle tab */
.csb-toggle {{
    position: fixed;
    top: 50%;
    left: {sidebar_width};
    transform: translateY(-50%);
    z-index: 9999;
    width: 16px; height: 48px;
    background: #1e293b;
    border: 1px solid #334155;
    border-left: none;
    border-radius: 0 6px 6px 0;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    color: #94a3b8;
    font-size: 9px; font-weight: 700;
    text-decoration: none;
    user-select: none;
    line-height: 1;
}}
.csb-toggle:hover {{ background: #2563eb; color: white; }}

/* ── Page components ── */
.metric-card {{ background:#1e293b; border:1px solid #334155; border-radius:10px; padding:18px 16px; text-align:center; }}
.metric-card-value {{ font-size:24px; font-weight:700; color:#f1f5f9; line-height:1.2; }}
.metric-card-label {{ font-size:12px; font-weight:500; color:#64748b; text-transform:uppercase; letter-spacing:0.8px; margin-top:4px; }}
.metric-card-accent {{ border-top:3px solid #3b82f6; }}
.info-card {{ background:#1e293b; border:1px solid #334155; border-radius:10px; padding:20px; margin-bottom:16px; font-size:14px; color:#cbd5e1; line-height:1.7; }}
.list-item {{ display:flex; align-items:flex-start; gap:10px; padding:10px 14px; background:#1e293b; border:1px solid #334155; border-radius:8px; margin-bottom:8px; font-size:14px; color:#cbd5e1; }}
.list-item-dot {{ width:6px; height:6px; border-radius:50%; background:#3b82f6; margin-top:6px; flex-shrink:0; }}
.chart-caption {{ background:#1e293b; border-left:3px solid #3b82f6; border-radius:0 6px 6px 0; padding:10px 14px; margin:8px 0 24px 0; color:#94a3b8; font-size:13px; line-height:1.6; }}
.section-title {{ font-size:15px; font-weight:600; color:#e2e8f0; margin-bottom:12px; padding-bottom:8px; border-bottom:1px solid #1e293b; }}
.page-header {{ margin-bottom:1.75rem; }}
.page-header-tag {{ font-size:11px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; color:#3b82f6; margin-bottom:6px; }}
.page-header-title {{ font-size:26px; font-weight:700; color:#f1f5f9; line-height:1.3; margin-bottom:6px; }}
.page-header-sub {{ font-size:14px; color:#64748b; }}
.step-box {{ background:#1e293b; border:1px solid #334155; border-radius:8px; padding:14px 12px; text-align:center; margin-bottom:10px; }}
.step-index {{ font-size:11px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:#3b82f6; margin-bottom:4px; }}
.step-text {{ font-size:13px; font-weight:500; color:#cbd5e1; }}
.result-box {{ background:#1e293b; border:1px solid #334155; border-radius:10px; padding:20px; margin-bottom:16px; }}
.result-box-label {{ font-size:11px; font-weight:600; letter-spacing:1px; color:#64748b; text-transform:uppercase; margin-bottom:6px; }}
.result-box-value {{ font-size:20px; font-weight:700; color:#f1f5f9; }}
.interpret-box {{ background:#1e293b; border:1px solid #334155; border-radius:10px; padding:22px; font-size:14px; color:#cbd5e1; line-height:1.8; }}
hr[data-testid="stDivider"] {{ border-color:#1e293b !important; margin:1.5rem 0 !important; }}
.stButton > button {{ background:#2563eb; color:#fff; border:none; border-radius:7px; font-weight:600; font-size:14px; padding:0.55rem 1.5rem; width:100%; transition:background 0.15s; }}
.stButton > button:hover {{ background:#1d4ed8; }}
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {{ background:#1e293b !important; border-color:#334155 !important; color:#f1f5f9 !important; border-radius:7px !important; font-size:14px !important; }}
label[data-testid="stWidgetLabel"] p {{ font-size:13px !important; font-weight:500 !important; color:#94a3b8 !important; }}
div[data-testid="stDataFrame"] {{ border-radius:10px; overflow:hidden; border:1px solid #334155; }}
div[data-testid="stAlert"] {{ border-radius:8px !important; border:1px solid #334155 !important; font-size:14px !important; }}
</style>
""", unsafe_allow_html=True)

# ---------- BUILD SIDEBAR HTML ----------
nav_rows = ""
for key, icon in nav_items:
    active_cls = "active" if st.session_state.page == key else ""
    nav_rows += (
        f'<a class="csb-item {active_cls}" href="?nav={key}" title="{key}" target="_self">'
        f'<span class="csb-ico">{icon}</span>'
        f'<span class="csb-lbl">{key}</span>'
        f'</a>'
    )

toggle_char = "&#9658;" if collapsed else "&#9668;"
footer_txt  = "v1.0" if collapsed else "Age Group Prediction &middot; v1.0"

st.markdown(
    f'<div id="csb">'
    f'  <div class="csb-brand">'
    f'    <div class="csb-icon">&#9685;</div>'
    f'    <div class="csb-text">'
    f'      <div class="csb-title">Age Insights</div>'
    f'      <div class="csb-desc">Prediction Dashboard</div>'
    f'    </div>'
    f'  </div>'
    f'  <div class="csb-label">Navigation</div>'
    f'  <div class="csb-nav">{nav_rows}</div>'
    f'  <div class="csb-footer">{footer_txt}</div>'
    f'</div>'
    f'<a class="csb-toggle" href="?toggle=1" title="Toggle sidebar" target="_self">{toggle_char}</a>',
    unsafe_allow_html=True,
)

# ---------- HANDLE QUERY PARAMS ----------
qp = st.query_params

if "toggle" in qp:
    st.session_state.sidebar_collapsed = not st.session_state.sidebar_collapsed
    st.query_params.clear()
    st.rerun()

if "nav" in qp:
    val = qp["nav"]
    if val in [k for k, _ in nav_items]:
        st.session_state.page = val
    st.query_params.clear()
    st.rerun()

# ---------- ROUTING ----------
page = st.session_state.page
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
