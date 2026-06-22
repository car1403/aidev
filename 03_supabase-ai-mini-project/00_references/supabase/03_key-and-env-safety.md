# 03 Key And Env Safety

Supabase 프로젝트에는 여러 key가 있습니다.

## anon key

프론트엔드나 일반 클라이언트에서 사용할 수 있는 key입니다.

하지만 RLS 정책이 없으면 위험할 수 있습니다.

## service role key

강한 권한을 가진 서버용 key입니다.

절대 아래 위치에 넣지 않습니다.

```text
Streamlit app.py
README.md
GitHub 저장소
발표 자료
브라우저에서 실행되는 코드
```

##.env

실제 key는 `.env` 파일에 넣습니다.

```text
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
```

##.env.example

공유용 예시 파일입니다.

```text
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your-anon-key
```

## 제출 전 확인

- `.env` 제출 금지
- 실제 key가 코드에 있는지 검색
- 발표 캡처에 key가 보이지 않는지 확인
- service role key가 노출되면 재발급

