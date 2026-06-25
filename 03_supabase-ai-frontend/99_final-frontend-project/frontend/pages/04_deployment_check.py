from __future__ import annotations

import os
from pathlib import Path

import httpx
import streamlit as st
from dotenv import load_dotenv


PROJECT_ENV = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(PROJECT_ENV)


def api_base_url() -> str:
    """백엔드 API 기본 주소를 환경변수 또는 Streamlit Secrets에서 가져옵니다."""
    try:
        secret_value = st.secrets.get("API_BASE_URL")
    except Exception:
        secret_value = None
    return (secret_value or os.getenv("API_BASE_URL", "http://127.0.0.1:8000")).rstrip("/")


st.set_page_config(page_title="Deployment Check", layout="wide")
st.title("Deployment Check")
st.caption("Render, Upstash, Streamlit Community Cloud 배포 전후 점검 화면입니다.")

st.subheader("현재 설정")
st.code(f"API_BASE_URL={api_base_url()}", language="text")

if st.button("배포된 백엔드 /health 확인"):
    try:
        response = httpx.get(f"{api_base_url()}/health", timeout=10.0)
        response.raise_for_status()
        st.success("백엔드 연결 성공")
        st.json(response.json())
    except Exception as exc:
        st.error("백엔드 연결 실패")
        st.write(exc)

st.subheader("배포 전 체크리스트")

checks = [
    "FastAPI 백엔드가 로컬에서 실행되는가?",
    "Streamlit 화면이 로컬에서 실행되는가?",
    "API_BASE_URL이 로컬에서는 http://127.0.0.1:8000 인가?",
    "GitHub 저장소에 .env 파일이 올라가지 않았는가?",
    "Render에 백엔드 환경변수를 등록했는가?",
    "Upstash REST URL과 Token을 Render 환경변수에 등록했는가?",
    "Streamlit Community Cloud Secrets에 배포된 Render URL을 등록했는가?",
    "배포된 Streamlit 앱에서 Render 백엔드 /health 호출이 성공하는가?",
]

for item in checks:
    st.checkbox(item)

st.warning("SUPABASE_SERVICE_ROLE_KEY, Upstash token, LLM API key는 프론트엔드 코드에 넣지 않습니다.")
