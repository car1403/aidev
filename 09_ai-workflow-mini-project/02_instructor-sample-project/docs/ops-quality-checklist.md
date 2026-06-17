# Ops Quality Checklist

## 실행 전

```text
[ ] Backend /health 정상
[ ] Frontend 접속 가능
[ ] 샘플 문의 입력 가능
[ ] /analyze 응답 확인
```

## 품질 검증

```text
[ ] category가 적절한가?
[ ] urgency가 적절한가?
[ ] draft_answer가 너무 짧지 않은가?
[ ] 금지 표현이 없는가?
[ ] next_action이 상황에 맞는가?
```

## 운영 확인

```text
[ ] /events에 실행 이력이 남는가?
[ ] /metrics에 실행 횟수와 긴급 비율이 표시되는가?
[ ] 실패 또는 검증 실패 시 대체 흐름이 있는가?
```
