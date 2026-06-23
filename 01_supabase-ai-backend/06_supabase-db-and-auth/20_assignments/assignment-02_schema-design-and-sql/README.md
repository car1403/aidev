# Assignment 02 - Supabase 테이블 설계와 SQL 작성

AI 서비스에서 사용할 데이터를 Supabase 테이블로 설계하는 과제입니다.

## 목표

- RDBMS 테이블 구조를 서비스 기능과 연결해서 설명할 수 있습니다.
- 테이블, 컬럼, 기본키, 외래키의 역할을 구분할 수 있습니다.
- 대화 이력과 서비스 로그를 저장하기 위한 최소 테이블 구조를 설계할 수 있습니다.

## 제출물

아래 내용을 포함한 설계 문서를 작성합니다.

```text
1. learning_notes 테이블 목적
2. conversations 테이블 목적
3. messages 테이블 목적
4. service_logs 테이블 목적
5. 각 테이블의 컬럼 목록
6. primary key
7. 테이블 간 관계
8. 예시 데이터 1개 이상
9. SQL 실행 결과 요약
```

## 참고 SQL

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql
```

## 설계 예시 형식

```text
테이블명: messages
목적: 대화 안에서 오간 사용자 메시지와 AI 메시지를 저장한다.
주요 컬럼:
- id: 메시지 고유 ID
- conversation_id: 어떤 대화에 속한 메시지인지 연결
- role: user 또는 assistant
- content: 메시지 내용
- created_at: 생성 시간
```

## 확인 기준

- 각 테이블의 목적이 서비스 기능과 연결되어 있습니다.
- `messages`가 `conversations`에 속한다는 관계를 설명했습니다.
- 로그 데이터와 사용자 대화 데이터를 구분했습니다.
