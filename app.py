import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 設定頁面配置
st.set_page_config(
    page_title="Agentic RAG ROI 計算機",
    page_icon="📊",
    layout="wide"
)

# 標題
st.title("📊 企業級 Agentic RAG 系統開發規格與成本效益評估計算機")
st.markdown("---")

# 側邊欄：輸入參數
st.sidebar.header("⚙️ 參數設定 (Configuration)")

# 1. 開發規模與複雜度
st.sidebar.subheader("1. 開發規模與複雜度")
dev_team_size = st.sidebar.number_input("核心團隊人數 (人)", min_value=1, value=3, step=1)
dev_avg_salary = st.sidebar.number_input("開發人員平均月薪 (TWD)", min_value=40000, value=120000, step=5000, help="含勞健保與公司負擔成本")
dev_cycle = st.sidebar.number_input("預計開發週期 (月)", min_value=1, value=6, step=1)
tooling_count = st.sidebar.number_input("工具對接數量 (個)", min_value=0, value=3, step=1)
data_heterogeneity = st.sidebar.slider("資料異質度等級 (1-5)", 1, 5, 3, help="1: 單一來源, 5: 高度複雜/多模態")

# 2. 運行與技術選型
st.sidebar.subheader("2. 運行與技術選型")
monthly_queries = st.sidebar.number_input("預估每月請求量 (次)", min_value=100, value=5000, step=100)
token_multiplier = st.sidebar.slider("Agent 推理循環倍數", 1.0, 20.0, 10.0, help="Agent 反思與多次檢索產生的 Token 乘數")
deployment_mode = st.sidebar.selectbox("部署模式", ["A: 公有雲 (Vertex AI/OpenAI)", "B: 私有雲 (VPC)", "C: 地端 (GDC/Local)"])

# 額外硬體成本 (僅地端)
hardware_cost = 0
if "地端" in deployment_mode:
    hardware_cost = st.sidebar.number_input("一次性硬體採購費用 (TWD)", min_value=0, value=500000, step=10000)

# 3. 現有業務基準
st.sidebar.subheader("3. 現有業務基準")
manual_task_time = st.sidebar.number_input("人工處理單次任務時長 (小時)", min_value=0.1, value=0.5, step=0.1)
employee_hourly_rate = st.sidebar.number_input("相關員工平均時薪 (TWD)", min_value=183, value=500, step=50)

# 4. 風險與敏感度調整 (第四部分)
st.sidebar.markdown("---")
st.sidebar.subheader("4. 風險與敏感度調整")
compliance_enabled = st.sidebar.toggle("啟用高規格法規合規 (資料脫敏)", value=False)
model_type = st.sidebar.radio("模型選型", ["旗艦模型 (GPT-4o/Gemini 1.5 Pro)", "輕量模型 (Gemini 2.0 Flash/GPT-4o-mini)"])

# --- 運算邏輯 (Calculation Logic) ---

# 假設常數
TOOLING_COST_PER_UNIT = 50000  # 每個工具對接的假設開發成本
DATA_COMPLEXITY_COST_PER_LEVEL = 100000 # 每個異質度等級的假設成本
TOKENS_PER_QUERY_BASE = 1000 # 基礎問答 Token 數 (未乘倍數)
TOKEN_PRICE_FLAGSHIP = 5.0 / 1000000 * 32 # USD to TWD approx, per token. $5 per 1M tokens.
TOKEN_PRICE_LIGHT = 0.1 / 1000000 * 32    # $0.1 per 1M tokens.

# 1. 開發總成本 (Total CapEx)
# 基礎人力成本
base_dev_cost = dev_team_size * dev_avg_salary * dev_cycle
# 技術複雜度成本
tech_cost = (tooling_count * TOOLING_COST_PER_UNIT) + (data_heterogeneity * DATA_COMPLEXITY_COST_PER_LEVEL)

total_capex = base_dev_cost + tech_cost + hardware_cost

