import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("필터 상태 관리")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if "filters" not in st.session_state:  # session_state에 값이 없을 때만 초기값을 만들어 화면 재실행에도 상태를 유지합니다.
    st.session_state.filters = {"course": "전체", "min_score": 0}  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

course = st.selectbox("과정", ["전체", "Python", "Streamlit", "FastAPI"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
min_score = st.slider("최소 점수", 0, 100, st.session_state.filters["min_score"])  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

if st.button("필터 적용"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.session_state.filters = {"course": course, "min_score": min_score}  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

st.write("현재 필터:", st.session_state.filters)  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

