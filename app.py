import streamlit as st
from views import overall, development, maintenance, landing

# 設定頁面配置 (Must be the first Streamlit command)
st.set_page_config(
    page_title="Agentic RAG ROI 計算機",
    page_icon="📊",
    layout="wide"
)

# Custom CSS to improve Sidebar look
# Global CSS with High Contrast Improvements
st.markdown("""
<style>
    /* Global Font - Roboto */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    /* M3 Cards (Containers) - Darkened for better contrast against white background */
    div[data-testid="stMetric"] {
        background-color: #E8DEF8; /* Surface Container - Slightly darker than previous F3EDF7 */
        border: 1px solid #D0BCFF; /* Add border for definition */
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.15); /* Slightly stronger shadow */
        transition: transform 0.2s;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Primary Button (Filled) - Higher Contrast */
    div.stButton > button {
        background-color: #6200EE; /* Deep Purple / Primary Key Color */
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.6rem 1.6rem;
        font-weight: 600; /* Bolder text */
        letter-spacing: 0.5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.4); /* stronger shadow */
        transition: background-color 0.2s, box-shadow 0.2s;
    }
    div.stButton > button:hover {
        background-color: #3700B3; /* Darker Purple on Hover */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
        color: white;
        border: 1px solid #FFFFFF; /* High contrast border on hover */
    }
    div.stButton > button:active {
        background-color: #000000; /* Black on active for max feedback */
        color: white;
    }

    /* Headers */
    h1, h2, h3 {
        color: #000000; /* High Contrast Black instead of #1C1B1F */
        font-weight: 600;
    }

    /* Sidebar - Increase contrast of background */
    section[data-testid="stSidebar"] {
        background-color: #F3E5F5; /* Slightly richer purple/pink tint to differentiate from main white */
        border-right: 1px solid #E1E1E1;
    }
    
    /* Sidebar Navigation Items */
    section[data-testid="stSidebar"] .stRadio > label {
        font-weight: bold;
        color: #000000; /* Black text for nav items */
        font-size: 1.05rem;
    }

    /* Inputs (Standard Rounded) - Darker background for visibility */
    div[data-baseweb="input"] > div {
        border-radius: 8px;
        background-color: #F0F0F0; /* Darker Surface Variant */
        border: 1px solid #B0B0B0; /* Add border */
    }
    
    /* Sliders */
    div[role="slider"] {
        color: #6200EE;
    }

</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("導覽 (Navigation)")
# Using radio button for "Tab" like switching
page = st.sidebar.radio(
    "選擇頁面 (Select Page)",
    ["📊 Overall", "💻 開發", "🛠️ 維護", "🚀 導入與落地"],
    index=0
)

st.sidebar.markdown("---")

# Routing Logic
if page == "📊 Overall":
    overall.show()
elif page == "💻 開發":
    development.show()
elif page == "🛠️ 維護":
    maintenance.show()
elif page == "🚀 導入與落地":
    landing.show()
