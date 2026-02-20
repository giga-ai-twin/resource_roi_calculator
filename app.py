import streamlit as st
from views import overall, development, maintenance, landing
from translations import TRANSLATIONS

# Initialize language session state
if 'lang' not in st.session_state:
    st.session_state.lang = 'zh-tw'

def swap_lang():
    if st.session_state.lang == 'zh-tw':
        st.session_state.lang = 'en'
    else:
        st.session_state.lang = 'zh-tw'

# 設定頁面配置 (Must be the first Streamlit command)
st.set_page_config(
    page_title="Agentic RAG ROI 計算機",
    page_icon="📊",
    layout="wide"
)

# Get current translations
t = TRANSLATIONS[st.session_state.lang]

# Global CSS with High Contrast Improvements and Top-Right positioning
st.markdown(f"""
<style>
    /* Global Font - Roboto */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Roboto', sans-serif;
    }}

    /* Position the button at the top-right */
    .stButton > button[kind="secondary"] {{
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background-color: #6200EE;
        color: white;
        border-radius: 20px;
        padding: 0.4rem 1rem;
        font-weight: 500;
    }}

    /* M3 Cards (Containers) */
    div[data-testid="stMetric"] {{
        background-color: #E8DEF8;
        border: 1px solid #D0BCFF;
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s;
    }}
    div[data-testid="stMetric"]:hover {{
        transform: translateY(-2px);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }}

    /* Primary Button */
    div.stButton > button {{
        background-color: #6200EE;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.6rem 1.6rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.4);
        transition: background-color 0.2s, box-shadow 0.2s;
    }}
    div.stButton > button:hover {{
        background-color: #3700B3;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
        color: white;
        border: 1px solid #FFFFFF;
    }}

    /* Headers */
    h1, h2, h3 {{
        color: #000000;
        font-weight: 600;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: #F3E5F5;
        border-right: 1px solid #E1E1E1;
    }}
    
    section[data-testid="stSidebar"] .stRadio > label {{
        font-weight: bold;
        color: #000000;
        font-size: 1.05rem;
    }}

</style>
""", unsafe_allow_html=True)

# Language Switcher at the top right
# We use a button with secondary kind to target it in CSS
st.button(t["lang_toggle"], on_click=swap_lang, type="secondary")

# Sidebar Navigation
st.sidebar.title(t["nav_title"])
page = st.sidebar.radio(
    t["select_page"],
    [t["tab_overall"], t["tab_dev"], t["tab_maint"], t["tab_landing"]],
    index=0
)

st.sidebar.markdown("---")

# Routing Logic
if page == t["tab_overall"]:
    overall.show()
elif page == t["tab_dev"]:
    development.show()
elif page == t["tab_maint"]:
    maintenance.show()
elif page == t["tab_landing"]:
    landing.show()
