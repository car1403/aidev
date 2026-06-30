from pathlib import Path
import os

import httpx
import streamlit as st
from dotenv import load_dotenv


COURSE_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(COURSE_ROOT / ".env")


def api_base_url() -> str:
    return os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


def get_health():
    try:
        response = httpx.get(f"{api_base_url()}/health", timeout=5.0)
        response.raise_for_status()
        return response.json(), None
    except httpx.HTTPError as exc:
        return None, str(exc)


st.set_page_config(page_title="Mini Project Starter", layout="wide")
st.title("AI 서비스 로그 대시보드 Starter")
st.caption("이 파일은 최종 프로젝트 화면을 직접 구현하기 위한 최소 시작 코드입니다.")

with st.sidebar:
    st.subheader("연결 설정")
    st.code(f"API_BASE_URL={api_base_url()}")
    if st.button("백엔드 상태 확인"):
        data, error = get_health()
        if error:
            st.error(error)
        else:
            st.success("백엔드 연결 성공")
            st.json(data)

st.subheader("구현할 화면")

st.markdown(
    """
    - 실시간 로그 스트림 영역
    - 최근 로그 테이블
    - level/status별 차트
    - 로그 생성 또는 테스트 이벤트 입력 폼
    - AI 답변 품질 피드백 입력/조회 영역
    - 배포 전 점검 영역
    """
)

st.info("01_supabase-and-sse-practice/frontend/app.py를 참고해 필요한 기능을 직접 구현하세요.")
