import pandas as pd  # 목록 데이터를 표와 차트로 다루기 위해 pandas를 pd라는 별칭으로 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("CSV 업로드 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if uploaded_file is not None:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    df = pd.read_csv(uploaded_file)  # 업로드된 CSV 파일을 pandas DataFrame으로 읽어옵니다.
    st.success("CSV 파일을 읽었습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    st.dataframe(df)  # 표 형태의 데이터를 스크롤 가능한 DataFrame UI로 표시합니다.
    st.write("행 개수:", len(df))  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
    st.write("컬럼 목록:", list(df.columns))  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.info("CSV 파일을 선택하면 표가 표시됩니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

