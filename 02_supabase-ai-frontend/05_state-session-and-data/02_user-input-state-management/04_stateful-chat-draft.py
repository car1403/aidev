import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("채팅 초안 상태")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if "draft" not in st.session_state:  # session_state에 값이 없을 때만 초기값을 만들어 화면 재실행에도 상태를 유지합니다.
    st.session_state.draft = ""  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

st.session_state.draft = st.text_area("질문 초안", value=st.session_state.draft)  # Streamlit이 재실행되어도 유지해야 하는 화면 상태를 session_state에 저장하거나 읽습니다.

if st.button("초안 확인"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.info(st.session_state.draft if st.session_state.draft else "초안이 비어 있습니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

