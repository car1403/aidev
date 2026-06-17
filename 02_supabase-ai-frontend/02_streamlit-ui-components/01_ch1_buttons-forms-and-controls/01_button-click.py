import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("버튼 클릭 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

clicked = st.button("인사말 보기")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if clicked:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.success("안녕하세요. 버튼이 클릭되었습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.info("버튼을 클릭하면 메시지가 표시됩니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

