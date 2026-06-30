create table if not exists ex90_profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table ex90_profiles enable row level security;

drop policy if exists "ex90 profiles select own" on ex90_profiles;
create policy "ex90 profiles select own"
on ex90_profiles
for select
using (auth.uid() = id);

drop policy if exists "ex90 profiles insert own" on ex90_profiles;
create policy "ex90 profiles insert own"
on ex90_profiles
for insert
with check (auth.uid() = id);

drop policy if exists "ex90 profiles update own" on ex90_profiles;
create policy "ex90 profiles update own"
on ex90_profiles
for update
using (auth.uid() = id)
with check (auth.uid() = id);
