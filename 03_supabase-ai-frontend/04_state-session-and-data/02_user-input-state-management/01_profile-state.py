import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("프로필 상태 관리")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if "profile" not in st.session_state:  # session_state에 값이 없을 때만 초기값을 만들어 화면 재실행에도 상태를 유지합니다.
    st.session_state.profile = {"name": "", "role": "AI 개발자"}  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

name = st.text_input("이름", value=st.session_state.profile["name"])  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.
role = st.selectbox("역할", ["AI 개발자", "백엔드 개발자", "프론트엔드 개발자"], index=0)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if st.button("프로필 저장"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.session_state.profile = {"name": name, "role": role}  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

st.json(st.session_state.profile)  # 딕셔너리나 JSON 응답을 보기 쉬운 구조로 화면에 표시합니다.

