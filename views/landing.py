import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def show():
    st.title("🚀 導入與落地 (Implementation & Landing)")
    st.markdown("---")
    
    st.info("此頁面追蹤 **業務導入狀況** 與 **實際影響力評估**。")

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("已導入部門", "3 / 10", "30%")
    with m2:
        st.metric("活躍用戶數 (WAU)", "150", "+12")
    with m3:
        st.metric("任務成功率", "88%", "+2.5%")
    with m4:
        st.metric("預估節省工時 (此月)", "320 hrs", "+45 hrs")

    st.markdown("---")
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("📈 用戶採用趨勢 (Adoption Trend)")
        # Mock Data
        dates = pd.date_range(start="2024-01-01", periods=12, freq="W")
        adoption_data = pd.DataFrame({
            "Date": dates,
            "Users": np.cumsum(np.random.randint(5, 20, 12))
        })
        
        fig = px.line(adoption_data, x="Date", y="Users", title="每週累計用戶數")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("🎓 教育訓練進度")
        training_progress = pd.DataFrame({
            "Department": ["Sales", "HR", "IT", "Marketing", "Finance"],
            "Progress": [100, 85, 90, 40, 10]
        })
        
        st.dataframe(
            training_progress,
            column_config={
                "Progress": st.column_config.ProgressColumn(
                    "完成度",
                    help="各部門受訓比例",
                    format="%d%%",
                    min_value=0,
                    max_value=100,
                ),
            },
            hide_index=True,
            use_container_width=True
        )

    st.markdown("### 📢 用戶反饋摘要")
    st.success("Sales Team: 'RAG 幫助我們快速找到合約條款，節省了大量時間！'")
    st.info("HR Team: '希望可以增加更多內部規章的知識庫。'")
