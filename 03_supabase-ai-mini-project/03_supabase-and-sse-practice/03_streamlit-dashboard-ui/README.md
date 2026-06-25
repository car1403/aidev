# 03_streamlit-dashboard-ui

이 단계에서는 Streamlit으로 프로젝트 화면을 구성하고 FastAPI API를 호출해 데이터를 표시합니다.

Streamlit은 빠르게 화면을 만들 수 있는 Python 기반 UI 도구입니다. 이 과정에서는 복잡한 프론트엔드 프레임워크보다 Streamlit으로 먼저 화면 흐름을 완성합니다.

## 학습 목표

- Streamlit에서 입력 폼, 버튼, 표, 상태 메시지를 구성할 수 있습니다.
- `API_BASE_URL`을 기준으로 FastAPI API를 호출할 수 있습니다.
- Supabase 데이터를 직접 읽기보다 FastAPI API를 통해 화면에 표시할 수 있습니다.
- 로그와 피드백을 대시보드 형태로 보여줄 수 있습니다.

## 화면 구성 예시

```text
상단: 프로젝트 제목, 실행 상태
왼쪽: 사용자 입력, 필터, 새로고침 버튼
본문: 대화 목록, 메시지 목록, 로그 테이블
하단: 피드백 입력, 오류 메시지 표시
```

## 실습 파일

- [01_dashboard-layout.md](./01_dashboard-layout.md)
- [02_api-base-url-and-httpx.md](./02_api-base-url-and-httpx.md)
- [03_table-chart-feedback-ui.md](./03_table-chart-feedback-ui.md)

## 체크리스트

- [ ] Streamlit 앱이 실행된다.
- [ ] FastAPI 서버 주소를 `API_BASE_URL`로 관리한다.
- [ ] API 호출 성공/실패 메시지를 화면에 표시한다.
- [ ] 로그 목록 또는 피드백 목록을 표로 표시한다.
- [ ] 화면에서 입력한 값이 API를 통해 저장된다.
