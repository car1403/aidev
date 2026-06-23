import pandas as pd  # 목록 데이터를 표와 차트로 다루기 위해 pandas를 pd라는 별칭으로 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("디버깅 예제: import 확인")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

df = pd.DataFrame({"course": ["Streamlit", "FastAPI"], "score": [90, 85]})  # 딕셔너리 데이터를 행과 열을 가진 DataFrame 표 구조로 변환합니다.
st.dataframe(df)  # 표 형태의 데이터를 스크롤 가능한 DataFrame UI로 표시합니다.

