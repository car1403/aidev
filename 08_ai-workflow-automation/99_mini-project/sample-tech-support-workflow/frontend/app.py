"""Streamlit frontend for the sample tech support workflow."""

import os

import httpx
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8900")

st.set_page_config(page_title="Tech Support Workflow", layout="wide")
st.title("Tech Support AI Workflow")

with st.sidebar:
    st.header("Service")
    st.write(API_BASE_URL)
    if st.button("Health Check"):
        response = httpx.get(f"{API_BASE_URL}/health", timeout=5)
        st.json(response.json())

left, right = st.columns([1, 1])

with left:
    st.subheader("Ticket Input")
    customer_name = st.text_input("Customer", "Jean")
    customer_tier = st.selectbox("Tier", ["basic", "premium"], index=1)
    title = st.text_input("Title", "AI 서비스 응답 지연")
    message = st.text_area(
        "Message",
        "프리미엄 고객입니다. AI 서비스 응답이 너무 느리고 장애가 의심됩니다. 빠르게 확인해 주세요.",
        height=160,
    )

    if st.button("Run Workflow", type="primary"):
        payload = {
            "customer_name": customer_name,
            "customer_tier": customer_tier,
            "title": title,
            "message": message,
        }
        response = httpx.post(f"{API_BASE_URL}/analyze", json=payload, timeout=10)
        response.raise_for_status()
        st.session_state["analysis"] = response.json()

with right:
    st.subheader("Analysis Result")
    if "analysis" in st.session_state:
        analysis = st.session_state["analysis"]
        st.metric("Urgency", analysis["urgency"])
        st.metric("Next Action", analysis["next_action"])
        st.json(analysis)
    else:
        st.info("Run Workflow를 눌러 결과를 확인하세요.")

st.subheader("Ops Metrics")
try:
    metrics = httpx.get(f"{API_BASE_URL}/metrics", timeout=5).json()
    st.json(metrics)
except httpx.HTTPError:
    st.warning("Backend가 실행 중인지 확인하세요.")

st.subheader("Recent Events")
try:
    events = httpx.get(f"{API_BASE_URL}/events", timeout=5).json()
    st.dataframe(events, use_container_width=True)
except httpx.HTTPError:
    st.warning("이벤트를 불러올 수 없습니다.")
