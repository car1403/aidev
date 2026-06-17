# Streamlit UI Components Notes

## 핵심 UI 컴포넌트

- `st.button()`: 버튼 클릭 이벤트를 처리합니다.
- `st.checkbox()`: 참/거짓 선택을 받습니다.
- `st.slider()`: 숫자 범위 입력을 받습니다.
- `st.form()`: 여러 입력값을 한 번에 제출합니다.
- `st.dataframe()`: 스크롤 가능한 표를 표시합니다.
- `st.table()`: 정적인 표를 표시합니다.
- `st.line_chart()`: 선 그래프를 표시합니다.
- `st.bar_chart()`: 막대 그래프를 표시합니다.
- `st.file_uploader()`: 파일 업로드 입력을 받습니다.

## pandas를 사용하는 이유

Streamlit에서 표와 차트를 다룰 때 데이터는 보통 pandas DataFrame 형태로 사용합니다.

이 단원에서는 다음 정도만 익히면 충분합니다.

- `pd.DataFrame()`으로 표 데이터 만들기
- 컬럼 이름 확인하기
- 조건으로 행 필터링하기
- 합계와 평균 계산하기
- CSV 파일을 `pd.read_csv()`로 읽기

## 수업 운영 팁

pandas 문법을 많이 외우게 하기보다, Streamlit 화면을 만들기 위해 필요한 데이터 모양을 이해시키는 데 집중합니다.

