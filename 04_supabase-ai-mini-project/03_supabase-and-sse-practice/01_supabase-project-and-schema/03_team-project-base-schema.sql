-- 04_supabase-ai-mini-project 팀 프로젝트 기본 Supabase 테이블 예시입니다.
-- Supabase Dashboard의 SQL Editor에 붙여 넣고 실행할 수 있습니다.
-- 팀 프로젝트 주제에 맞게 컬럼 이름과 테이블 이름을 조정해도 됩니다.

create table if not exists profiles (
  id uuid primary key default gen_random_uuid(),
  email text not null,
  display_name text,
  created_at timestamptz not null default now()
);

create table if not exists conversations (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id),
  title text not null default '새 대화',
  created_at timestamptz not null default now()
);

create table if not exists messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references conversations(id),
  role text not null check (role in ('user', 'assistant', 'system')),
  content text not null,
  created_at timestamptz not null default now()
);

create table if not exists service_logs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id),
  action text not null,
  status text not null default 'success',
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists feedbacks (
  id uuid primary key default gen_random_uuid(),
  message_id uuid references messages(id),
  rating integer check (rating between 1 and 5),
  comment text,
  created_at timestamptz not null default now()
);

create index if not exists idx_conversations_user_id on conversations(user_id);
create index if not exists idx_messages_conversation_id on messages(conversation_id);
create index if not exists idx_service_logs_created_at on service_logs(created_at);
create index if not exists idx_feedbacks_message_id on feedbacks(message_id);
