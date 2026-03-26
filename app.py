import streamlit as st
import overview
import data_analysis
import model_results
import final_model
import prediction
import conclusion


st.set_page_config(
    page_title="Age Prediction Dashboard",
    layout="wide"
)


st.title("Age Group Prediction Dashboard")


# ===== SIDEBAR DESIGN =====

st.sidebar.title("📊 Dashboard Menu")

st.sidebar.markdown("---")

st.sidebar.write("Project:")
st.sidebar.write("Age Group Prediction")

st.sidebar.markdown("---")


page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Overview",
        "📊 Data Analysis",
        "📈 Model Results",
        "🤖 Final Model",
        "🔮 Prediction",
        "✅ Conclusion",
    ],
)


st.sidebar.markdown("---")
st.sidebar.write("ML Project")
st.sidebar.write("Gradient Boosting Model")


# ===== PAGE CONTROL =====

if page == "🏠 Overview":
    overview.show()

elif page == "📊 Data Analysis":
    data_analysis.show()

elif page == "📈 Model Results":
    model_results.show()

elif page == "🤖 Final Model":
    final_model.show()

elif page == "🔮 Prediction":
    prediction.show()

elif page == "✅ Conclusion":
    conclusion.show()