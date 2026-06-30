# 01. Debugging Playbook

오류가 나면 바로 코드를 고치기보다, 먼저 정보를 모읍니다.

## 1. 실행 명령 확인

어떤 폴더에서 어떤 명령을 실행했는지 확인합니다.

```powershell
Get-Location
python -c "import sys; print(sys.executable)"
```

FastAPI 실행 예:

```powershell
uvicorn main:app --reload
```

## 2. 오류 유형 분류

| 오류 유형 | 먼저 볼 것 |
| --- | --- |
| `ModuleNotFoundError` | `.venv` 활성화, `pip install -r requirements.txt` 실행 여부 |
| 404 Not Found | URL 경로가 코드의 endpoint와 같은지 |
| 405 Method Not Allowed | GET/POST/PUT/DELETE를 맞게 사용했는지 |
| 422 Validation Error | 요청 Body가 Pydantic 모델과 맞는지 |
| Gemini 503 | 모델 수요가 높아 일시적으로 실패했는지 |
| Supabase table error | 테이블명과 컬럼명이 실제 SQL과 같은지 |
| Invalid login credentials | 회원가입 여부, 이메일 인증 설정, 비밀번호 확인 |
| RLS access error | JWT/Bearer token, RLS policy, key 종류 확인 |

## 3. Codex에게 물어보는 형식

```text
아래 오류를 분석해주세요.

실행 위치:
C:\aidev\02_supabase-ai-backend\...

실행 명령:
uvicorn main:app --reload

기대 결과:
Swagger에서 POST /ai/chat이 동작해야 합니다.

실제 결과:
405 Method Not Allowed

요청:
아직 코드를 수정하지 말고, 가능한 원인과 확인 순서를 초보자 기준으로 설명해주세요.
```

## 4. 수정 전 확인

- 내가 실행한 파일과 문서가 같은 단원의 것인가?
- 터미널의 Python 경로가 현재 과정의 `.venv`인가?
- `.env` 파일이 필요한 폴더에 있는가?
- Swagger에서 GET이 아니라 POST를 눌렀는가?
- 실제 API 호출 전에 mock 예제로 먼저 확인했는가?
