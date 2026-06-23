# Assignment 03 - 대화 이력 테이블 설계

AI 챗봇 서비스에서 대화 묶음과 메시지를 저장하는 구조를 설계하는 과제입니다.

## 목표

- `conversations`와 `messages`를 분리하는 이유를 설명할 수 있습니다.
- 메시지 역할 `user`, `assistant`, `system`을 구분할 수 있습니다.
- 특정 대화의 메시지를 시간 순서로 조회하는 구조를 설계할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. conversations 테이블 목적
2. messages 테이블 목적
3. conversations 컬럼 목록
4. messages 컬럼 목록
5. 두 테이블의 관계
6. role 값의 종류와 의미
7. 특정 conversation_id의 메시지를 시간순으로 조회하는 방법
8. 예시 데이터
```

## 관계 설명 예시

```text
conversations.id
-> messages.conversation_id
```

## 확인 기준

- 대화 묶음과 개별 메시지를 분리했습니다.
- `messages.conversation_id`의 역할을 설명했습니다.
- 대화 이력이 Supabase에 저장되어야 하는 이유를 설명했습니다.

## 정리 질문

- 이전 대화 목록 화면은 어떤 테이블을 조회해야 만들 수 있나요?
- 특정 대화 상세 화면은 어떤 테이블을 조회해야 만들 수 있나요?
