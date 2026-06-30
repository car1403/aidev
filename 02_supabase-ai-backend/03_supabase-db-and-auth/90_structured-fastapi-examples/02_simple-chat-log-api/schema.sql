create table if not exists ex90_simple_chat_logs (
  id uuid primary key default gen_random_uuid(),
  user_message text not null,
  assistant_message text,
  provider text not null default 'mock',
  model text,
  actual_api_called boolean not null default false,
  status text not null default 'success',
  error_message text,
  created_at timestamptz not null default now()
);
