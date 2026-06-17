import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("간단 설문 폼")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

with st.form("survey_form"):  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    topic = st.selectbox("가장 어려웠던 주제", ["실행", "입력", "레이아웃", "표", "차트"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    satisfaction = st.slider("수업 만족도", min_value=1, max_value=5, value=3)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    comment = st.text_area("추가 의견")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    submitted = st.form_submit_button("설문 제출")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if submitted:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.subheader("설문 결과")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.write(f"이름: {name if name else '미입력'}")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write(f"어려웠던 주제: {topic}")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write(f"만족도: {satisfaction}점")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    if comment:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.caption(comment)  # 보조 설명이나 현재 설정값을 작은 글씨로 표시합니다.

