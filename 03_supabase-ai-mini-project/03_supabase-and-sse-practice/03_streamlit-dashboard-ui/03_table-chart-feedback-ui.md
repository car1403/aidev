# 03. 표, 차트, 피드백 UI

서비스 로그와 사용자 피드백은 프로젝트 품질을 설명할 때 중요한 자료가 됩니다.

## 표로 보여줄 데이터

```text
messages
-> role, content, created_at

service_logs
-> action, status, metadata, created_at

feedbacks
-> rating, comment, created_at
```

## 간단한 통계 예시

```text
전체 질문 수
AI 응답 수
오류 발생 수
평균 피드백 점수
```

## 피드백 입력 예시

```text
평점: 1~5
의견: 자유 입력
저장 버튼
```

## 체크리스트

- [ ] 로그 데이터를 표로 표시했다.
- [ ] 피드백 입력 폼을 만들었다.
- [ ] 저장 버튼 클릭 후 FastAPI API를 호출한다.
- [ ] 저장 성공/실패 메시지가 표시된다.
- [ ] 프로젝트 발표 때 보여줄 수 있는 결과 화면이 있다.
