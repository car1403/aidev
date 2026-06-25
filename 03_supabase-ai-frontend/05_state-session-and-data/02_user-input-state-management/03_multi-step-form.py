import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("단계형 입력 상태")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if "step" not in st.session_state:  # session_state에 값이 없을 때만 초기값을 만들어 화면 재실행에도 상태를 유지합니다.
    st.session_state.step = 1  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

if st.session_state.step == 1:  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.
    st.write("1단계: 이름 입력")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.session_state.name = st.text_input("이름", value=st.session_state.get("name", ""))  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.
    if st.button("다음"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.session_state.step = 2  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.
        st.rerun()  # session_state 변경 사항을 즉시 반영하기 위해 Streamlit 스크립트를 다시 실행합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.write("2단계: 관심 분야 입력")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.session_state.topic = st.selectbox("관심 분야", ["Streamlit", "FastAPI", "DB"] )  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.
    st.write("이름:", st.session_state.get("name", ""))  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write("관심 분야:", st.session_state.topic)  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

