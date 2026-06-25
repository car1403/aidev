from __future__ import annotations

import os
from pathlib import Path

import httpx
import streamlit as st
from dotenv import load_dotenv


PROJECT_ENV = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(PROJECT_ENV)


def get_api_base_url() -> str:
    """환경변수 또는 Streamlit Secrets에서 백엔드 API 주소를 읽습니다."""
    try:
        secret_value = st.secrets.get("API_BASE_URL")
    except Exception:
        secret_value = None
    return (secret_value or os.getenv("API_BASE_URL", "http://127.0.0.1:8000")).rstrip("/")


def check_backend(api_base_url: str) -> tuple[bool, dict | str]:
    """백엔드 `/health` API를 호출해 연결 상태를 확인합니다."""
    try:
        response = httpx.get(f"{api_base_url}/health", timeout=5.0)
        response.raise_for_status()
        return True, response.json()
    except Exception as exc:
        return False, str(exc)


st.set_page_config(page_title="Final Frontend Project", layout="wide")

st.title("개인화 AI 챗봇 서비스 최종 예제")
st.caption("Streamlit 프론트엔드가 FastAPI 백엔드를 호출하는 02 과정 최종 실습입니다.")

api_base_url = get_api_base_url()
st.info(f"현재 API_BASE_URL: {api_base_url}")

ok, result = check_backend(api_base_url)

if ok:
    st.success("백엔드 연결 성공")
    st.json(result)
else:
    st.error("백엔드 연결 실패")
    st.write(result)
    st.warning("FastAPI 백엔드가 실행 중인지, `.env` 또는 Streamlit Secrets의 API_BASE_URL이 맞는지 확인하세요.")

st.subheader("실습 흐름")
st.write(
    """
    1. 왼쪽 메뉴에서 Chatbot 화면을 엽니다.
    2. 사용자 이름과 질문을 입력합니다.
    3. Chat History에서 저장된 대화 이력을 확인합니다.
    4. Service Logs에서 API 호출 로그를 확인합니다.
    5. Deployment Check에서 배포 전 점검 항목을 확인합니다.
    """
)

st.subheader("03 미니 프로젝트로 확장하기")
st.write(
    """
    이 예제는 03 과정에서 Supabase 테이블, SSE 스트리밍, 피드백 데이터,
    API 설계 문서, 화면 설계서, 데이터베이스 설계서로 확장됩니다.
    02에서는 프론트엔드와 백엔드 연결 흐름을 익히고,
    03에서는 팀 프로젝트 산출물 형태로 구조를 완성합니다.
    """
)
