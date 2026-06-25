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


st.set_page_config(page_title="Chatbot", layout="wide")
st.title("Chatbot")
st.caption("사용자 질문을 FastAPI 백엔드로 보내고 mock AI 응답을 화면에 표시합니다.")

with st.form("chat_form"):
    user_name = st.text_input("사용자 이름", value="student")
    message = st.text_area("질문", placeholder="예: 오늘 만든 Streamlit 화면은 어떻게 배포하나요?")
    submitted = st.form_submit_button("질문 보내기")

if submitted:
    if not user_name.strip() or not message.strip():
        st.warning("사용자 이름과 질문을 모두 입력하세요.")
    else:
        payload = {"user_name": user_name.strip(), "message": message.strip()}

        with st.spinner("백엔드에 질문을 보내는 중입니다..."):
            try:
                response = httpx.post(f"{api_base_url()}/api/chat", json=payload, timeout=10.0)
                response.raise_for_status()
                data = response.json()
            except Exception as exc:
                st.error("API 호출에 실패했습니다.")
                st.write(exc)
            else:
                st.success("응답을 받았습니다.")
                st.chat_message("user").write(data["user_message"])
                st.chat_message("assistant").write(data["assistant_message"])

                with st.expander("응답 데이터 확인"):
                    st.json(data)
