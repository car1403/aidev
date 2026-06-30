-- 99_final-backend-project solution
-- 상품 설명 생성 API에서 사용하는 예시 테이블입니다.
-- Supabase SQL Editor에서 실행합니다.

create table if not exists final_products (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  description text not null,
  target_audience text not null default '초보자',
  ai_description text,
  created_at timestamptz not null default now()
);

create table if not exists final_service_logs (
  id uuid primary key default gen_random_uuid(),
  action text not null,
  status text not null,
  detail text,
  created_at timestamptz not null default now()
);
