import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("폼 입력 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

with st.form("profile_form"):  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    role = st.selectbox("관심 분야", ["AI", "Backend", "Frontend", "Data"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    submitted = st.form_submit_button("제출")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if submitted:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    if name:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.success(f"{name}님의 관심 분야는 {role}입니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        st.error("이름을 입력하세요.")  # 오류 상황을 사용자에게 명확히 보여줍니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.info("값을 입력한 뒤 제출 버튼을 누르세요.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

