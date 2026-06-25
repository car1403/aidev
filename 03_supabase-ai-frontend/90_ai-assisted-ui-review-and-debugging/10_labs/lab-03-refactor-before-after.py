import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.


def make_message(name, level):  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    if not name:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        return "이름을 입력하세요."  # 함수 실행 결과를 호출한 위치로 돌려줍니다.
    return f"{name}님의 현재 수준은 {level}입니다."  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


st.title("리팩토링 실습 결과")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
level = st.selectbox("수준", ["입문", "기초", "중급"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if st.button("메시지 보기"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.write(make_message(name, level))  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

