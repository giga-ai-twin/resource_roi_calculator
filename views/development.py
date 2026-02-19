import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("💻 開發階段評估 (Development Phase)")
    st.markdown("---")
    
    st.info("此頁面專注於 **技術開發細節** 與 **工程資源分配**。")

    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("🛠️ 技術棧選型")
        st.multiselect("核心框架", ["LangChain", "LlamaIndex", "Haystack", "Custom (Native Python)"], default=["LangChain"])
        st.multiselect("向量資料庫", ["Pinecone", "Milvus", "Weaviate", "Qdrant", "Chroma"], default=["Qdrant"])
        st.multiselect("監控與評估", ["LangSmith", "Arize Phoenix", "DeepEval", "Ragas"], default=["LangSmith"])

    with c2:
        st.subheader("👥 人力資源配置")
        st.slider("Backend / AI Engineers", 1, 10, 3)
        st.slider("Frontend / UI Engineers", 0, 5, 1)
        st.slider("Domain Experts (SME)", 0, 5, 1)
        st.slider("QA / Testing", 0, 3, 1)

    st.markdown("---")
    st.subheader("📅 開發里程碑預估")
    
    # Simple Gantt Chart Data
    df = pd.DataFrame([
        dict(Task="需求分析 & POC", Start='2024-01-01', Finish='2024-02-01', Resource='PM & Lead'),
        dict(Task="系統架構設計", Start='2024-02-01', Finish='2024-03-01', Resource='Architect'),
        dict(Task="核心 RAG 開發", Start='2024-03-01', Finish='2024-05-01', Resource='AI Team'),
        dict(Task="前端與整合", Start='2024-04-15', Finish='2024-06-01', Resource='Full Stack'),
        dict(Task="測試與優化", Start='2024-06-01', Finish='2024-07-01', Resource='QA & Team')
    ])
    
    # We can visualize this table or use a simple timeline
    st.dataframe(df, use_container_width=True)
    
    st.caption("以上甘特圖數據僅為範例，實際需依據 Jira/Asana 排程為準。")
