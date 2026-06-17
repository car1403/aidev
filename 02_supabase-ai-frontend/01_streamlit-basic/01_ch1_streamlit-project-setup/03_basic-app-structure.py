import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.


def render_header():  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    st.title("기본 앱 구조")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
    st.write("함수를 사용해 화면 영역을 나누는 간단한 예제입니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.


def render_content():  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    st.header("본문 영역")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.write("실제 앱에서는 이 영역에 입력, 결과, 표, 차트 등을 배치합니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.


def render_footer():  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    st.divider()  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.caption("01_streamlit-basic / ch1")  # 보조 설명이나 현재 설정값을 작은 글씨로 표시합니다.


render_header()  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
render_content()  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
render_footer()  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.

