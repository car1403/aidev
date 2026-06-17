# 04. Ops Quality Validation

이 문서는 팀 프로젝트의 운영, 품질, 비용, 오류 처리 기준을 설계하는 실습 문서입니다.

## 1. 작성 항목

```text
입력 검증:
출력 검증:
오류 처리:
Fallback:
로그 항목:
운영 지표:
비용 관리:
개선 기준:
```

## 2. 입력 검증

```text
빈 입력:
너무 짧은 입력:
너무 긴 입력:
민감정보 포함 입력:
Prompt Injection 의심 입력:
```

## 3. 출력 검증

```text
응답 형식:
민감정보 포함 여부:
확정할 수 없는 정보 처리:
위험한 안내 차단:
응답 품질이 낮을 때 처리:
```

## 4. 오류 처리와 Fallback

```text
AI API 실패:
RAG/Knowledge 검색 실패:
외부 API 실패:
입력 데이터 부족:
응답 형식 오류:
```

## 5. 로그와 운영 지표

```text
request_id:
category:
priority:
selected_tool:
success:
error_message:
api_calls:
estimated_cost:
duration_ms:
created_at:
```

## 6. 비용과 리소스 관리

```text
1회 실행당 예상 API 호출 수:
비용이 많이 발생할 수 있는 구간:
비용 절감 방법:
처리 시간이 오래 걸리는 작업:
동시 요청이 많아질 때 대응:
```

## 7. 품질 개선 루프

```text
테스트 결과를 어디에 기록할 것인가?
오답이 발생하면 어떤 기준으로 수정할 것인가?
Prompt를 어떻게 개선할 것인가?
Knowledge 문서는 어떻게 보강할 것인가?
운영 로그를 보고 어떤 지표를 개선할 것인가?
```
