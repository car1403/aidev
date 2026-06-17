import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.set_page_config(page_title="기본 대시보드", layout="wide")  # Streamlit 페이지의 브라우저 제목과 레이아웃 같은 기본 설정을 지정합니다.

st.title("기본 대시보드 페이지")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

with st.sidebar:  # 화면 왼쪽 사이드바 영역에 입력 컴포넌트를 배치합니다.
    st.header("필터")  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    course = st.selectbox("과정", ["Python Basic", "Streamlit Basic", "FastAPI Backend"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    progress = st.slider("진도율", min_value=0, max_value=100, value=60)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

summary_col, status_col, memo_col = st.columns(3)  # 메인 화면을 여러 열로 나누어 대시보드 요소를 배치합니다.

with summary_col:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.metric("선택 과정", course)  # 핵심 숫자나 상태값을 대시보드 지표 형태로 표시합니다.

with status_col:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.metric("진도율", f"{progress}%")  # 핵심 숫자나 상태값을 대시보드 지표 형태로 표시합니다.

with memo_col:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    if progress >= 80:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.success("마무리 점검 단계입니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    elif progress >= 40:  # 앞 조건이 False일 때 추가 조건을 검사합니다.
        st.info("꾸준히 진행 중입니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        st.warning("기초 예제부터 다시 확인하세요.")  # 주의가 필요한 상황을 경고 메시지로 표시합니다.

tab_overview, tab_plan = st.tabs(["개요", "학습 계획"])  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.

with tab_overview:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.write(f"현재 선택한 과정은 {course}입니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.progress(progress)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.

with tab_plan:  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
    st.write("1. 예제 실행")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write("2. 입력값 변경")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write("3. 화면 구성 수정")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

