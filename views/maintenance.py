import streamlit as st
import pandas as pd
import numpy as np
from translations import TRANSLATIONS

def show():
    t = TRANSLATIONS[st.session_state.lang]
    st.title(t["maint_title"])
    st.markdown("---")
    
    st.info(t["maint_info"])

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(t["latency_metric"], "1.2s", "-0.1s")
    with col2:
        st.metric(t["hallucination_metric"], "2.3%", "-0.5%")
    with col3:
        st.metric(t["csat_metric"], "4.5/5.0", "+0.2")

    st.markdown(f"### {t['logs_header']}")
    
    # Mock Logs
    logs = [
        {t["time_col"]: "2024-02-20 10:00", t["level_col"]: "INFO", t["message_col"]: "System deployment successful"},
        {t["time_col"]: "2024-02-20 10:15", t["level_col"]: "WARNING", t["message_col"]: "High latency detected in vector DB"},
        {t["time_col"]: "2024-02-20 10:30", t["level_col"]: "ERROR", t["message_col"]: "Connection timeout - API Gateway"},
        {t["time_col"]: "2024-02-20 11:00", t["level_col"]: "INFO", t["message_col"]: "Cache cleared automatically"}
    ]
    
    st.table(pd.DataFrame(logs))
    
    st.subheader(t["maint_plan_header"])
    st.text_area(t["next_sprint_label"], t["next_sprint_placeholder"])
    
    if st.button(t["submit_maint_btn"]):
        st.success(t["submit_maint_success"])
