import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("텍스트 입력 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

name = st.text_input("이름을 입력하세요")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if name:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.write(f"안녕하세요, {name}님!")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.warning("이름을 입력하면 인사말이 표시됩니다.")  # 주의가 필요한 상황을 경고 메시지로 표시합니다.

