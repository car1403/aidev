# 01_ch1_single-vs-multi-agent

단일 Agent와 Multi-Agent 구조를 비교합니다.

## 핵심 개념

단일 Agent는 하나의 Agent가 요청 분석, 도구 선택, 실행, 검증을 모두 처리합니다.

Multi-Agent는 역할별 Agent가 나뉘어 각자 맡은 일을 처리하고, 최종 결과를 통합합니다.

## 비교 기준

| 기준 | 단일 Agent | Multi-Agent |
| --- | --- | --- |
| 구조 | 단순함 | 복잡함 |
| 책임 분리 | 약함 | 강함 |
| 디버깅 | 처음에는 쉬움 | 로그와 상태 설계 필요 |
| 확장성 | 제한적 | 역할별 확장 가능 |
| 운영 | 작은 서비스에 적합 | 복잡한 서비스에 적합 |

## 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
..\.venv\Scripts\Activate.ps1
python.\01_ch1_single-vs-multi-agent\01_single-agent-vs-multi-agent.py
```
