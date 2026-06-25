# 무료 배포 서비스 사용 가이드

이 문서는 `99_final-frontend-project` 예제를 무료 배포 서비스에 올려 보는 과정을 안내합니다.

배포 목표는 다음과 같습니다.

```text
FastAPI 백엔드 -> Render
Redis 캐시/로그 보조 저장소 -> Upstash
Streamlit 프론트엔드 -> Streamlit Community Cloud
```

이 배포 실습은 02 프론트엔드 과정의 마무리 실습입니다. Docker, Docker Compose, AWS, GitHub Actions 기반 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 0. 로컬 실행과 배포 실행의 차이

로컬 실행과 배포 실행은 백엔드 주소가 다릅니다.

```text
로컬 백엔드:
http://127.0.0.1:8000

배포 백엔드:
https://서비스이름.onrender.com
```

Streamlit은 `API_BASE_URL` 값을 보고 백엔드 주소를 결정합니다.

```text
로컬 실습:
API_BASE_URL=http://127.0.0.1:8000

배포 후:
API_BASE_URL=https://서비스이름.onrender.com
```

## 1. 준비물

| 서비스 | 용도 |
| --- | --- |
| GitHub | 배포할 코드를 저장하는 곳 |
| Render | FastAPI 백엔드를 배포하는 곳 |
| Upstash | Redis를 서버 설치 없이 사용하는 곳 |
| Streamlit Community Cloud | Streamlit 프론트엔드를 배포하는 곳 |

주의할 점은 다음과 같습니다.

- `.env` 파일은 GitHub에 올리지 않습니다.
- API key, Upstash token, Supabase service role key는 코드에 직접 쓰지 않습니다.
- 배포 서비스의 Environment Variables 또는 Secrets 메뉴에 값을 등록합니다.

## 2. GitHub 저장소 준비

초보자에게는 전체 `C:\aidev`를 그대로 올리기보다 배포할 예제만 별도 저장소로 정리하는 방식을 권장합니다.

예시 저장소 구조:

```text
my-final-frontend-project
├─ backend
│  ├─ main.py
│  └─ requirements.txt
└─ frontend
   ├─ app.py
   ├─ requirements.txt
   └─ pages
      ├─ 01_chatbot.py
      ├─ 02_chat_history.py
      ├─ 03_service_logs.py
      └─ 04_deployment_check.py
```

현재 예제에서 복사할 폴더는 다음 두 개입니다.

```text
C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend
C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\frontend
```

`.env` 파일은 복사하지 않습니다.

## 3. Upstash Redis 만들기

Upstash는 Redis 서버를 직접 설치하지 않고도 Redis를 사용할 수 있게 해주는 서비스입니다.

이 예제에서 Upstash는 필수가 아닙니다. 값을 비워 두면 백엔드는 메모리에만 로그를 저장합니다. 다만 배포 흐름을 익히기 위해 생성해 볼 수 있습니다.

1. Upstash에 로그인합니다.
2. Redis 메뉴로 이동합니다.
3. `Create Database`를 선택합니다.
4. 이름은 예를 들어 `final-frontend-logs`로 입력합니다.
5. 가까운 Region을 선택합니다.
6. Free plan을 선택합니다.
7. 생성 후 REST API 정보를 확인합니다.

복사할 값은 다음 두 가지입니다.

```text
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN
```

이 값은 Render 백엔드 환경변수에 등록합니다. Streamlit 프론트엔드에는 넣지 않습니다.

## 4. Render에 FastAPI 백엔드 배포

Render는 GitHub 저장소에 있는 FastAPI 앱을 웹 서비스로 배포할 수 있습니다.

### 4-1. Render Web Service 생성

1. Render에 로그인합니다.
2. `New`를 누릅니다.
3. `Web Service`를 선택합니다.
4. GitHub 저장소를 연결합니다.
5. 배포할 저장소를 선택합니다.
6. Root Directory가 필요하면 `backend`를 입력합니다.
7. Runtime은 Python을 선택합니다.

### 4-2. Build Command

```text
pip install -r requirements.txt
```

### 4-3. Start Command

