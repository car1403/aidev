from __future__ import annotations

import os
from pathlib import Path

import httpx
import pandas as pd
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


st.set_page_config(page_title="Chat History", layout="wide")
st.title("Chat History")
st.caption("백엔드에 저장된 대화 이력을 조회합니다.")

if st.button("대화 이력 새로고침"):
    try:
        response = httpx.get(f"{api_base_url()}/api/chats", timeout=10.0)
        response.raise_for_status()
        items = response.json().get("items", [])
    except Exception as exc:
        st.error("대화 이력 조회에 실패했습니다.")
        st.write(exc)
    else:
        if not items:
            st.info("아직 저장된 대화가 없습니다.")
        else:
            df = pd.DataFrame(items)
            st.dataframe(df, use_container_width=True)

            st.subheader("간단 지표")
            col1, col2 = st.columns(2)
            col1.metric("대화 수", len(df))
            col2.metric("평균 응답 시간(ms)", round(df["elapsed_ms"].mean(), 2))

st.info("대화가 보이지 않으면 Chatbot 화면에서 질문을 먼저 보내 보세요.")
