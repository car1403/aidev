# Environment Guide

이 과정은 Windows, PowerShell, VS Code, Python `.venv` 기준으로 설명합니다.

## Python과 `.venv`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`01`, `02`, `03`, `04`, `06`, `07`, `08`은 과정 최상위 `.venv` 하나를 기본으로 사용합니다. `05`는 단원별 의존성이 달라질 수 있어 단원별 `.venv` 방식을 우선 권장합니다.

## VS Code

`01`, `02`, `03`, `04`, `06`, `07`, `08` 과정에는 `.vscode/settings.json`이 포함되어 있습니다. 해당 과정 폴더 자체를 VS Code로 열면 새 터미널에서 `.venv`가 자동 활성화됩니다.

`C:\aidev` 루트를 열면 하위 과정의 `.vscode/settings.json`이 자동 적용되지 않을 수 있습니다.

## 선택 도구

Postman은 FastAPI API를 직접 테스트할 때 사용할 수 있는 선택 도구입니다. 설치가 필요하면 아래 공식 다운로드 페이지를 사용합니다.

```text
https://www.postman.com/downloads/
```

Postman을 설치하지 않아도 FastAPI의 Swagger UI(`/docs`)와 PowerShell `Invoke-RestMethod`로 기본 API 테스트를 진행할 수 있습니다.

## Gemini와 OpenAI 계정

이 과정의 02~04 과정에서는 Gemini API를 기본 LLM API로 사용합니다. OpenAI API는 선택/비교 실습에서 사용합니다.

Gemini를 사용할 때는 아래 항목을 먼저 확인합니다.

```text
1. Google 계정으로 Google AI Studio에 로그인했는가?
2. Gemini API Key를 발급했는가?
3. 무료 범위, rate limit, quota, 유료 전환 조건을 공식 화면에서 확인했는가?
4. GEMINI_API_KEY를 .env에만 저장하고 GitHub에 올리지 않는가?
5. 수업 중 API 호출 횟수를 과도하게 늘리지 않도록 주의하는가?
```

참고 공식 문서:

- Gemini API Key: https://aistudio.google.com/app/apikey
- Gemini API Key 보안: https://ai.google.dev/gemini-api/docs/api-key
- Gemini API 가격: https://ai.google.dev/gemini-api/docs/pricing
- Gemini API rate limit: https://ai.google.dev/gemini-api/docs/rate-limits

OpenAI를 사용할 때는 아래 항목을 확인합니다.

```text
1. OpenAI 계정으로 로그인했는가?
2. API Key를 발급했는가?
3. 결제 수단, 사용량 한도, 조직/프로젝트 설정을 확인했는가?
4. OPENAI_API_KEY를 .env에만 저장하고 GitHub에 올리지 않는가?
```

OpenAI API는 ChatGPT 구독과 별도로 과금/사용량이 관리될 수 있습니다. 수업에서 OpenAI 예제를 실행하기 전에는 아래 화면을 직접 확인합니다.

```text
1. OpenAI Platform에 로그인했는가?
2. API Keys 화면에서 프로젝트용 API Key를 만들었는가?
3. Billing/Usage 화면에서 결제 방식과 현재 사용량을 확인했는가?
4. Limits 또는 Project settings에서 월 예산, 알림, rate limit을 확인했는가?
5. 실습용 Key를 GitHub, README, 화면 캡처, 로그에 노출하지 않는가?
```

참고 공식 문서:

- OpenAI Platform 로그인: https://platform.openai.com/
- OpenAI API Key 관리: https://platform.openai.com/api-keys
- OpenAI API 사용량 확인: https://platform.openai.com/usage
- OpenAI API 결제/사용량 도움말: https://help.openai.com/en/collections/3675945-understanding-openai-api-billing-and-usage
- OpenAI 사용량 대시보드 안내: https://help.openai.com/en/articles/10478918-api-usage-dashboard
- OpenAI usage limit 안내: https://help.openai.com/en/articles/6643435-how-do-i-get-more-tokens-or-increase-my-monthly-usage-limits
- OpenAI 프로젝트와 예산/한도 관리: https://help.openai.com/en/articles/9186755-managing-your-work-in-the-api-platform-with-projects

API 가격, 무료 범위, rate limit, quota는 수시로 바뀔 수 있습니다. 수업 자료의 예시보다 각 서비스의 공식 콘솔과 공식 문서를 우선 기준으로 삼습니다.

## `.env`와 보안

```text
.env
-> 실제 실행에 사용하는 비밀 값
-> GitHub와 제출물에 포함하지 않음

.env.example
-> 필요한 환경변수 이름을 보여주는 예시
-> 실제 key를 넣지 않음
-> GitHub에 포함 가능
```

실제 API Key, Supabase service role key, AWS Access Key, 비밀번호, token은 README, 발표 자료, 화면 캡처, 로그에 남기지 않습니다.

## Docker와 AWS

- `05`부터 Docker Desktop을 사용합니다.
- `05`는 주로 `docker run`으로 Ollama, pgvector 같은 도구를 실행합니다.
- `07`부터 Docker Compose, GitHub Actions, AWS 선택 배포를 다룹니다.
- AWS 실습은 비용이 발생할 수 있으므로 선택 실습으로 진행합니다.
