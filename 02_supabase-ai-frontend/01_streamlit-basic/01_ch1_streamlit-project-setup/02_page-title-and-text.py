import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.set_page_config(page_title="기본 텍스트 출력", page_icon="📘")  # Streamlit 페이지의 브라우저 제목과 레이아웃 같은 기본 설정을 지정합니다.

st.title("페이지 제목")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
st.header("섹션 제목")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
st.subheader("작은 섹션 제목")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
st.write("st.write는 문자열, 숫자, 리스트, 딕셔너리 등 다양한 값을 출력할 수 있습니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
st.markdown("**Markdown** 문법도 사용할 수 있습니다.")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
st.code("print('hello')", language="python")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
st.success("화면 출력 예제가 정상적으로 실행되었습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.

