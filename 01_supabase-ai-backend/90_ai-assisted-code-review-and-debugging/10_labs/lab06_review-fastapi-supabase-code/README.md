# Lab 06 - FastAPI Supabase 코드 리뷰

## 목표

FastAPI와 Supabase를 연결한 코드를 Codex에게 리뷰하도록 요청하고, 문제점을 스스로 분류합니다.

## 실습 파일

```text
sample_review_target.py
```

## 실습 절차

1. `sample_review_target.py`를 읽습니다.
2. 실행 오류, 보안 문제, Supabase 사용 문제를 직접 표시합니다.
3. Codex에게 코드 리뷰를 요청합니다.
4. Codex의 지적을 다음 기준으로 분류합니다.

```text
반드시 수정
수정하면 좋음
질문 필요
이번 실습에서는 보류
```

## 요청 예시

```text
이 FastAPI/Supabase 코드를 리뷰해줘.

관점:
1. 실행 오류 가능성
2. Supabase update/delete 조건 누락
3. service role key 노출 위험
4. Pydantic 검증 부족
5. 초보자가 이해하기 어려운 부분
```
