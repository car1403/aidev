import os  # 운영체제 환경변수에서 API 주소나 비밀 키를 읽기 위해 os 모듈을 가져옵니다.

import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = os.getenv("AI_CHAT_API_BASE_URL", "http://127.0.0.1:8000")  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.


def call_chat_api(message):  # 백엔드 API 호출 로직을 함수로 분리해 화면 코드에서 재사용합니다.
    url = f"{API_BASE_URL}/api/chat"  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    response = httpx.post(url, json={"message": message}, timeout=5.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()["reply"]  # 백엔드 JSON 응답에서 assistant 답변 문자열만 꺼내 호출한 곳으로 돌려줍니다.


st.title("챗 서비스 설정 분리")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
st.caption(f"API 주소: {API_BASE_URL}")  # 보조 설명이나 현재 설정값을 작은 글씨로 표시합니다.

prompt = st.chat_input("질문을 입력하세요")  # 채팅 입력창에서 사용자가 보낸 질문 문자열을 변수에 저장합니다.

if prompt:  # 사용자가 채팅 입력창에 질문을 입력했을 때만 메시지 처리 로직을 실행합니다.
    st.chat_message("user").write(prompt)  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.
    st.chat_message("assistant").write(call_chat_api(prompt))  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.


