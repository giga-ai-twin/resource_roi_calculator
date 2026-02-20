import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from translations import TRANSLATIONS

def show():
    t = TRANSLATIONS[st.session_state.lang]
    st.title(t["dev_title"])
    st.markdown("---")
    
    st.info(t["dev_info"])

    st.subheader(t["tech_stack_header"])
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.multiselect(t["core_framework"], ["LangChain", "LlamaIndex", "Haystack"], ["LangChain"])
    with col2:
        st.multiselect(t["vector_db"], ["Pinecone", "Milvus", "Chroma", "Weaviate"], ["Pinecone"])
    with col3:
        st.multiselect(t["monitoring_eval"], ["LangSmith", "Weights & Biases", "Arize Phoenix"], ["LangSmith"])

    st.markdown("---")
    st.subheader(t["hr_config_header"])
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.slider(t["be_ai_eng"], 1, 10, 3)
    with c2:
        st.slider(t["fe_ui_eng"], 1, 10, 1)
    with c3:
        st.slider(t["domain_experts"], 1, 5, 1)
    with c4:
        st.slider(t["qa_testing"], 1, 5, 1)

    st.markdown("---")
    st.subheader(t["milestone_header"])
    
    # Mock Dataframe for Milestones
    df = pd.DataFrame([
        {t["task_col"]: t["task_analysis"], t["start_col"]: "2024-03-01", t["finish_col"]: "2024-03-15", t["resource_col"]: "PM/AI Eng"},
        {t["task_col"]: t["task_arch"], t["start_col"]: "2024-03-16", t["finish_col"]: "2024-03-31", t["resource_col"]: "AI Lead"},
        {t["task_col"]: t["task_rag"], t["start_col"]: "2024-04-01", t["finish_col"]: "2024-05-15", t["resource_col"]: "AI Eng"},
        {t["task_col"]: t["task_fe"], t["start_col"]: "2024-05-16", t["finish_col"]: "2024-06-15", t["resource_col"]: "FE Eng"},
        {t["task_col"]: t["task_qa"], t["start_col"]: "2024-06-16", t["finish_col"]: "2024-06-30", t["resource_col"]: "QA"},
    ])
    
    st.table(df)
    st.caption(t["dev_caption"])
