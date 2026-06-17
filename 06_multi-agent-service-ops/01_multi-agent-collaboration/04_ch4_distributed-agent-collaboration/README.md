# 04_ch4_distributed-agent-collaboration

분산 협업 구조를 흉내 내며 Agent 간 결과를 통합하는 방법을 학습합니다.

## 핵심 개념

분산 협업은 여러 Agent가 동시에 또는 단계적으로 실행되고, 최종적으로 결과가 통합되는 구조입니다.

실제 운영 환경에서는 각 Agent가 별도 프로세스, 별도 컨테이너, 별도 작업 큐로 분리될 수 있습니다.

## Docker Compose 연결 관점

나중에 Docker Compose에서는 아래처럼 분리할 수 있습니다.

```text
backend: 요청 수신과 Supervisor 실행
worker: 오래 걸리는 Agent 작업 처리
monitor: 실행 상태와 로그 표시
```

## 실행

```powershell
python .\04_ch4_distributed-agent-collaboration\01_distributed-agent-collaboration.py
```
