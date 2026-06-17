# 02 Failure Recovery Design

장애 유형별 복구 로직을 설계합니다.

| 장애 유형 | 감지 기준 | 복구 조치 | 실패 시 다음 단계 |
| --- | --- | --- | --- |
| unhealthy | `/health` 실패 | restart | escalate |
| timeout | 응답 지연 | retry | fallback |
