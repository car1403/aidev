# Supabase Schema Checklist

Supabase SQL Editor에서 스키마를 실행한 뒤 아래 항목을 확인합니다.

## learning_notes

- `id` 컬럼이 기본키입니다.
- `title` 컬럼이 비어 있으면 안 됩니다.
- `content` 컬럼에 학습 메모 내용을 저장할 수 있습니다.
- `created_at` 컬럼으로 생성 시간을 확인할 수 있습니다.

## conversations

- 사용자별 대화 묶음을 저장합니다.
- 한 사용자가 여러 대화를 만들 수 있는 구조입니다.
- 이후 챗봇 서비스에서 “대화 목록” 화면을 만들 때 사용합니다.

## messages

- 하나의 대화 안에 여러 메시지를 저장합니다.
- `role` 컬럼으로 `user`, `assistant`, `system` 같은 메시지 역할을 구분합니다.
- 이후 Streamlit 화면에서 이전 대화를 다시 보여 줄 때 사용합니다.

## service_logs

- API 호출, 오류, 사용자 행동 같은 서비스 로그를 저장합니다.
- 이후 서비스 운영과 디버깅에서 “언제 어떤 일이 있었는지” 확인할 때 사용합니다.

## 오류가 발생했을 때

- `already exists`는 이미 테이블이 있다는 뜻입니다. 학습 중에는 큰 문제가 아닐 수 있습니다.
- `permission denied`는 SQL 실행 권한이나 프로젝트 선택 상태를 확인해야 합니다.
- `Could not find the table`은 Python 코드가 찾는 테이블이 아직 없다는 뜻입니다.
