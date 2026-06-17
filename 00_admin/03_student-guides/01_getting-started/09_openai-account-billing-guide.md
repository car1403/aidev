# 09. OpenAI Account and Billing Guide

이 문서는 OpenAI 계정, ChatGPT 구독, API 결제, Codex 사용 가능 여부를 초보자도 이해할 수 있도록 정리한 안내입니다.

중요: 결제 정보는 개인정보입니다. 수업 중 카드 번호, 결제 화면, API Key를 공유하지 않습니다.

## 1. 가장 먼저 구분해야 하는 것

OpenAI를 사용할 때는 크게 두 가지 결제 흐름을 구분해야 합니다.

| 구분 | 주로 사용하는 곳 | 예시 |
| --- | --- | --- |
| ChatGPT 계정 결제 | chatgpt.com, ChatGPT 앱, Codex app, VS Code Codex extension | Free, Go, Plus, Pro, Business 등 |
| OpenAI API Platform 결제 | Python 코드, FastAPI 서버, 자동화 스크립트, 외부 앱 연동 | API key, usage, prepaid billing |

두 결제는 서로 연결되어 보일 수 있지만, 실제 결제와 사용량 관리 화면이 다를 수 있습니다.

## 2. 꼭 기억해야 할 핵심

아래 내용을 반드시 기억합니다.

```text
Codex app 사용을 위한 ChatGPT 계정 결제와
OpenAI API key 연동을 위한 API 결제는 별개의 결제입니다.
```

즉, Codex app에서 ChatGPT 계정으로 로그인해 사용하는 것과, OpenAI API key를 발급받아 Python 코드나 서비스에 연결하는 것은 결제 방식이 다를 수 있습니다.

중요한 예시:

```text
ChatGPT Plus 또는 Pro를 결제했다고 해서 OpenAI API 사용량이 자동으로 무료가 되는 것은 아닙니다.
OpenAI API 결제 수단을 등록했다고 해서 ChatGPT Plus 또는 Pro가 자동으로 구독되는 것도 아닙니다.
```

## 3. Codex app 사용 결제와 API key 결제 비교

| 항목 | Codex app / VS Code Codex extension | OpenAI API key 연동 |
| --- | --- | --- |
| 주 사용 위치 | Codex app, VS Code Codex 패널 | Python 코드, FastAPI, 자동화 스크립트 |
| 로그인 방식 | ChatGPT 계정 로그인 중심 | API key 사용 |
| 결제 성격 | ChatGPT 플랜 또는 Codex 포함 사용량과 관련 | API 사용량 또는 크레딧 결제와 관련 |
| 사용 예 | 코드 설명, 수정, 리뷰, 프로젝트 작업 | 코드에서 모델 API 직접 호출 |
| 비용 확인 위치 | ChatGPT Billing | OpenAI Platform Billing 또는 Usage |
| 초보자 주의점 | 현재 플랜에서 Codex 사용 가능 여부 확인 | API key 유출 시 비용 발생 가능 |

수업에서 Codex app만 사용하는 경우에는 API key 결제가 필요하지 않을 수 있습니다. 하지만 Python 코드에서 OpenAI API를 직접 호출하거나, FastAPI 서버에서 AI 모델 API를 연결하는 경우에는 API key와 API 결제 설정이 필요할 수 있습니다.

## 4. Codex와 ChatGPT 플랜

공식 안내 기준으로 Codex는 Free, Go, Plus, Pro, Business, Edu, Enterprise 등 여러 ChatGPT 플랜에서 제공될 수 있습니다. 다만 사용 한도, 기능 제공 방식, 플랜별 조건은 시점에 따라 달라질 수 있습니다.

수업에서는 아래처럼 안내합니다.

```text
1. 본인의 ChatGPT 계정으로 Codex 사용 가능 여부를 확인합니다.
2. 유료 플랜이 필요한 경우 강사 또는 기관 안내를 따릅니다.
3. 개인 결제를 강제로 진행하지 않습니다.
4. 사용 한도와 가격은 수업 시점의 공식 결제 화면을 기준으로 확인합니다.
```

