# 09. Codex Account And Billing Troubleshooting

Codex, ChatGPT 계정, OpenAI API 결제, API Key 사용 중 자주 만나는 문제를 정리한 문서입니다.

이 문서는 결제를 권장하는 문서가 아닙니다. 직접 **어떤 계정이 필요한지**, **어떤 결제가 어떤 상황에서 필요한지**, **API Key를 어떻게 안전하게 다루는지** 이해하도록 돕는 문서입니다.

## 1. Codex에 로그인이 되지 않을 때

먼저 아래를 확인합니다.

```text
1. 인터넷 연결이 정상인가?
2. ChatGPT 계정 이메일과 비밀번호가 맞는가?
3. 브라우저에서 ChatGPT에 먼저 로그인되는가?
4. 학교/회사 네트워크에서 로그인이 차단된 것은 아닌가?
5. Codex 앱 또는 VS Code를 완전히 종료한 뒤 다시 실행했는가?
```

브라우저에서는 로그인되는데 Codex에서만 안 된다면, Codex 앱을 재실행하거나 VS Code를 재시작합니다.

## 2. Codex가 VS Code에 보이지 않을 때

아래 순서로 확인합니다.

```text
1. VS Code Extensions에서 Codex가 설치되어 있는지 확인한다.
2. VS Code를 재시작한다.
3. 왼쪽 사이드바에 Codex 아이콘이 있는지 확인한다.
4. 명령 팔레트에서 Codex 관련 명령을 검색한다.
```

명령 팔레트:

```text
Ctrl + Shift + P
```

검색어 예:

```text
Codex
```

## 3. ChatGPT 결제와 API 결제를 혼동할 때

가장 많이 헷갈리는 부분입니다.

```text
ChatGPT 구독:
ChatGPT 웹, 앱, Codex 같은 ChatGPT 계정 기반 기능을 사용하는 결제입니다.

OpenAI API Platform 결제:
Python 코드에서 OpenAI API를 호출할 때 사용하는 결제입니다.
API Key를 발급하고 사용량에 따라 비용이 발생할 수 있습니다.
```

즉, ChatGPT Plus를 사용한다고 해서 API 비용이 자동으로 포함되는 것은 아닙니다. 반대로 API 결제를 설정했다고 해서 ChatGPT 구독이 자동으로 생기는 것도 아닙니다.

## 4. API Key가 없다고 나올 때

오류 예:

```text
OPENAI_API_KEY is not set
API key missing
AuthenticationError
```

확인 순서:

```text
1. 이 실습이 OpenAI API Key를 사용하는 실습인지 확인한다.
2..env 파일을 만들었는지 확인한다.
3..env 파일 안에 OPENAI_API_KEY 값이 있는지 확인한다.
4..env 파일이 현재 실행 폴더 기준으로 읽히는 위치에 있는지 확인한다.
5. API Key 앞뒤에 따옴표나 공백이 잘못 들어가지 않았는지 확인한다.
```

예:

```text
OPENAI_API_KEY=sk-...
```

API Key는 절대로 GitHub에 올리면 안 됩니다.

## 5. 결제 카드 등록이 필요한지 헷갈릴 때

수업 중 개인 결제가 필요한 실습은 별도로 안내합니다.

먼저 아래를 구분합니다.

```text
1. Codex 사용을 위한 ChatGPT 계정 로그인이 필요한가?
2. Python 코드에서 OpenAI API를 호출하는 실습인가?
3. 수업에서 제공한 공용 키 또는 테스트 환경을 사용하는가?
4. 개인 API Key가 필요한 실습인가?
```

개인 결제가 필요한지 불확실하면 결제를 먼저 진행하지 말고 진행자에게 확인합니다.

## 6. 결제 수단이 거절될 때

아래 원인을 확인합니다.

```text
1. 카드 해외 결제 또는 온라인 결제가 가능한가?
2. 카드 한도나 잔액이 충분한가?
3. 카드사 보안 인증이 필요한가?
4. OpenAI 계정의 국가/지역과 결제 수단 정보가 일치하는가?
5. 일시 승인 금액이 표시되었지만 실제 청구가 아닌 것은 아닌가?
```

지역과 상품에 따라 지원되는 결제 수단은 달라질 수 있습니다. 결제 화면에 표시되는 최신 안내를 기준으로 확인합니다.

## 7. 사용량과 비용이 걱정될 때

API를 사용하는 수업에서는 아래 원칙을 지킵니다.

```text
1. 불필요하게 반복 실행하지 않는다.
2. 테스트 질문은 짧게 작성한다.
3. 같은 요청을 여러 번 실행하기 전에 코드 오류를 먼저 확인한다.
4. 사용량 대시보드를 확인한다.
5. 수업에서 지정한 모델과 설정을 사용한다.
```

초보자는 코드가 멈춘 것 같다고 계속 실행 버튼을 누르기 쉽습니다. API 호출 실습에서는 실행 횟수도 비용과 연결될 수 있으므로 결과를 기다린 뒤 판단합니다.

## 8. 안내 문장 예시

수업 진행에서는 아래처럼 안내하면 혼동을 줄일 수 있습니다.

```text
오늘은 Codex 설치와 로그인까지만 확인합니다. 결제는 지금 바로 진행하지 않습니다.
```

```text
ChatGPT 구독과 API 결제는 서로 다릅니다. API Key가 필요한 실습은 별도로 안내하겠습니다.
```

```text
API Key는 비밀번호와 같습니다. 화면 공유나 GitHub 업로드 때 노출되지 않도록 주의합니다.
```

## 9. 공식 문서 확인

계정, 결제, 지원 범위는 시간이 지나며 바뀔 수 있습니다. 최종 기준은 OpenAI 공식 문서를 확인합니다.

```text
Codex App:
https://developers.openai.com/codex/app

Codex on Windows:
https://developers.openai.com/codex/windows

Codex in IDE:
https://developers.openai.com/codex/ide

Codex with ChatGPT plan:
https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

ChatGPT and Platform billing:
https://help.openai.com/en/articles/9039756-managing-billing-settings-on-chatgpt-web-and-platform

API prepaid billing:
https://help.openai.com/en/articles/8264644-how-can-i-set-up-prepaid-billing
```
