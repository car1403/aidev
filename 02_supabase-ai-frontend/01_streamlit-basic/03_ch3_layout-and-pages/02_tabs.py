import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("Tabs 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

tab_summary, tab_detail, tab_memo = st.tabs(["요약", "상세", "메모"])  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.

with tab_summary:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.header("요약")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.write("핵심 내용을 짧게 보여주는 영역입니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

with tab_detail:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.header("상세")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    st.write("표, 차트, 긴 설명 같은 상세 정보를 배치할 수 있습니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

with tab_memo:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.header("메모")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    memo = st.text_area("메모를 입력하세요")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    st.write("입력한 메모:", memo)  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

