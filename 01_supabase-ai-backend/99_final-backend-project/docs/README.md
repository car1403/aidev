# Final Backend Project Docs

이 폴더는 최종 백엔드 프로젝트의 설계 문서와 검증 결과를 정리하는 공간입니다.

문서는 코드만큼 중요합니다. API가 어떤 역할을 하는지, 데이터가 어디에 저장되는지, 어떤 환경 변수가 필요한지, 어떤 테스트를 했는지 문서로 남겨야 프로젝트를 다시 확인하기 쉽습니다.

## 작성 문서

```text
api-design.md
database-design.md
env-guide.md
service-data-flow.md
security-cost-check.md
test-result.md
codex-review-log.md
```

## 문서 작성 기준

- 이해한 내용을 직접 작성합니다.
- 실제 API key, token, service role key는 적지 않습니다.
- 실행 결과는 Swagger UI, 터미널 출력, Supabase Table Editor 결과를 기준으로 정리합니다.
- Codex 답변은 그대로 붙여 넣지 않고, 반영한 내용과 보류한 내용을 나누어 기록합니다.
- Docker, AWS 배포, SSE 스트리밍은 이 프로젝트의 필수 제출 범위가 아닙니다.
