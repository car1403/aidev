"""서비스 운영 상태를 확인하는 Streamlit monitor 화면입니다."""

import httpx
import streamlit as st


st.set_page_config(page_title="Ops Monitor", layout="wide")
st.title("Ops Monitor")

health_url = "http://backend:8000/health"

try:
    response = httpx.get(health_url, timeout=5)
    st.success("backend health check 성공")
    st.json(response.json())
except httpx.HTTPError as exc:
    st.error(f"backend health check 실패: {exc}")
