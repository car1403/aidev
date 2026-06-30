# Frontend Starter

최종 프로젝트용 Streamlit frontend starter입니다. 기본 코드는 backend `/health` 연결 확인만 제공합니다.

## 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\03_project_structure\frontend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

## 구현할 화면

- 실시간 로그 스트림 영역
- 최근 로그 테이블
- level/status별 차트
- 로그 생성 또는 테스트 이벤트 입력 폼
- AI 답변 품질 피드백 입력/조회 영역
- 배포 전 점검 영역

구현 예시는 `01_supabase-and-sse-practice/frontend/app.py`를 참고합니다.
