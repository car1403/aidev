# Lab 03. Session State and Token

## 목표

로그인 token 저장과 Authorization header 구성을 점검합니다.

## 확인할 것

- `st.session_state["token"]`을 사용하기 전에 초기화했는가?
- 로그인 성공 후 token을 저장하는가?
- 보호된 API 호출 시 `Authorization: Bearer ...` header를 보내는가?
- 화면에 token 전체를 출력하지 않는가?
- 로그아웃 시 token을 삭제하는가?

## 질문 예시

```text
로그인 후 보호된 API 호출이 실패합니다.
token 값은 보안상 ***로 가렸습니다.
session_state 초기화, token 저장, Authorization header 중 무엇을 먼저 확인해야 하나요?
```
