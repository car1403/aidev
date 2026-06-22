# 01_streamlit-basic

Streamlit을 사용해 Python 코드만으로 간단한 웹 화면을 만드는 첫 번째 단원입니다.

이 단원에서는 복잡한 AI 기능이나 API 연동보다, 화면을 띄우고 입력을 받고 결과를 보여주는 기본 흐름을 손으로 직접 작성하는 데 집중합니다.

## 학습 목표

- Streamlit 앱을 실행할 수 있다.
- 제목, 문장, 코드 블록, 상태 메시지를 화면에 출력할 수 있다.
- 텍스트, 숫자, 선택 입력을 받을 수 있다.
- 입력값을 바탕으로 간단한 결과 화면을 만들 수 있다.
- columns, tabs, sidebar를 사용해 기본 레이아웃을 구성할 수 있다.

## 학습 순서

```text
01_ch1_streamlit-project-setup
-> 02_ch2_text-input-and-output
-> 03_ch3_layout-and-pages
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
01_streamlit-basic
├─ README.md
├─ 00_references
├─ 01_ch1_streamlit-project-setup
├─ 02_ch2_text-input-and-output
├─ 03_ch3_layout-and-pages
├─ 10_labs
└─ 20_assignments
```

## 실행 방법

가상 환경을 활성화한 뒤 예제 파일을 Streamlit으로 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run.\01_streamlit-basic\01_ch1_streamlit-project-setup\01_hello-streamlit.py
```

아직 `02_supabase-ai-frontend` 가상 환경을 만들지 않았다면 다음 패키지가 필요합니다.

```powershell
pip install streamlit pandas
```

## 실행 확인 기준

- 브라우저가 열리고 Streamlit 화면이 표시된다.
- 제목과 본문 텍스트가 정상적으로 보인다.
- 입력값을 변경했을 때 화면 결과가 바뀐다.
- sidebar, columns, tabs가 화면에 구분되어 표시된다.

## 다음 단원 연결

이 단원을 마친 뒤 `02_streamlit-ui-components`에서 버튼, 폼, 표, 차트, 파일 업로드 같은 UI 컴포넌트를 더 깊게 다룹니다.

