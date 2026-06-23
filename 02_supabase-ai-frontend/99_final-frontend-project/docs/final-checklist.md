# Final Frontend Project Checklist

최종 실습을 마친 뒤 직접 확인하는 체크리스트입니다.

## 로컬 실행

- [ ] `02_supabase-ai-frontend`의 `.venv`를 활성화했다.
- [ ] 필요한 패키지를 설치했다.
- [ ] `.env` 파일을 만들었다.
- [ ] FastAPI 백엔드를 실행했다.
- [ ] `http://127.0.0.1:8000/health`가 열린다.
- [ ] Streamlit 프론트엔드를 실행했다.
- [ ] `http://localhost:8501`이 열린다.

## 기능 확인

- [ ] Chatbot 화면에서 질문을 보낼 수 있다.
- [ ] assistant 응답이 화면에 표시된다.
- [ ] Chat History 화면에서 대화 이력을 볼 수 있다.
- [ ] Service Logs 화면에서 API 호출 로그를 볼 수 있다.
- [ ] Deployment Check 화면에서 백엔드 연결을 확인할 수 있다.

## 배포 확인

- [ ] 백엔드 코드를 GitHub 저장소에 올렸다.
- [ ] Render에서 FastAPI 백엔드를 배포했다.
- [ ] Render 환경변수에 필요한 값을 등록했다.
- [ ] Upstash Redis를 만들고 REST URL/Token을 확인했다.
- [ ] Streamlit Community Cloud에 프론트엔드를 배포했다.
- [ ] Streamlit Secrets에 `API_BASE_URL`을 등록했다.
- [ ] 배포된 Streamlit 화면에서 Render 백엔드 호출이 성공한다.

## 보안 확인

- [ ] `.env` 파일을 GitHub에 올리지 않았다.
- [ ] API key와 token을 코드에 직접 쓰지 않았다.
- [ ] Upstash token은 백엔드 환경변수에만 등록했다.
- [ ] Supabase service role key를 프론트엔드에 넣지 않는 이유를 설명할 수 있다.
- [ ] Gemini API key는 실제 서비스 구조에서 백엔드에 두는 것이 원칙임을 설명할 수 있다.

## 03 미니 프로젝트 연결

- [ ] 메모리 저장을 Supabase 저장으로 바꿔야 하는 이유를 설명할 수 있다.
- [ ] 대화 이력, 서비스 로그, 피드백 테이블이 왜 필요한지 설명할 수 있다.
- [ ] SSE 스트리밍을 03에서 다루는 이유를 설명할 수 있다.
- [ ] 03에서 API 설계 문서, 화면 설계서, DB 설계서가 필요한 이유를 설명할 수 있다.
