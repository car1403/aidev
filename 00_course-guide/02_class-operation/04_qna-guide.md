# 04. Q&A Guide

초보자 수업에서 자주 나오는 질문과 답변 방향입니다.

## Python 관련

### Python이 왜 필요한가요?

FastAPI, Streamlit, AI API 호출 예제를 실행하기 위해 필요합니다.

###.venv는 왜 매번 켜야 하나요?

현재 과정에서 사용할 패키지 환경을 선택하는 과정입니다. `.venv`를 켜지 않으면 패키지를 설치했는데도 못 찾는 경우가 생깁니다.

## VS Code 관련

### README.md는 왜 이상한 글자로 보이나요?

원본 Markdown을 보고 있기 때문입니다. `Ctrl + Shift + V`로 Preview를 열면 보기 좋게 보입니다.

### 파일은 어디에서 열어야 하나요?

항상 `C:\aidev` 폴더를 VS Code로 열고 시작합니다.

## Supabase 관련

### anon key와 service role key는 뭐가 다른가요?

```text
anon key:
제한된 권한으로 사용하는 공개 가능한 키입니다. RLS와 함께 사용해야 안전합니다.

service role key:
강한 권한을 가진 서버용 키입니다. Streamlit 화면에 넣으면 안 됩니다.
```

## Docker 관련

### 왜 02~04에서는 Docker를 안 쓰나요?

초보자 단계에서는 Python, API, 화면, Supabase 연결을 먼저 익히는 것이 중요합니다. Docker는 05부터 시작하고, Docker Compose와 배포는 07에서 본격적으로 다룹니다.

## SSE 관련

### SSE는 Supabase 기능인가요?

아닙니다.

```text
SSE:
서버가 응답을 실시간으로 화면에 보내는 통신 방식

Supabase:
최종 메시지와 로그를 저장하는 데이터 저장소
```
