import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.


def call_chat_api(message):  # 백엔드 API 호출 로직을 함수로 분리해 화면 코드에서 재사용합니다.
    response = httpx.post(f"{API_BASE_URL}/api/chat", json={"message": message}, timeout=5.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()["reply"]  # 백엔드 JSON 응답에서 assistant 답변 문자열만 꺼내 호출한 곳으로 돌려줍니다.


st.title("백엔드 챗 API 클라이언트")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

prompt = st.chat_input("질문을 입력하세요")  # 채팅 입력창에서 사용자가 보낸 질문 문자열을 변수에 저장합니다.

if prompt:  # 사용자가 채팅 입력창에 질문을 입력했을 때만 메시지 처리 로직을 실행합니다.
    st.chat_message("user").write(prompt)  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.
    with st.spinner("AI 응답을 기다리는 중입니다..."):  # API 응답을 기다리는 동안 로딩 메시지를 보여주는 컨텍스트를 엽니다.
        reply = call_chat_api(prompt)  # 백엔드 또는 AI 서비스가 만든 응답 문자열을 화면 출력용 변수에 저장합니다.
    st.chat_message("assistant").write(reply)  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.


