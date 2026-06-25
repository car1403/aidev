import os  # 운영체제 환경변수에서 설정값을 읽기 위해 사용합니다.
from pathlib import Path  # 현재 파일 위치를 기준으로 .env 파일 경로를 계산하기 위해 사용합니다.

import pandas as pd  # 표 형태의 데이터를 만들고 Streamlit 화면에 표시하기 위해 사용합니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 사용합니다.
from dotenv import load_dotenv  # .env 파일의 값을 Python 환경변수로 불러오기 위해 사용합니다.


# 이 예제는 frontend 폴더 안에서 실행되지만,
# 환경변수 파일은 03_supabase-ai-mini-project 최상위에 둡니다.
PROJECT_ENV = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(PROJECT_ENV)

# APP_TITLE은 선택 환경변수입니다.
# .env에 값이 없으면 기본 제목을 사용합니다.
APP_TITLE = os.getenv("APP_TITLE", "03 Supabase Mini Project")

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(APP_TITLE)
st.caption("Streamlit 화면이 로컬 Python 환경에서 정상 실행되는지 확인하는 기본 예제입니다.")

st.info(f"환경변수 파일 기준: {PROJECT_ENV}")

df = pd.DataFrame(
    {
        "component": ["Streamlit", "FastAPI", "Supabase"],
        "role": ["사용자가 보는 화면", "요청 검증과 API 응답", "사용자/로그/피드백 데이터 저장"],
        "current_step": ["현재 실행 확인", "다음 단계에서 연결", "풀스택 단계에서 연결"],
    }
)

st.dataframe(df, use_container_width=True)

st.write(
    """
    이 단계에서는 아직 백엔드 API를 호출하지 않습니다.
    먼저 Streamlit 화면이 정상적으로 열리는지 확인하고,
    다음 `04_local-full-stack`에서 FastAPI와 Supabase를 함께 연결합니다.
    """
)
