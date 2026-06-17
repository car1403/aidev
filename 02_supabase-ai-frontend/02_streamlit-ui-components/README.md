# 02_streamlit-ui-components

Streamlit에서 자주 사용하는 UI 컴포넌트를 직접 다루는 단원입니다.

`01_streamlit-basic`에서 화면 출력, 입력, 기본 레이아웃을 배웠다면, 이 단원에서는 버튼, 폼, 표, 차트, 파일 업로드, 대시보드 구성을 학습합니다.

pandas는 데이터 분석 전체를 깊게 다루기보다, Streamlit에서 표와 차트를 만들기 위해 필요한 만큼만 사용합니다.

## 학습 목표

- 버튼, 체크박스, 슬라이더, 폼을 사용할 수 있다.
- 리스트와 딕셔너리 데이터를 pandas DataFrame으로 바꿀 수 있다.
- `st.dataframe`, `st.table`로 표를 출력할 수 있다.
- 간단한 필터링과 요약 값을 만들 수 있다.
- Streamlit 기본 차트를 출력할 수 있다.
- CSV 파일을 업로드하고 화면에 표시할 수 있다.
- 여러 UI 요소를 조합해 기본 대시보드를 만들 수 있다.

## 학습 순서

```text
01_ch1_buttons-forms-and-controls
-> 02_ch2_dataframe-table-basics
-> 03_ch3_charts-and-files
-> 04_ch4_dashboard-layout
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
02_streamlit-ui-components
├─ README.md
├─ 00_references
├─ 01_ch1_buttons-forms-and-controls
├─ 02_ch2_dataframe-table-basics
├─ 03_ch3_charts-and-files
├─ 04_ch4_dashboard-layout
├─ 10_labs
└─ 20_assignments
```

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-frontend
streamlit run .\02_streamlit-ui-components\01_ch1_buttons-forms-and-controls\01_button-click.py
```

필요 패키지는 다음과 같습니다.

```powershell
pip install streamlit pandas
```

## 실행 확인 기준

- 버튼 클릭 여부에 따라 화면 결과가 바뀐다.
- 폼 입력 후 제출 버튼을 눌렀을 때 결과가 표시된다.
- DataFrame 표가 화면에 표시된다.
- CSV 업로드 후 데이터가 표시된다.
- 차트와 필터가 함께 동작한다.

## 다음 단원 연결

이 단원을 마치면 `03_api-integration`에서 Streamlit 화면과 FastAPI 백엔드를 HTTP 요청으로 연결합니다.

