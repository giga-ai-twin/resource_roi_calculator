import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from translations import TRANSLATIONS

def show():
    t = TRANSLATIONS[st.session_state.lang]
    
    st.title(t["app_title"])
    st.markdown("---")
    
    st.sidebar.header(t["config_header"])

    # 1. 開發規模與複雜度
    st.sidebar.subheader(t["dev_scale_header"])
    team_size = st.sidebar.slider(t["team_size"], 1, 20, 5)
    avg_salary = st.sidebar.number_input(t["avg_salary"], value=120000, step=5000, help=t["salary_help"])
    dev_cycle = st.sidebar.slider(t["dev_cycle"], 1, 24, 6)
    tooling_count = st.sidebar.number_input(t["tooling_count"], 0, 50, 5)
    data_heterogeneity = st.sidebar.select_slider(t["data_heterogeneity"], options=[1,2,3,4,5], value=3, help=t["data_help"])

    # 2. 運行與技術選型
    st.sidebar.subheader(t["ops_tech_header"])
    monthly_queries = st.sidebar.number_input(t["monthly_queries"], value=10000, step=1000)
    token_multiplier = st.sidebar.slider(t["token_multiplier"], 1.0, 10.0, 3.0, help=t["token_help"])
    
    deployment_mode = st.sidebar.selectbox(
        t["deployment_mode"],
        [t["deploy_a"], t["deploy_b"], t["deploy_c"]]
    )
    
    hardware_cost = 0
    if deployment_mode == t["deploy_c"]:
        hardware_cost = st.sidebar.number_input(t["hardware_cost"], value=1500000, step=100000)

    # 3. 現有業務基準
    st.sidebar.subheader(t["business_baseline_header"])
    manual_time = st.sidebar.number_input(t["manual_time"], value=0.5, step=0.1)
    hourly_rate = st.sidebar.number_input(t["hourly_rate"], value=600, step=50)

    # 4. 風險與敏感度
    st.sidebar.subheader(t["risk_sensitive_header"])
    compliance_high = st.sidebar.toggle(t["compliance_toggle"])

    if compliance_high:
        st.sidebar.info(t["compliance_info"])

    model_sel = st.sidebar.radio(t["model_selection"], [t["model_flagship"], t["model_light"]])

    # --- Calculations ---
    capex_base = team_size * avg_salary * dev_cycle
    if compliance_high:
        capex_base *= 1.2
        dev_cycle += 1
    
    total_capex = capex_base + hardware_cost
    
    # OpEx Calculation
    token_price = 0.0005 if model_sel == t["model_light"] else 0.005
    monthly_token_cost = monthly_queries * token_multiplier * 2000 * (token_price / 1000)
    monthly_infra_cost = 20000 if deployment_mode != t["deploy_c"] else 5000
    total_opex = monthly_token_cost + monthly_infra_cost
    
    # Benefits
    monthly_savings = monthly_queries * manual_time * hourly_rate
    net_monthly_benefit = monthly_savings - total_opex
    
    payback_period = total_capex / net_monthly_benefit if net_monthly_benefit > 0 else float('inf')

    # --- Main Dashboard ---
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(t["metrics_capex"], f"TWD {total_capex:,.0f}", help=t["metrics_capex_help"])
    with m2:
        st.metric(
            t["metrics_net_benefit"], 
            f"TWD {net_monthly_benefit:,.0f}", 
            delta=t["metrics_net_benefit_delta"].format(savings=monthly_savings, opex=total_opex)
        )
    with m3:
        if payback_period != float('inf'):
            st.metric(t["metrics_payback"], t["payback_months"].format(months=payback_period))
        else:
            st.metric(t["metrics_payback"], t["payback_failed"], delta_color="inverse")

    st.markdown("---")
    
    # ROI Chart
    months = np.arange(0, 37)
    cash_flow = [-total_capex] + [net_monthly_benefit] * 36
    cumulative_cash_flow = np.cumsum(cash_flow)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, 
        y=cumulative_cash_flow, 
        mode='lines+markers',
        name=t["chart_legend"],
        line=dict(color='#6200EE', width=3)
    ))
    
    fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text=t["chart_breakeven"])
    
    fig.update_layout(
        title=t["chart_title"],
        xaxis_title=t["chart_xaxis"],
        yaxis_title=t["chart_yaxis"],
        hovermode="x unified",
        template="plotly_white"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # --- Insights ---
    st.markdown(t["insight_header"])
    col_a, col_b = st.columns(2)
    
    with col_a:
        cost_ratio = (monthly_token_cost / total_opex) * 100 if total_opex > 0 else 0
        st.write(t["insight_model_cost"].format(ratio=cost_ratio))
        
    with col_b:
        if compliance_high:
            st.warning(t["insight_compliance_warn"])
        else:
            st.success(t["insight_compliance_success"])

    st.markdown("---")
    st.caption(t["footer_caption"])
