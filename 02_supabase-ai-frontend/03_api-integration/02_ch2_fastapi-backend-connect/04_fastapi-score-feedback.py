import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.

st.title("점수 피드백 API 연동")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
score = st.slider("점수", min_value=0, max_value=100, value=70)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if st.button("피드백 요청"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    payload = {"name": name, "score": score}  # API 요청 본문으로 보낼 데이터를 딕셔너리 형태로 구성합니다.
    response = httpx.post(f"{API_BASE_URL}/api/score-feedback", json=payload, timeout=5.0)  # POST 요청의 응답을 response 변수에 저장해 성공 여부와 결과 데이터를 확인합니다.
    result = response.json()  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

    st.success(result["feedback"])  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    st.json(result)  # 딕셔너리나 JSON 응답을 보기 쉬운 구조로 화면에 표시합니다.

