create table if not exists ex90_user_chat_logs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  user_message text not null,
  assistant_message text,
  provider text not null default 'mock',
  model text,
  actual_api_called boolean not null default false,
  cached boolean not null default false,
  status text not null default 'success',
  error_message text,
  created_at timestamptz not null default now()
);

alter table ex90_user_chat_logs enable row level security;

drop policy if exists "ex90 chat logs select own" on ex90_user_chat_logs;
create policy "ex90 chat logs select own"
on ex90_user_chat_logs
for select
using (auth.uid() = user_id);

drop policy if exists "ex90 chat logs insert own" on ex90_user_chat_logs;
create policy "ex90 chat logs insert own"
on ex90_user_chat_logs
for insert
with check (auth.uid() = user_id);
