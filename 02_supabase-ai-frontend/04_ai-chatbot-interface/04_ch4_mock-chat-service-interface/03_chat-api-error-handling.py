import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.


def call_chat_api(message):  # 백엔드 API 호출 로직을 함수로 분리해 화면 코드에서 재사용합니다.
    response = httpx.post(f"{API_BASE_URL}/api/chat", json={"message": message}, timeout=3.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json().get("reply", "응답에 reply 항목이 없습니다.")  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


st.title("챗 API 오류 처리")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

prompt = st.chat_input("질문을 입력하세요")  # 채팅 입력창에서 사용자가 보낸 질문 문자열을 변수에 저장합니다.

if prompt:  # 사용자가 채팅 입력창에 질문을 입력했을 때만 메시지 처리 로직을 실행합니다.
    st.chat_message("user").write(prompt)  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.
    try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
        reply = call_chat_api(prompt)  # 백엔드 또는 AI 서비스가 만든 응답 문자열을 화면 출력용 변수에 저장합니다.
        st.chat_message("assistant").write(reply)  # role 값에 맞는 채팅 말풍선 영역에 메시지를 출력합니다.
    except httpx.ConnectError:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
        st.error("백엔드 서버에 연결할 수 없습니다.")  # 오류 상황을 사용자에게 명확히 보여줍니다.
    except httpx.TimeoutException:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
        st.error("AI 응답 시간이 초과되었습니다.")  # 오류 상황을 사용자에게 명확히 보여줍니다.
    except httpx.HTTPStatusError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
        st.error(f"API 오류가 발생했습니다: {error.response.status_code}")  # 오류 상황을 사용자에게 명확히 보여줍니다.


