import json  # metadata 입력값을 JSON 딕셔너리로 변환하기 위해 사용합니다.
import os  # 운영체제 환경변수에서 API 주소를 읽기 위해 사용합니다.
from pathlib import Path  # 현재 파일 위치를 기준으로 03 과정 최상위 .env 경로를 계산하기 위해 사용합니다.

import httpx  # FastAPI 백엔드 API에 HTTP 요청을 보내기 위해 사용합니다.
import pandas as pd  # 로그 목록을 표와 집계 데이터로 다루기 위해 사용합니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 사용합니다.
from dotenv import load_dotenv  # .env 파일에 저장한 환경변수를 Python 실행 환경으로 불러오기 위해 사용합니다.

COURSE_ROOT = Path(__file__).resolve().parents[3]  # frontend/app.py에서 03_supabase-ai-mini-project 최상위 폴더로 올라갑니다.
load_dotenv(COURSE_ROOT / ".env")  # 하위 팀 폴더가 아니라 03 과정 최상위 .env를 읽습니다.

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")  # Streamlit이 호출할 FastAPI 서버 주소입니다.

st.set_page_config(page_title="Service Log Dashboard", layout="wide")  # 페이지 제목과 화면 폭을 설정합니다.
st.title("실시간 로그 대시보드 인터페이스")  # 프로젝트의 핵심 화면 제목을 표시합니다.
st.caption(f"API_BASE_URL: {API_BASE_URL}")  # 현재 Streamlit이 호출하는 백엔드 주소를 화면에 표시합니다.


def load_logs() -> list[dict]:  # FastAPI에서 서비스 로그 목록을 가져오는 함수입니다.
    response = httpx.get(f"{API_BASE_URL}/api/logs", timeout=5.0)  # 로그 목록 조회 API를 호출합니다.
    response.raise_for_status()  # HTTP 오류 상태 코드가 오면 예외를 발생시킵니다.
    return response.json().get("items", [])  # 응답 JSON에서 items 목록만 꺼내 반환합니다.


def create_log(action: str, status: str, metadata: dict) -> dict:  # 새 서비스 로그를 저장하는 함수입니다.
    payload = {"action": action, "status": status, "metadata": metadata}  # API 요청 본문을 구성합니다.
    response = httpx.post(f"{API_BASE_URL}/api/logs", json=payload, timeout=5.0)  # 로그 생성 API를 호출합니다.
    response.raise_for_status()  # HTTP 오류 상태 코드가 오면 예외를 발생시킵니다.
    return response.json()  # 저장 결과를 반환합니다.


def update_log(log_id: str, status: str) -> dict:  # 기존 서비스 로그의 상태를 수정하는 함수입니다.
    response = httpx.patch(f"{API_BASE_URL}/api/logs/{log_id}", json={"status": status}, timeout=5.0)  # 로그 상태 수정 API를 호출합니다.
    response.raise_for_status()  # HTTP 오류 상태 코드가 오면 예외를 발생시킵니다.
    return response.json()  # 수정 결과를 반환합니다.


def parse_metadata(raw_text: str) -> dict:  # 화면에 입력한 JSON 문자열을 Python 딕셔너리로 바꾸는 함수입니다.
    if not raw_text.strip():  # 아무것도 입력하지 않으면 빈 딕셔너리로 처리합니다.
        return {}
    parsed = json.loads(raw_text)  # 문자열을 JSON으로 해석합니다.
    if not isinstance(parsed, dict):  # metadata는 객체 형태여야 하므로 리스트나 문자열이면 오류로 처리합니다.
        raise ValueError("metadata는 JSON object 형식이어야 합니다.")
    return parsed


