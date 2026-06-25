"""사용자 프로필 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
먼저 "서비스에서 사용자 정보를 어떤 모양으로 관리할지"를 Python dict로 확인합니다.

핵심 아이디어:
- Supabase Auth는 로그인한 사용자의 id를 만들어 줍니다.
- profiles 테이블은 서비스 화면에 필요한 사용자 표시 정보를 저장합니다.
- profiles.id는 Supabase Auth의 user id와 같은 값을 사용하는 것이 일반적입니다.
"""


# Supabase Auth에서 확인한 사용자 id라고 가정합니다.
# 실제 Supabase Auth의 user id는 UUID 형태입니다.
auth_user_id = "00000000-0000-0000-0000-000000000001"


# profiles 테이블에 저장할 사용자 프로필 예시입니다.
# id는 auth.users.id와 연결되는 기준값으로 사용합니다.
profile = {
    "id": auth_user_id,
    "display_name": "수강생 A",
    "preferred_language": "ko",
    "course_level": "beginner",
}


def describe_profile(profile_data: dict) -> str:
    """프로필 데이터를 사람이 읽기 쉬운 설명 문장으로 바꿉니다."""

    return (
        f"{profile_data['display_name']}님은 "
        f"{profile_data['course_level']} 단계 학습자이며, "
        f"기본 언어는 {profile_data['preferred_language']}입니다."
    )


print("프로필 데이터:")
print(profile)

print("\n프로필 설명:")
print(describe_profile(profile))

print("\n저장 위치 기준:")
print("오래 보관할 사용자 프로필은 Supabase profiles 테이블에 저장합니다.")
print("짧게 유지할 임시 상태나 캐시는 Upstash Redis에 저장합니다.")