## 5. ChatGPT 구독 결제 관리

ChatGPT 웹 구독은 보통 ChatGPT 설정의 Billing 메뉴에서 관리합니다.

일반 흐름:

```text
1. chatgpt.com 접속
2. 로그인
3. 프로필 또는 Settings 열기
4. Billing 선택
5. 구독, 결제 수단, 청구 내역 확인
```

이 화면에서는 주로 아래 내용을 확인합니다.

```text
현재 ChatGPT 플랜
월 구독 여부
자동 갱신 여부
결제 카드
청구 내역
플랜 변경 또는 해지
```

## 6. OpenAI API Platform 결제

Python 코드에서 OpenAI API를 직접 호출하려면 API key와 API Platform 결제 설정이 필요할 수 있습니다.

API 결제 흐름은 ChatGPT 구독과 다를 수 있습니다.

일반 흐름:

```text
1. platform.openai.com 접속
2. 로그인
3. Billing 또는 Usage 확인
4. 결제 수단 또는 prepaid billing 설정
5. API key 생성
6. .env 파일에 API key 저장
```

주의:

```text
API key를 코드에 직접 적지 않습니다.
API key를 README에 적지 않습니다.
API key를 GitHub에 올리지 않습니다.
API key는 .env 파일에만 저장합니다.
```

예시:

```env
OPENAI_API_KEY=your-openai-api-key
```

`.env.example`에는 실제 키가 아닌 예시 값만 적습니다.

```env
OPENAI_API_KEY=your-openai-api-key
```

## 7. 카드 결제 전에 확인할 것

카드 결제를 진행하기 전에 아래 항목을 확인합니다.

```text
[ ] 내가 결제하려는 것이 ChatGPT 플랜인지 OpenAI API 크레딧인지 확인했다.
[ ] Codex app 사용 결제와 API key 연동 결제가 별개라는 것을 이해했다.
[ ] 개인 계정인지 학교/회사/팀 계정인지 확인했다.
[ ] 월 구독인지 사용량 기반 결제인지 확인했다.
[ ] 포함 사용량과 초과 사용 시 과금 방식을 확인했다.
[ ] 결제 통화와 세금 포함 여부를 확인했다.
[ ] 자동 갱신 여부를 확인했다.
[ ] 환불 또는 해지 정책을 확인했다.
[ ] API key를 사용할 경우 사용량 한도 설정 가능 여부를 확인했다.
```

학생 개인 카드로 결제해야 하는 상황이라면, 결제 전에 강사에게 먼저 확인하는 것이 좋습니다.

## 8. 수업에서 결제 화면을 다룰 때 주의할 점

수업에서는 결제 수단을 공개하지 않습니다.

```text
카드 번호를 화면 공유하지 않습니다.
결제 완료 화면을 전체 화면으로 공유하지 않습니다.
API key를 채팅창에 붙여넣지 않습니다.
.env 파일을 제출하지 않습니다.
학교/회사 계정은 관리자 정책을 따릅니다.
유료 기능은 승인 후 사용합니다.
```

## 9. 수업에서 권장하는 운영 방식

강의에서는 가능하면 아래 방식이 안전합니다.

```text
1. 무료로 가능한 범위에서 먼저 실습합니다.
2. 유료 기능이 필요한 경우 강사가 데모 계정 또는 기관 계정을 준비합니다.
3. 학생 개인 결제가 필요한 경우 사전에 별도로 안내합니다.
4. API 사용량이 발생하는 실습은 입력 데이터와 실행 횟수를 작게 제한합니다.
5. 비용이 발생할 수 있는 자동 반복 실행은 하지 않습니다.
```

## 10. 자주 묻는 질문

### ChatGPT Plus를 결제하면 API도 무료인가요?

