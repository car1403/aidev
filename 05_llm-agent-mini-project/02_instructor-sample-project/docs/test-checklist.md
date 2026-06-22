# Test Checklist

이 체크리스트의 명령은 아래 폴더에서 실행합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
```

## CLI

- [ ] 상위 폴더 `.venv` 활성화 완료
- [ ] `pip install -r..\requirements.txt` 실행 완료
- [ ] `python -m app.graph` 실행 성공
- [ ] 가능한 후보 시간이 출력됨
- [ ] 제안 메시지가 출력됨

## Streamlit

- [ ] `streamlit run.\frontend\streamlit_app.py --server.port 8701` 실행 성공
- [ ] 요청 입력 가능
- [ ] 에이전트 실행 버튼 동작
- [ ] 최종 답변 표시
- [ ] 상태 JSON 표시

## 확장 확인

- [ ] 참석자 이름을 바꾸면 결과가 달라짐
- [ ] 회의 시간을 바꾸면 state에 반영됨
- [ ] API Key 없이도 규칙 기반 메시지가 생성됨