# 敏感度調整 - 法規
if compliance_enabled:
    st.sidebar.info("ℹ️ 已啟用合規模式：開發成本增加 20%，週期 +1 個月")
    total_capex *= 1.2
    # 週期變動不影響已計算的人力成本 (假設是額外外包或授權費)，或者也可以重新計算人力。
    # 這裡依照提示：「開發成本增加 20%，開發週期增加 1 個月」
    # 我們將 CapEx 直接加成，並在顯示時註記。

# 2. 每月運行成本 (Monthly OpEx)
avg_tokens_per_query = TOKENS_PER_QUERY_BASE * token_multiplier
price_per_token = TOKEN_PRICE_LIGHT if "輕量" in model_type else TOKEN_PRICE_FLAGSHIP

# 雲端/地端 基礎設施維護費假設
infra_base_cost = 0
if "公有雲" in deployment_mode:
    infra_base_cost = 5000 
elif "私有雲" in deployment_mode:
    infra_base_cost = 20000
else: # 地端
    infra_base_cost = 10000 # 電費維護等

model_api_cost = monthly_queries * avg_tokens_per_query * price_per_token
monthly_opex = model_api_cost + infra_base_cost

# 3. 效益產出 (Value Realization)
# 節省成本 = 請求量 * (人工時間 * 時薪) * (由 Agent 取代的比例)
# 假設 Agent 完全取代該任務
monthly_savings = monthly_queries * manual_task_time * employee_hourly_rate
net_monthly_benefit = monthly_savings - monthly_opex

# --- 輸出儀表板 (Dashboard) ---

# 顯示關鍵指標
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("總開發成本 (CapEx)", f"NT$ {total_capex:,.0f}", help="首年建置成本")

with c2:
    st.metric("每月淨效益 (Net Value)", f"NT$ {net_monthly_benefit:,.0f}", delta=f"節省: {monthly_savings:,.0f} | 成本: {monthly_opex:,.0f}")

# 計算回收期 (Payback Period)
if net_monthly_benefit > 0:
    payback_months = total_capex / net_monthly_benefit
    payback_text = f"{payback_months:.1f} 個月"
else:
    payback_terms = "無法回收 (效益 < 成本)"
    payback_months = 999

with c3:
    st.metric("預計回收期 (Payback Period)", payback_text)

# --- 圖表分析 ---

st.subheader("📉 成本回收與效益預測 (36 個月)")

# 產生數據與圖表
months = list(range(37))
cumulative_cash_flow = [-total_capex] # 第 0 個月只有支出
current_balance = -total_capex

for m in range(1, 37):
    current_balance += net_monthly_benefit
    cumulative_cash_flow.append(current_balance)

# 繪製 Line Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y=cumulative_cash_flow, mode='lines+markers', name='累計現金流 (Cumulative Cash Flow)'))

# 標示損益兩平點 (若在範圍內)
if 0 < payback_months < 36:
    fig.add_shape(type="line",
        x0=payback_months, y0=min(cumulative_cash_flow), x1=payback_months, y1=max(cumulative_cash_flow),
        line=dict(color="Green", width=2, dash="dashdot")
    )
    fig.add_annotation(x=payback_months, y=0, text="損益兩平點", showarrow=True, arrowhead=1)

# 0 軸線
fig.add_hline(y=0, line_dash="dash", line_color="gray")

fig.update_layout(
    xaxis_title="月份 (Month)",
    yaxis_title="累計金額 (TWD)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# 額外分析：法規與模型影響提示
st.markdown("### 💡 分析洞察")
col_a, col_b = st.columns(2)

with col_a:
    st.info(f"**模型與運算成本佔比**：\n目前 API/運算成本佔每月 OpEx 的 **{(model_api_cost/monthly_opex*100):.1f}%**。若需降低運行成本，可考慮切換至輕量模型或優化 Token 用量。")

with col_b:
    if compliance_enabled:
        st.warning("**合規成本影響**：\n已啟用資料脫敏與合規要求，導致 CapEx 上升 20%。請評估此合規性是否為絕對必要，或可分階段實施。")
    else:
        st.success("**合規成本影響**：\n目前未啟用高規格合規要求。若未來導入 ISO/GDPR 等標準，請預留 20% 額外預算緩衝。")

st.markdown("---")
st.caption("此模型僅供估算參考，實際成本請依據 detailed design 與 vendor quotation 為準。")
