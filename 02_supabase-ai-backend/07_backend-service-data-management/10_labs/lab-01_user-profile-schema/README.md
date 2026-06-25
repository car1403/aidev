# Lab 01 - 사용자 프로필 데이터 구조

이 실습은 Supabase에 접속하지 않고 사용자 프로필 데이터 구조를 먼저 이해합니다.

## 목표

- Supabase Auth의 사용자 ID와 `profiles` 테이블의 관계를 설명할 수 있습니다.
- `display_name`, `preferred_language`, `course_level`의 역할을 구분할 수 있습니다.
- 사용자 프로필은 장기 보관 데이터이므로 Supabase에 저장해야 한다는 기준을 이해합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\01_user-profile-data\01_profile_schema_example.py
```

## 확인 기준

- 프로필 dict가 출력됩니다.
- `id`가 Auth 사용자 ID와 연결된다는 설명을 이해합니다.
- 프로필 데이터는 Redis가 아니라 Supabase에 저장하는 것이 적절하다고 설명할 수 있습니다.

## 정리 질문

- 이메일은 Auth에 있는데 `display_name`을 따로 저장하는 이유는 무엇인가요?
- `preferred_language`는 AI 응답 개인화에 어떻게 활용할 수 있나요?
