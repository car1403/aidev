-- 05_backend-mini-service-practice
-- AI 질문 응답 백엔드 미니 서비스용 Supabase 스키마입니다.
--
-- 실행 위치:
-- Supabase Dashboard -> SQL Editor -> New query
--
-- 이 SQL은 두 개의 테이블을 만듭니다.
-- 1. mini_questions: 사용자 질문과 AI 답변 저장
-- 2. mini_service_logs: API 처리 로그 저장

create table if not exists mini_questions (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  question text not null,
  answer text not null,
  provider text not null default 'gemini',
  model text not null default 'gemini-2.5-flash-lite',
  actual_api_called boolean not null default false,
  llm_call_mode text not null default 'mock-first',
  created_at timestamptz not null default now()
);

create table if not exists mini_service_logs (
  id uuid primary key default gen_random_uuid(),
  event_type text not null,
  message text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

-- 사용자별 질문 목록을 빠르게 조회하기 위한 인덱스입니다.
create index if not exists idx_mini_questions_user_id
on mini_questions(user_id);

-- 최신 질문부터 정렬해서 조회하기 위한 인덱스입니다.
create index if not exists idx_mini_questions_created_at
on mini_questions(created_at desc);

-- 로그 종류별로 조회하기 위한 인덱스입니다.
create index if not exists idx_mini_service_logs_event_type
on mini_service_logs(event_type);

-- 최신 로그부터 정렬해서 조회하기 위한 인덱스입니다.
create index if not exists idx_mini_service_logs_created_at
on mini_service_logs(created_at desc);

-- RLS는 Auth를 적용하는 단계에서 활성화합니다.
-- 이번 미니 서비스에서는 먼저 백엔드 서버에서 저장과 조회 흐름을 확인합니다.
-- 이후 사용자 인증을 붙일 때 user_id 기준 정책을 추가할 수 있습니다.
