create table if not exists mini_qa_items (
  id uuid primary key default gen_random_uuid(),
  user_id text,
  question text not null,
  answer text not null,
  model text not null default 'mock-teacher',
  created_at timestamptz not null default now()
);

create table if not exists mini_service_logs (
  id uuid primary key default gen_random_uuid(),
  event_type text not null,
  message text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_mini_qa_items_user_id on mini_qa_items(user_id);
create index if not exists idx_mini_qa_items_created_at on mini_qa_items(created_at);
create index if not exists idx_mini_service_logs_event_type on mini_service_logs(event_type);
create index if not exists idx_mini_service_logs_created_at on mini_service_logs(created_at);

-- RLS는 Auth를 적용하는 단계에서 활성화합니다.
-- 초보 수업에서는 먼저 서버에서 service role key로 저장 흐름을 확인합니다.
