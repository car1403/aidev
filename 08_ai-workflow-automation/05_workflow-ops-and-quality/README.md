# 05_workflow-ops-and-quality

AI 워크플로우를 만든 뒤 안정적으로 운영하고 품질을 개선하는 방법을 학습하는 단원입니다.

01~04 단원에서는 워크플로우 개념, AIPP, n8n, Dify를 활용해 AI 자동화 흐름을 설계했습니다. 05 단원에서는 만들어진 워크플로우를 실제 업무에 적용할 때 필요한 운영 관리, 비용 관리, 오류 처리, 로그 분석, 데이터 품질 검증을 다룹니다.

## 학습 목표

- Model, Prompt, Workflow 버전을 관리해야 하는 이유를 이해한다.
- API 사용량과 비용을 추적하는 기본 구조를 설계할 수 있다.
- 오류 처리와 예외 흐름을 워크플로우에 반영할 수 있다.
- 실행 로그를 분석해 워크플로우 개선 포인트를 찾을 수 있다.
- 입력/출력 데이터 품질을 검증하는 기준을 만들 수 있다.
- Prompt Injection 방어와 입력/출력 보안 필터를 설계할 수 있다.
- API 사용량, CPU/GPU/메모리 같은 실행 리소스 관리 기준을 만들 수 있다.
- Workflow 실행 흐름 최적화가 필요한 지점을 찾고 개선 전략을 세울 수 있다.
- 수평/수직 확장과 재사용 가능한 Workflow Template을 설계할 수 있다.
- Multi-Agent Workflow 운영 구조를 설계할 수 있다.
- 운영 데이터 기반 Workflow Ops Assistant 구조를 설계할 수 있다.

## 전체 구조

```text
05_workflow-ops-and-quality
├─ README.md
├─ 01_ch1_version-and-cost-management
├─ 02_ch2_error-handling-and-exception-flow
├─ 03_ch3_log-analysis-and-improvement
├─ 04_ch4_data-quality-validation
├─ 05_ch5_workflow-ops-assistant
├─ 06_ch6_prompt-injection-and-security-filters
├─ 07_ch7_resource-scaling-template-ops
├─ 08_ch8_multi-agent-workflow-ops
├─ 10_labs
└─ 20_assignments
```

## 권장 학습 순서

```text
01_ch1_version-and-cost-management
-> 02_ch2_error-handling-and-exception-flow
-> 03_ch3_log-analysis-and-improvement
-> 04_ch4_data-quality-validation
-> 05_ch5_workflow-ops-assistant
-> 06_ch6_prompt-injection-and-security-filters
-> 07_ch7_resource-scaling-template-ops
-> 08_ch8_multi-agent-workflow-ops
-> 10_labs
-> 20_assignments
```

## 단원별 핵심 내용

| 챕터 | 내용 |
| --- | --- |
| 01_ch1_version-and-cost-management | 모델, 프롬프트, 워크플로우 버전 관리와 비용 추적 |
| 02_ch2_error-handling-and-exception-flow | 오류 처리, 재시도, 대체 경로, 사람 검토 흐름 |
| 03_ch3_log-analysis-and-improvement | 실행 로그 분석과 운영 데이터 기반 개선 |
| 04_ch4_data-quality-validation | 입력/출력 검증, 응답 필터링, 데이터 품질 관리 |
| 05_ch5_workflow-ops-assistant | 운영 데이터를 바탕으로 개선안을 제안하는 Ops Assistant 설계 |
| 06_ch6_prompt-injection-and-security-filters | Prompt Injection 방어, 입력 검증, 출력 필터링, 보안 정책 적용 |
| 07_ch7_resource-scaling-template-ops | API 사용량, 실행 리소스, Workflow 실행 흐름 최적화, 확장성, 재사용 가능한 Workflow Template 운영 |
| 08_ch8_multi-agent-workflow-ops | Multi-Agent 기반 역할 분리, 협업 Workflow, 운영 추적 구조 |
| 10_labs | 운영/품질 실습 |
| 20_assignments | 워크플로우 운영 설계 과제 |

## 왜 운영과 품질이 중요한가?

AI 워크플로우는 한 번 만든 뒤 끝나는 자동화가 아닙니다.

실제 업무에서는 다음 문제가 계속 발생합니다.

```text
프롬프트를 바꾸니 답변 품질이 달라짐
모델을 바꾸니 비용과 응답 시간이 달라짐
외부 API가 실패함
입력 데이터가 비어 있거나 형식이 틀림
LLM 출력이 기대한 JSON 형식이 아님
사용자가 부적절한 입력을 보냄
실행 로그가 없어 원인 분석이 어려움
```

그래서 워크플로우에는 운영 기준이 필요합니다.

```text
Version
Cost
Error Handling
Log
Quality Validation
Improvement Loop
```

## 운영 관점의 기본 흐름

```text
Workflow 실행
-> 입력 검증
-> AI/Tool 실행
-> 오류 처리
-> 출력 검증
-> 로그 저장
-> 비용/사용량 기록
-> 품질 분석
-> 실행 흐름 최적화
-> 개선안 반영
```

여기서 `Workflow 실행 흐름 최적화`는 단순히 서버 자원을 늘리는 일이 아닙니다.
수업 참여자는 실행 로그를 보고 오래 걸리는 노드, 반복 호출이 많은 노드, 실패가 자주 발생하는 노드, 불필요하게 비용이 큰 API 호출을 찾아 워크플로우 순서와 조건을 개선하는 연습을 하게 됩니다.

## 실행 준비

상위 폴더에서 가상 환경을 활성화합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

05 단원의 예제는 외부 API 없이 실행됩니다.

## 실습 파일 실행 순서

```powershell
cd C:\aidev\08_ai-workflow-automation\05_workflow-ops-and-quality
python .\01_ch1_version-and-cost-management\01_version_cost_tracker.py
python .\02_ch2_error-handling-and-exception-flow\01_exception_flow_runner.py
python .\03_ch3_log-analysis-and-improvement\01_workflow_log_analyzer.py
python .\04_ch4_data-quality-validation\01_data_quality_validator.py
python .\05_ch5_workflow-ops-assistant\01_workflow_ops_assistant.py
python .\06_ch6_prompt-injection-and-security-filters\01_prompt_injection_security_filter.py
python .\07_ch7_resource-scaling-template-ops\01_resource_scaling_template_ops.py
python .\08_ch8_multi-agent-workflow-ops\01_multi_agent_workflow_ops.py
```

## 이후 과정과의 연결

05 단원은 99 미니 프로젝트로 연결됩니다.

```text
01~04에서 워크플로우 설계와 구현 흐름 학습
-> 05에서 운영, 품질, 비용, 오류 처리 기준 학습
-> 99에서 실제 Tech Support AI Workflow 미니 프로젝트 구현
```
