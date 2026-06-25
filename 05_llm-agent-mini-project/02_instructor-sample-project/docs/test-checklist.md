# Test Checklist

이 체크리스트의 명령은 아래 폴더에서 실행합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
```

## 실행 준비

- [ ] 최상위 `.venv`를 활성화했습니다.
- [ ] `python -m pip install --upgrade pip`를 실행했습니다.
- [ ] `pip install -r ..\requirements.txt`를 실행했습니다.
- [ ] `.env.example`을 `.env`로 복사했습니다.

## CLI

- [ ] `python -m app.graph` 실행이 성공합니다.
- [ ] 가능한 후보 시간이 출력됩니다.
- [ ] 제안 메시지가 출력됩니다.
- [ ] API Key가 없어도 규칙 기반 메시지가 생성됩니다.

## Streamlit

- [ ] `streamlit run .\frontend\streamlit_app.py --server.port 8701` 실행이 성공합니다.
- [ ] 요청 입력이 가능합니다.
- [ ] Agent 실행 버튼이 동작합니다.
- [ ] 최종 답변이 표시됩니다.
- [ ] 상태 JSON 또는 실행 결과를 확인할 수 있습니다.

## 확장 확인

- [ ] 참석자 이름을 바꾸면 결과가 달라집니다.
- [ ] 회의 시간을 바꾸면 State에 반영됩니다.
- [ ] 공통 시간이 없는 경우 fallback 메시지를 확인했습니다.
