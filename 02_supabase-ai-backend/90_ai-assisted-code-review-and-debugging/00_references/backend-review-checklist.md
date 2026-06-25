# Backend Review Checklist

FastAPI, Supabase, LLM API, Upstash Redis 실습 코드를 리뷰할 때 사용하는 체크리스트입니다.

## FastAPI

- [ ] endpoint URL이 리소스 중심으로 작성되었나요?
- [ ] HTTP Method가 의미에 맞게 사용되었나요?
- [ ] 요청 Body가 Pydantic 모델로 검증되나요?
- [ ] 응답 모델이 실제 반환 데이터와 일치하나요?
- [ ] 빈 문자열, 너무 긴 입력, 잘못된 role 값이 차단되나요?
- [ ] 없는 데이터 조회 시 404를 반환하나요?
- [ ] 서버 설정 문제는 500 계열 오류로 구분되나요?
- [ ] Swagger UI에서 요청/응답 예시를 확인할 수 있나요?

## Supabase

- [ ] `.env`에서 URL/key를 읽나요?
- [ ] anon key와 service role key의 역할이 구분되나요?
- [ ] service role key를 프론트엔드에 노출하지 않나요?
- [ ] insert 결과가 비어 있을 때 오류 처리가 있나요?
- [ ] update/delete에 `.eq(...)` 조건이 있나요?
- [ ] 테이블명과 컬럼명이 SQL과 일치하나요?
- [ ] 사용자별 데이터라면 user_id 또는 owner_id 조건이 있나요?
- [ ] RLS가 필요한 데이터인지 판단했나요?

## LLM API

- [ ] Gemini SDK 기본 사용 흐름이 문서와 코드에 반영되어 있나요?
- [ ] REST 호출 예제는 구조 이해용 보충으로 분리되어 있나요?
- [ ] OpenAI 예제는 선택 실습 또는 비교 실습으로 분리되어 있나요?
- [ ] mock-first 호출과 실제 Gemini SDK 호출이 명확히 분리되어 있나요?
- [ ] `provider`, `model`, `actual_api_called`, `llm_call_mode`로 호출 상태를 구분하나요?
- [ ] 실제 API 호출 전 key 존재 여부를 확인하나요?
- [ ] 최대 출력 길이 같은 비용 제한 값이 있나요?
- [ ] 반복문에서 실제 API를 과도하게 호출하지 않나요?
- [ ] API 오류 발생 시 사용자에게 적절한 메시지를 반환하나요?

## Upstash Redis

- [ ] Redis token이 출력되거나 프론트엔드에 노출되지 않나요?
- [ ] 세션, 캐시, rate limit key가 목적별로 구분되나요?
- [ ] TTL이 필요한 key에 만료 시간이 설정되어 있나요?
- [ ] rate limit key가 사용자별로 분리되어 있나요?
- [ ] Redis에 오래 보관해야 할 데이터를 저장하지 않나요?
- [ ] 최종 대화 이력과 로그는 Supabase에 저장되나요?

## Service Logs

- [ ] 성공/실패 로그가 남나요?
- [ ] `event_type`이 일관되게 작성되었나요?
- [ ] `metadata`에 endpoint, provider, model, actual_api_called, llm_call_mode, item_id 등 필요한 정보가 있나요?
- [ ] API key, token, 개인정보 같은 민감 정보가 로그에 들어가지 않나요?
- [ ] 로그 저장 실패가 전체 API 실패로 이어지지 않나요?

## Mini Service

- [ ] 요구사항 문서와 구현 결과가 일치하나요?
- [ ] API 설계 문서와 실제 endpoint가 일치하나요?
- [ ] SQL 스키마와 Python 코드의 테이블명/컬럼명이 일치하나요?
- [ ] mock-first 구현과 Supabase 구현의 역할이 명확히 구분되나요?
- [ ] 최종 프로젝트로 확장하기 전 개선 항목이 정리되어 있나요?
