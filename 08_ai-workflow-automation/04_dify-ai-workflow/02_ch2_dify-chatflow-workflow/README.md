# 02_ch2_dify-chatflow-workflow

Dify의 Chatflow와 Workflow 차이를 학습하는 챕터입니다.

## 핵심 개념

```text
Chatflow: 사용자와 여러 번 대화하는 흐름에 적합
Workflow: 한 번 호출해서 정해진 결과를 만드는 업무 처리 흐름에 적합
```

## 예시

```text
Chatflow:
사용자가 질문
-> 대화 맥락 유지
-> 문서 검색
-> 답변
-> 추가 질문

Workflow:
입력 데이터 수신
-> 분류
-> 문서 검색
-> 결과 생성
-> JSON 반환
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\04_dify-ai-workflow
python .\02_ch2_dify-chatflow-workflow\01_chatflow_vs_workflow.py
```