```text
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render에서는 포트 번호를 직접 `8000`으로 고정하지 않습니다. Render가 제공하는 `$PORT` 환경변수를 사용해야 합니다.

### 4-4. Render 환경변수

Render 서비스 설정에서 Environment Variables를 등록합니다.

```env
APP_ENV=render
UPSTASH_REDIS_REST_URL=본인 Upstash REST URL
UPSTASH_REDIS_REST_TOKEN=본인 Upstash REST Token
```

Upstash를 아직 만들지 않았다면 두 값은 비워 두어도 예제는 동작합니다.

### 4-5. 백엔드 배포 확인

배포가 끝나면 Render URL이 생성됩니다.

```text
https://서비스이름.onrender.com
```

브라우저에서 아래 주소를 엽니다.

```text
https://서비스이름.onrender.com/health
```

정상이라면 JSON 응답이 보입니다.

## 5. Streamlit Community Cloud에 프론트엔드 배포

### 5-1. Streamlit 앱 생성

1. Streamlit Community Cloud에 로그인합니다.
2. `Create app` 또는 `New app`을 선택합니다.
3. GitHub 저장소를 선택합니다.
4. Branch를 선택합니다.
5. Main file path에 다음 값을 입력합니다.

```text
frontend/app.py
```

저장소 구조가 다르면 실제 `app.py` 위치에 맞게 입력합니다.

### 5-2. Streamlit Secrets 등록

Streamlit Community Cloud의 Secrets 메뉴에 다음 값을 등록합니다.

```toml
API_BASE_URL = "https://서비스이름.onrender.com"
```

주의할 점:

- 로컬 주소 `http://127.0.0.1:8000`을 넣으면 배포 환경에서는 동작하지 않습니다.
- Render에서 받은 실제 URL을 넣어야 합니다.
- 백엔드 전용 key나 token은 Streamlit Secrets에 넣지 않는 것이 원칙입니다.

### 5-3. 프론트엔드 배포 확인

배포가 끝나면 Streamlit 앱 URL이 생성됩니다.

```text
https://앱이름.streamlit.app
```

앱을 열고 다음을 확인합니다.

1. 홈 화면에서 백엔드 연결 성공이 보이는가?
2. Chatbot 화면에서 질문을 보낼 수 있는가?
3. Chat History 화면에서 대화가 보이는가?
4. Service Logs 화면에서 로그가 보이는가?
5. Deployment Check 화면에서 `/health` 호출이 성공하는가?

## 6. 자주 만나는 오류

### Streamlit에서 백엔드 연결 실패

가능한 원인:

```text
API_BASE_URL이 로컬 주소로 남아 있음
Render 백엔드가 아직 깨어나지 않음
Render 배포가 실패함
```

해결 방법:

```text
Streamlit Secrets의 API_BASE_URL을 Render URL로 바꿉니다.
Render의 /health 주소를 브라우저에서 직접 열어 봅니다.
Render Logs에서 오류 메시지를 확인합니다.
```

### Render에서 Application failed to respond

가능한 원인:

```text
Start Command가 잘못됨
$PORT를 사용하지 않음
main.py 위치가 Root Directory와 맞지 않음
```

해결 방법:

```text
Start Command:
uvicorn main:app --host 0.0.0.0 --port $PORT

Root Directory:
backend
```

### ModuleNotFoundError

가능한 원인:

```text
requirements.txt에 필요한 패키지가 없음
Root Directory가 잘못되어 requirements.txt를 찾지 못함
```

해결 방법:

```text
backend/requirements.txt가 있는지 확인합니다.
Render Root Directory가 backend인지 확인합니다.
```

### Upstash Redis 인증 실패

가능한 원인:

```text
REST URL 또는 Token 오타
Render 환경변수 이름 오타
```

확인할 환경변수 이름:

```text
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN
```

## 7. 제출할 내용

배포 실습 후 다음 내용을 정리합니다.

1. Render 백엔드 URL
2. Streamlit Community Cloud URL
3. `/health` 호출 결과 화면 캡처
4. Chatbot 질문/응답 화면 캡처
5. Service Logs 화면 캡처
6. 배포 중 발생한 오류와 해결 과정
7. 03 미니 프로젝트에서 Supabase로 확장할 아이디어
