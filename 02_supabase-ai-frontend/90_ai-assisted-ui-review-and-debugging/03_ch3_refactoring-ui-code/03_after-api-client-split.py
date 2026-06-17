import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.


def get_health_status():  # 저장된 데이터를 조회하는 요청을 처리합니다.
    response = httpx.get(f"{API_BASE_URL}/health", timeout=5.0)  # GET 요청의 응답을 response 변수에 저장해 상태 코드와 JSON 데이터를 확인합니다.
    response.raise_for_status()  # HTTP 상태 코드가 오류이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


st.title("API 호출 함수 분리")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if st.button("백엔드 상태 확인"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    try:  # 실패할 수 있는 코드를 실행하고, 오류가 나면 except 블록에서 처리합니다.
        st.json(get_health_status())  # 딕셔너리나 JSON 응답을 보기 쉬운 구조로 화면에 표시합니다.
    except httpx.HTTPError as error:  # 특정 예외가 발생했을 때 사용자에게 안내하거나 복구 동작을 수행합니다.
        st.error(f"API 호출 실패: {error}")  # 오류 상황을 사용자에게 명확히 보여줍니다.

