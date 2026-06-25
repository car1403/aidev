# Dashboard Result Template

대시보드 구현 결과물 문서 템플릿입니다.

## 1. 대시보드 목적

```text
이 대시보드는 어떤 데이터를 확인하기 위한 화면인가?
어떤 사용자가 어떤 판단을 할 수 있는가?
```

## 2. 구현 화면

| 화면 | 설명 | 캡처 |
| --- | --- | --- |
| 메인 대시보드 | 전체 로그와 지표 확인 |  |
| 로그 등록 | 새 로그 또는 질문 입력 |  |
| 로그 상세 | 단일 로그 상세 확인 |  |
| 피드백 | 응답 품질 평가 |  |

## 3. 주요 지표

| 지표 | 의미 | 데이터 출처 |
| --- | --- | --- |
| 전체 로그 수 | 저장된 이벤트 수 | service_logs |
| 성공 요청 수 | 정상 처리된 요청 | service_logs.status |
| 오류 수 | 실패한 요청 | service_logs.status |
| 평균 피드백 | 사용자 만족도 | feedbacks.rating |

## 4. 실행 방법

```powershell
cd C:\aidev\04_supabase-ai-mini-project\99_team-projects\팀폴더\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

```powershell
cd C:\aidev\04_supabase-ai-mini-project\99_team-projects\팀폴더\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

## 5. 개선 방향

```text
데이터가 부족한 부분:
화면에서 더 보기 쉽게 바꿀 부분:
오류 처리 보완점:
AI 응답 품질 개선 방향:
```
