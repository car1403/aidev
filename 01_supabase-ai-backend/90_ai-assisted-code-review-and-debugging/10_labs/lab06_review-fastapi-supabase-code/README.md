# Lab 06 - FastAPI와 Supabase 코드 리뷰

이 lab에서는 FastAPI와 Supabase를 연결한 코드를 Codex에게 리뷰하도록 요청하고, 발견된 문제를 직접 분류합니다.

백엔드 코드는 실행 여부만 보면 부족합니다. endpoint 설계, 요청/응답 모델, Supabase 테이블명, update/delete 조건, key 노출 위험까지 함께 확인해야 합니다.

## 실습 목표

- FastAPI/Supabase 코드 리뷰 관점을 작성할 수 있다.
- endpoint, Pydantic 모델, Supabase 호출 코드를 함께 볼 수 있다.
- update/delete 조건 누락 위험을 설명할 수 있다.
- service role key 노출 위험을 구분할 수 있다.
- Codex 리뷰 결과를 우선순위별로 분류할 수 있다.

## 실습 파일

```text
sample_review_target.py
```

## 실습 절차

1. `sample_review_target.py`를 읽습니다.
2. endpoint URL과 HTTP Method를 확인합니다.
3. 요청 Body가 Pydantic 모델로 검증되는지 확인합니다.
4. Supabase 테이블명과 컬럼명이 코드에서 어떻게 쓰이는지 봅니다.
5. update/delete 조건 누락 위험이 있는지 찾습니다.
6. API key 또는 service role key가 노출될 가능성이 있는지 확인합니다.
7. Codex에게 코드 리뷰를 요청합니다.
8. 리뷰 결과를 `반드시 수정`, `수정하면 좋음`, `질문 필요`, `보류`로 나눕니다.

## Codex 요청 예시

```text
이 FastAPI/Supabase 코드를 리뷰해주세요.

파일:
sample_review_target.py

리뷰 관점:
1. 실행 오류 가능성
2. endpoint URL과 HTTP Method가 적절한지
3. Pydantic 요청 모델의 검증 조건이 충분한지
4. Supabase 테이블명과 컬럼명이 맞는지
5. Supabase update/delete 조건 누락 위험이 있는지
6. service role key 노출 위험이 있는지
7. 오류 응답이 초보자가 이해할 수 있는지

출력 형식:
- 반드시 수정
- 수정하면 좋음
- 질문 필요
- 이번 실습에서는 보류

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 결과 정리

```md
## Lab 06 결과

- 리뷰한 파일:
- 발견한 실행 오류 가능성:
- 발견한 Supabase 관련 문제:
- 발견한 보안 위험:
- 반드시 수정할 항목:
- 보류한 항목과 이유:
- 수정 후 확인할 실행 방법:
```

## 완료 체크리스트

- [ ] endpoint와 HTTP Method를 확인했다.
- [ ] Pydantic 모델 검증 조건을 확인했다.
- [ ] Supabase 테이블명과 컬럼명을 확인했다.
- [ ] update/delete 조건 누락 위험을 확인했다.
- [ ] key 노출 위험을 확인했다.
- [ ] Codex 리뷰 결과를 우선순위별로 분류했다.
