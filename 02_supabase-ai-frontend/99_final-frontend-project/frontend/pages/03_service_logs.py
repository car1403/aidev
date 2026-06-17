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
    """백엔드 API 기본 주소를 가져옵니다."""
    try:
        secret_value = st.secrets.get("API_BASE_URL")
    except Exception:
        secret_value = None
    return (secret_value or os.getenv("API_BASE_URL", "http://127.0.0.1:8000")).rstrip("/")


st.set_page_config(page_title="Service Logs", layout="wide")
st.title("Service Logs")
st.caption("백엔드 API 호출 기록을 조회해 서비스 상태를 점검합니다.")

if st.button("서비스 로그 새로고침"):
    try:
        response = httpx.get(f"{api_base_url()}/api/logs", timeout=10.0)
        response.raise_for_status()
        items = response.json().get("items", [])
    except Exception as exc:
        st.error("서비스 로그 조회에 실패했습니다.")
        st.write(exc)
    else:
        if not items:
            st.info("아직 저장된 서비스 로그가 없습니다.")
        else:
            df = pd.DataFrame(items)
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df["event"].value_counts())

st.write(
    """
    이 화면은 03 미니 프로젝트에서 로그 대시보드로 확장됩니다.
    03에서는 이 로그를 Supabase 테이블에 저장하고, 오류 유형, 처리 시간,
    사용자 피드백까지 함께 시각화합니다.
    """
)
