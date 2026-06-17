# Security And Cost Checklist

AI 백엔드 수업에서 보안과 비용 문제를 줄이기 위한 체크리스트입니다.

## 민감 정보

- [ ] `.env` 파일은 GitHub에 올리지 않습니다.
- [ ] `.env.example`에는 실제 key가 아닌 예시 값만 둡니다.
- [ ] `GEMINI_API_KEY`, `OPENAI_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `UPSTASH_REDIS_REST_TOKEN`을 print하지 않습니다.
- [ ] 01~03 과정에서는 Gemini API를 기본으로 사용하고, OpenAI API는 선택/비교 실습일 때만 호출합니다.
- [ ] service role key는 FastAPI 서버 코드에서만 사용합니다.
- [ ] Streamlit, 브라우저 JavaScript, README 캡처에 secret이 노출되지 않게 합니다.

## 비용

- [ ] mock 예제로 먼저 API 구조를 검증합니다.
- [ ] 실제 LLM API 호출은 강사가 과금 상태를 확인한 뒤 진행합니다.
- [ ] `max_tokens`를 너무 크게 설정하지 않습니다.
- [ ] 반복문 안에서 실제 LLM API를 무제한 호출하지 않습니다.
- [ ] 실패 재시도 로직이 무한 반복되지 않도록 제한합니다.

## 로그

- [ ] 로그에는 key/token을 남기지 않습니다.
- [ ] 오류 로그에는 필요한 최소 정보만 남깁니다.
- [ ] 사용자 질문을 로그로 남길 경우 개인정보 포함 가능성을 고려합니다.
- [ ] 운영 로그와 사용자 대화 이력을 구분합니다.
