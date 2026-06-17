"""Docker Compose frontend Streamlit 화면입니다."""

import httpx
import streamlit as st


st.set_page_config(page_title="AI Service Frontend", layout="wide")
st.title("AI Service Frontend")

backend_url = "http://backend:8000/agent/status"

if st.button("Backend 상태 확인"):
    try:
        response = httpx.get(backend_url, timeout=5)
        st.json(response.json())
    except httpx.HTTPError as exc:
        st.error(f"backend 연결 실패: {exc}")