with st.sidebar:  # 화면 왼쪽 사이드바 영역입니다.
    st.header("로그 등록")  # 새 로그 입력 영역 제목입니다.
    action = st.text_input("작업 이름", value="chat_request")  # 어떤 작업이 실행되었는지 입력합니다.
    status = st.selectbox("상태", ["success", "fail", "warning"])  # 로그 상태를 선택합니다.
    metadata_text = st.text_area(  # 추가 정보를 JSON 문자열로 입력합니다.
        "metadata(JSON)",
        value='{"model": "gemini-2.5-flash-lite", "source": "streamlit"}',
        height=120,
    )

    if st.button("로그 저장"):  # 버튼을 누르면 로그 저장 API를 호출합니다.
        try:
            metadata = parse_metadata(metadata_text)  # 사용자가 입력한 metadata를 딕셔너리로 변환합니다.
            create_log(action, status, metadata)  # FastAPI를 통해 Supabase service_logs 테이블에 저장합니다.
            st.success("서비스 로그를 저장했습니다.")  # 성공 메시지를 표시합니다.
        except (ValueError, json.JSONDecodeError) as error:
            st.error(f"metadata 형식을 확인해 주세요: {error}")  # JSON 입력 오류를 안내합니다.
        except httpx.HTTPError as error:
            st.error(f"로그 저장 실패: {error}")  # API 호출 오류를 안내합니다.

    st.divider()  # 입력 영역과 상태 수정 영역을 나눕니다.
    st.header("상태 수정")  # 기존 로그 상태 수정 영역 제목입니다.
    log_id = st.text_input("로그 ID")  # Supabase의 uuid id를 입력합니다.
    next_status = st.selectbox("변경할 상태", ["success", "fail", "warning"], key="next_status")  # 새 상태를 선택합니다.

    if st.button("상태 변경"):  # 버튼을 누르면 상태 수정 API를 호출합니다.
        if not log_id.strip():
            st.warning("수정할 로그 ID를 입력해 주세요.")  # ID가 없으면 안내 메시지를 표시합니다.
        else:
            try:
                update_log(log_id.strip(), next_status)  # FastAPI를 통해 Supabase 로그 상태를 수정합니다.
                st.success("로그 상태를 변경했습니다.")  # 성공 메시지를 표시합니다.
            except httpx.HTTPError as error:
                st.error(f"상태 변경 실패: {error}")  # API 호출 오류를 안내합니다.

if st.button("백엔드 상태 확인"):  # 백엔드와 Supabase 연결 상태를 확인하는 버튼입니다.
    try:
        response = httpx.get(f"{API_BASE_URL}/health", timeout=5.0)  # health check API를 호출합니다.
        response.raise_for_status()  # HTTP 오류 상태 코드가 오면 예외를 발생시킵니다.
        st.json(response.json())  # 응답 JSON을 화면에 표시합니다.
    except httpx.HTTPError as error:
        st.error(f"상태 확인 실패: {error}")  # API 호출 오류를 안내합니다.

try:
    logs = load_logs()  # FastAPI에서 서비스 로그 목록을 가져옵니다.
    df = pd.DataFrame(logs)  # 로그 목록을 표 형태로 다루기 위해 DataFrame으로 변환합니다.

    if df.empty:
        st.info("등록된 서비스 로그가 없습니다.")  # 데이터가 없을 때 안내 메시지를 표시합니다.
    else:
        col_total, col_success, col_fail = st.columns(3)  # 주요 지표를 3개 열로 배치합니다.
        col_total.metric("전체 로그 수", len(df))  # 전체 로그 개수를 표시합니다.
        col_success.metric("성공 로그", int((df["status"] == "success").sum()))  # success 상태 로그 수를 표시합니다.
        col_fail.metric("실패 로그", int((df["status"] == "fail").sum()))  # fail 상태 로그 수를 표시합니다.

        st.subheader("서비스 로그 목록")  # 로그 표 제목입니다.
        st.dataframe(df, use_container_width=True)  # 로그 데이터를 표로 표시합니다.

        if "status" in df.columns:
            st.subheader("상태별 로그 수")  # 간단한 차트 제목입니다.
            st.bar_chart(df["status"].value_counts())  # 상태별 로그 개수를 막대 차트로 표시합니다.

except httpx.HTTPError as error:
    st.error(f"서비스 로그를 불러올 수 없습니다: {error}")  # API 호출 오류를 안내합니다.