아닙니다. ChatGPT 구독과 OpenAI API 사용량 결제는 별도로 이해해야 합니다. API를 코드에서 직접 호출하려면 API Platform의 결제 또는 사용량 설정을 별도로 확인해야 할 수 있습니다.

### OpenAI API 결제를 하면 ChatGPT Plus가 되나요?

아닙니다. OpenAI API 결제 수단을 등록했다고 해서 ChatGPT Plus 또는 Pro 같은 ChatGPT 유료 플랜이 자동으로 구독되는 것은 아닙니다.

### Codex app을 쓰려면 반드시 API key가 필요한가요?

항상 그런 것은 아닙니다. Codex app이나 VS Code Codex extension은 ChatGPT 계정 로그인으로 사용할 수 있는 경우가 있습니다. 다만 CLI, 자동화, API 기반 사용에서는 API key가 필요할 수 있습니다.

### Python 코드에서 OpenAI 모델을 호출하려면 무엇이 필요한가요?

보통 아래가 필요합니다.

```text
OpenAI 계정
API key
API 결제 또는 크레딧 설정
.env 파일
openai Python 패키지
```

### 카드 결제를 했는데 Codex가 안 보이면 어떻게 하나요?

아래를 확인합니다.

```text
1. 올바른 계정으로 로그인했는가?
2. 결제한 계정과 Codex에 로그인한 계정이 같은가?
3. 결제한 항목이 ChatGPT 플랜인지 API 크레딧인지 확인했는가?
4. VS Code 또는 Codex app을 재시작했는가?
5. 학교/회사 계정이라면 관리자가 Codex 사용을 허용했는가?
```

### API key를 어디에 넣나요?

`.env` 파일에 넣습니다.

예시:

```env
OPENAI_API_KEY=your-openai-api-key
```

API key는 비밀번호처럼 다룹니다. README, 과제 문서, 발표 자료, GitHub 저장소, 화면 캡처에 노출하지 않습니다.

## 11. 결제 관련 학생 보안 체크리스트

아래 항목을 지킵니다.

```text
[ ] 카드 번호를 화면 공유하지 않는다.
[ ] API key를 채팅창에 붙여넣지 않는다.
[ ] .env 파일을 제출하지 않는다.
[ ] 결제 화면은 본인만 확인한다.
[ ] 학교/회사 계정은 관리자 정책을 따른다.
[ ] 유료 기능은 승인 후 사용한다.
[ ] Codex app 결제와 API key 결제가 별개라는 것을 이해한다.
```

## 12. 공식 참고 링크

```text
Codex with ChatGPT plan:
https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

Codex pricing:
https://developers.openai.com/codex/pricing

Codex authentication:
https://developers.openai.com/codex/auth

ChatGPT billing settings:
https://help.openai.com/en/articles/9039756-managing-billing-settings-on-chatgpt-web-and-platform

OpenAI multi-currency billing:
https://help.openai.com/en/articles/10421635-multicurrency-billing

API prepaid billing:
https://help.openai.com/en/articles/8264644-how-can-i-set-up-prepaid-billing

OpenAI billing and payment:
https://help.openai.com/en/articles/20001216-billing-payment
```

## 13. 최종 체크리스트

수업 전에 아래 항목을 확인합니다.

```text
[ ] OpenAI 계정에 로그인할 수 있다.
[ ] ChatGPT 구독 결제와 OpenAI API 결제가 다르다는 것을 이해했다.
[ ] Codex app 사용 결제와 API key 연동 결제가 별개라는 것을 이해했다.
[ ] 카드 결제 전 자동 갱신, 포함 사용량, 초과 과금 여부를 확인해야 한다는 것을 이해했다.
[ ] API key는 .env에만 저장해야 한다는 것을 이해했다.
[ ] API key를 GitHub에 올리면 안 된다는 것을 이해했다.
[ ] 결제 화면과 카드 정보는 공유하지 않는다는 것을 이해했다.
```
