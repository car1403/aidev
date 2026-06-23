# Assignment 05 - 대화 이력과 서비스 로그 저장 설계

AI 챗봇 서비스에서 사용자 대화와 서비스 로그를 어떻게 저장할지 설계하는 과제입니다.

앞 단원인 `05_llm-api-integration`에서는 실제 프로젝트 기본 LLM 호출 방식을 Gemini SDK로 정리했습니다. 이 과제에서는 실제 호출을 필수로 하지 않지만, mock 응답과 Gemini SDK 응답을 같은 테이블 구조로 저장할 수 있도록 설계해야 합니다.

## 목표

- 대화 이력과 서비스 로그의 목적을 구분할 수 있습니다.
- 사용자 질문과 AI 응답을 어떤 순서로 저장할지 설명할 수 있습니다.
- 오류 발생 시 어떤 정보를 로그에 남겨야 하는지 설계할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. conversations 테이블 역할
2. messages 테이블 역할
3. service_logs 테이블 역할
4. 사용자 질문 저장 순서
5. AI 응답 저장 순서
6. 오류 발생 시 service_logs.metadata에 넣을 정보
7. 관리자 화면에서 조회하면 좋은 로그 필터 조건 3개
8. Redis가 아니라 Supabase에 저장해야 하는 데이터 설명
9. Gemini SDK 응답을 저장할 때 추가로 남길 metadata
```

## 저장 흐름 예시

```text
1. 사용자가 질문을 입력한다.
2. conversations에 대화 묶음이 없으면 새로 만든다.
3. messages에 사용자 질문을 저장한다.
4. mock 응답을 생성하거나 Gemini SDK 응답을 생성한다.
5. messages에 AI 응답을 저장한다.
6. service_logs에 호출 결과 또는 오류를 저장한다.
```

## 확인 기준

- 대화 이력과 로그를 같은 테이블에 섞지 않았습니다.
- 오류 로그에 필요한 정보가 구체적입니다.
- 장기 보관 데이터와 임시 캐시 데이터를 구분했습니다.
- `actual_api_called=false`인 mock 응답과 `actual_api_called=true`인 Gemini SDK 응답을 모두 기록할 수 있습니다.
