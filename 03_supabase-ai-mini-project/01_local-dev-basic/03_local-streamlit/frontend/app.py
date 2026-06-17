import os  # 운영체제 환경변수에서 API 주소나 비밀 키를 읽기 위해 os 모듈을 가져옵니다.

import pandas as pd  # 목록 데이터를 표와 차트로 다루기 위해 pandas를 pd라는 별칭으로 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

APP_TITLE = os.getenv("APP_TITLE", "Streamlit App")  # 환경변수 값을 읽어 설정값으로 저장합니다. 코드에 비밀 값을 직접 쓰지 않기 위한 방식입니다.

st.set_page_config(page_title=APP_TITLE)  # Streamlit 페이지의 브라우저 제목과 레이아웃 같은 기본 설정을 지정합니다.
st.title(APP_TITLE)  # Streamlit 화면의 가장 큰 제목을 표시합니다.
st.write("Streamlit is running locally.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

df = pd.DataFrame(  # 딕셔너리 데이터를 행과 열을 가진 DataFrame 표 구조로 변환합니다.
    {
        "service": ["frontend", "local run"],  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
        "status": ["running", "ready"],  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    }
)

st.dataframe(df)  # 표 형태의 데이터를 스크롤 가능한 DataFrame UI로 표시합니다.

