-- 테스트용 샘플 데이터입니다.
-- 실제 프로젝트 데이터가 아니라 화면과 API 연결을 확인하기 위한 데이터입니다.

insert into profiles (email, display_name)
values ('demo@example.com', 'Demo User')
on conflict do nothing;

insert into service_logs (action, status, metadata)
values
  ('app_start', 'success', '{"source": "seed"}'::jsonb),
  ('chat_request', 'success', '{"model": "gemini-2.5-flash-lite"}'::jsonb),
  ('feedback_saved', 'success', '{"rating": 5}'::jsonb);
