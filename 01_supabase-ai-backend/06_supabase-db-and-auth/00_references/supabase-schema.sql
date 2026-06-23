-- Supabase schema for 06_supabase-db-and-auth.
-- Run this file in Supabase Dashboard > SQL Editor.
-- The "create table if not exists" statements are safe to run more than once.

create table if not exists learning_notes (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  content text not null,
  created_at timestamptz not null default now()
);

create table if not exists profiles (
  id uuid primary key,
  display_name text not null,
  created_at timestamptz not null default now()
);

create table if not exists conversations (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  title text not null,
  created_at timestamptz not null default now()
);

create table if not exists messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references conversations(id) on delete cascade,
  role text not null check (role in ('user', 'assistant', 'system')),
  content text not null,
  created_at timestamptz not null default now()
);

create table if not exists service_logs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  event_type text not null,
  message text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

-- Compatibility fix for older practice tables.
alter table service_logs add column if not exists user_id uuid;

create index if not exists idx_conversations_user_id on conversations(user_id);
create index if not exists idx_messages_conversation_id on messages(conversation_id);
create index if not exists idx_service_logs_user_id on service_logs(user_id);
create index if not exists idx_service_logs_event_type on service_logs(event_type);
create index if not exists idx_service_logs_created_at on service_logs(created_at);

-- RLS examples are reviewed after the Auth lesson.
-- Before enabling RLS, define table purpose and user access scope first.
--
-- alter table profiles enable row level security;
--
-- create policy "users can read own profile"
-- on profiles
-- for select
-- using (auth.uid() = id);
