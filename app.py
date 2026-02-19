import streamlit as st
from views import overall, development, maintenance, landing

# 設定頁面配置 (Must be the first Streamlit command)
st.set_page_config(
    page_title="Agentic RAG ROI 計算機",
    page_icon="📊",
    layout="wide"
)

# Custom CSS to improve Sidebar look
st.markdown("""
<style>
    /* Styling for the sidebar navigation to make it look more like tabs if possible, 
       though native radio buttons are standard. We can enhance later in Step 7. */
    section[data-testid="stSidebar"] .stRadio > label {
        font-weight: bold;
        color: #1C1B1F;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("導覽 (Navigation)")
# Using radio button for "Tab" like switching
page = st.sidebar.radio(
    "選擇頁面 (Select Page)",
    ["Overall", "開發", "維護", "導入與落地"],
    index=0
)

st.sidebar.markdown("---")

# Routing Logic
if page == "Overall":
    overall.show()
elif page == "開發":
    development.show()
elif page == "維護":
    maintenance.show()
elif page == "導入與落地":
    landing.show()
