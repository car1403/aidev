# 00_references

`05_state-session-and-data`에서 상태 관리와 인증 흐름을 이해하기 위한 참고 자료입니다.

## 문서와 파일

| 파일 | 설명 |
| --- | --- |
| `state-session-notes.md` | Streamlit 상태 관리, 인증 흐름, 보안 기준을 정리합니다. |
| `backend-auth-session-sample.py` | 백엔드 인증 단원이 준비되지 않았을 때 사용하는 보조 FastAPI 샘플입니다. |

## 샘플 백엔드 실행

```powershell
cd C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-auth-session-sample:app --reload --host 127.0.0.1 --port 8000
```

샘플 계정은 다음과 같습니다.

```text
student / 1234
```

이 샘플은 Supabase를 대체하지 않습니다. token 저장, Authorization header, 사용자별 대화 이력 화면 흐름을 빠르게 확인하기 위한 보조 자료입니다.
