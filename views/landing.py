import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from translations import TRANSLATIONS

def show():
    t = TRANSLATIONS[st.session_state.lang]
    st.title(t["landing_title"])
    st.markdown("---")
    
    st.info(t["landing_info"])

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(t["dept_adopted"], "3 / 10", "30%")
    with m2:
        st.metric(t["wau_metric"], "150", "+12")
    with m3:
        st.metric(t["success_rate_metric"], "88%", "+2.5%")
    with m4:
        st.metric(t["saved_hours_metric"], "320 hrs", "+45 hrs")

    st.markdown("---")
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader(t["adoption_trend_header"])
        # Mock Data
        dates = pd.date_range(start="2024-01-01", periods=12, freq="W")
        adoption_data = pd.DataFrame({
            t["date_col"]: dates,
            t["users_col"]: np.cumsum(np.random.randint(5, 20, 12))
        })
        
        fig = px.line(adoption_data, x=t["date_col"], y=t["users_col"], title=t["adoption_chart_title"])
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader(t["training_progress_header"])
        training_progress = pd.DataFrame({
            t["dept_col"]: ["Sales", "HR", "IT", "Marketing", "Finance"],
            t["progress_col"]: [100, 85, 90, 40, 10]
        })
        
        st.dataframe(
            training_progress,
            column_config={
                t["progress_col"]: st.column_config.ProgressColumn(
                    t["progress_col"],
                    help=t["progress_help"],
                    format="%d%%",
                    min_value=0,
                    max_value=100,
                ),
            },
            hide_index=True,
            use_container_width=True
        )

    st.markdown(f"### {t['feedback_header']}")
    st.success(t["feedback_sales"])
    st.info(t["feedback_hr"])
