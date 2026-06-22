# 03_ch3_tool-permission-control

Tool 실행 권한 제어는 Agent가 어떤 도구를 사용할 수 있는지 제한하는 구조입니다.

## 왜 필요한가?

모든 Agent가 모든 Tool을 실행할 수 있으면 위험합니다.

예를 들어 `viewer_agent`는 로그 조회만 가능해야 하고, `ops_agent`만 재시작 요청을 만들 수 있어야 합니다.

## 기본 흐름

```text
Agent 역할 확인
-> Tool 요청 확인
-> 권한 검사
-> 허용된 경우만 실행
```

## 실행

```powershell
python.\03_ch3_tool-permission-control\01_tool-permission-control.py
```
