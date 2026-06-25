import os  # 운영체제 환경변수에서 API 주소나 비밀 키를 읽기 위해 os 모듈을 가져옵니다.
from pathlib import Path  # 현재 파일 위치를 기준으로 프로젝트 루트의 .env 경로를 계산하기 위해 사용합니다.

import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import pandas as pd  # 목록 데이터를 표와 차트로 다루기 위해 pandas를 pd라는 별칭으로 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.
from dotenv import load_dotenv  # .env 파일에 저장한 환경변수를 Python 실행 환경으로 불러오기 위해 가져옵니다.

PROJECT_ENV = Path(__file__).resolve().parents[3] / ".env"  # 04_supabase-ai-mini-project 최상위 .env 파일 경로입니다.
load_dotenv(PROJECT_ENV)  # 실행 위치가 frontend 폴더여도 04 과정의 .env를 읽도록 명시합니다.

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.

st.set_page_config(page_title="Supabase 학습 로그", layout="wide")  # Streamlit 페이지의 브라우저 제목과 레이아웃 같은 기본 설정을 지정합니다.
st.title("Supabase 학습 로그 대시보드")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
st.caption(f"API_BASE_URL: {API_BASE_URL}")  # 보조 설명이나 현재 설정값을 작은 글씨로 표시합니다.


def load_logs():  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    response = httpx.get(f"{API_BASE_URL}/api/logs", timeout=5.0)  # GET 요청의 응답을 response 변수에 저장해 상태 코드와 JSON 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json().get("items", [])  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


def create_log(learner_name, topic, minutes, memo):  # 요청 본문으로 받은 데이터를 새 항목으로 저장합니다.
    payload = {"learner_name": learner_name, "topic": topic, "minutes": minutes, "memo": memo}  # API 요청 본문으로 보낼 데이터를 딕셔너리 형태로 구성합니다.
    response = httpx.post(f"{API_BASE_URL}/api/logs", json=payload, timeout=5.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


def update_log(log_id, status):  # 경로 변수와 요청 본문을 사용해 기존 데이터를 수정합니다.
    response = httpx.patch(f"{API_BASE_URL}/api/logs/{log_id}", json={"status": status}, timeout=5.0)  # PATCH 요청의 응답을 response 변수에 저장해 수정 결과를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


with st.sidebar:  # 화면 왼쪽 사이드바 영역에 입력 컴포넌트를 배치합니다.
    st.header("로그 등록")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    learner_name = st.text_input("학습자", value="Student")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    topic = st.text_input("학습 주제", value="Supabase Mini Project")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    minutes = st.number_input("학습 시간(분)", min_value=1, max_value=600, value=30)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    memo = st.text_area("메모", value="Supabase 방식으로 학습 로그를 저장합니다.")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

    if st.button("등록"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
            create_log(learner_name, topic, minutes, memo)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
            st.success("등록했습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
        except httpx.HTTPError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
            st.error(f"등록 실패: {error}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

    st.divider()  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.header("상태 변경")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    log_id = st.number_input("로그 ID", min_value=1, value=1)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    status = st.selectbox("새 상태", ["created", "doing", "done"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

    if st.button("상태 저장"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
            update_log(log_id, status)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
            st.success("상태를 변경했습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
        except httpx.HTTPError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
            st.error(f"상태 변경 실패: {error}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

if st.button("백엔드 상태 확인"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
        response = httpx.get(f"{API_BASE_URL}/health", timeout=5.0)  # GET 요청의 응답을 response 변수에 저장해 상태 코드와 JSON 데이터를 확인합니다.
        st.json(response.json())  # 딕셔너리나 JSON 응답을 보기 쉬운 구조로 화면에 표시합니다.
    except httpx.HTTPError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
        st.error(f"상태 확인 실패: {error}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
    logs = load_logs()  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    df = pd.DataFrame(logs)  # 딕셔너리 데이터를 행과 열을 가진 DataFrame 표 구조로 변환합니다.
    if df.empty:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.info("등록된 학습 로그가 없습니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        col_count, col_minutes = st.columns(2)  # 메인 화면을 여러 열로 나누어 대시보드 요소를 배치합니다.
        col_count.metric("로그 수", len(df))  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
        col_minutes.metric("총 학습 시간", f"{int(df['minutes'].sum())}분")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
        st.dataframe(df, use_container_width=True)  # 표 형태의 데이터를 스크롤 가능한 DataFrame UI로 표시합니다.
except httpx.HTTPError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
    st.error(f"학습 로그를 불러올 수 없습니다: {error}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

