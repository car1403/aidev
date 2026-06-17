import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.

st.title("FastAPI 메시지 전송")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
message = st.text_input("메시지")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if st.button("전송"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    payload = {"name": name, "message": message}  # API 요청 본문으로 보낼 데이터를 딕셔너리 형태로 구성합니다.
    response = httpx.post(f"{API_BASE_URL}/api/message", json=payload, timeout=5.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.

    if response.status_code == 200:  # HTTP 응답 상태 코드를 확인해 성공과 실패 흐름을 나눕니다.
        result = response.json()  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
        st.success(result["reply"])  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        st.error(f"API 호출 실패: {response.status_code}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

