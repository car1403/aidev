"""Upstash Redis 환경변수 확인 예제.

이 파일은 Redis에 실제로 데이터를 저장하기 전에 `.env` 파일에
필요한 값이 들어 있는지 확인합니다.

초보자는 먼저 환경변수 이름을 정확히 맞추는 연습이 중요합니다.
환경변수 이름이 한 글자라도 다르면 Python 코드는 값을 찾지 못합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# 현재 파일 위치에서 위로 세 번 올라가면 01_supabase-ai-backend 폴더입니다.
# .env 파일은 과정 최상위 폴더에 두는 것이 수업 기준입니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


# load_dotenv는 .env 파일에 적힌 값을 os.environ에서 읽을 수 있게 올려줍니다.
load_dotenv(ENV_PATH)


redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")


print("Upstash Redis 환경변수 확인")
print("-" * 32)
print(f".env 위치: {ENV_PATH}")

if redis_url:
    # URL은 민감 정보는 아니지만, 수업에서는 "설정됨" 정도만 확인해도 충분합니다.
    print("UPSTASH_REDIS_REST_URL: 설정됨")
else:
    print("UPSTASH_REDIS_REST_URL: 없음")

if redis_token:
    # token은 비밀번호와 같으므로 전체 값을 출력하지 않습니다.
    print("UPSTASH_REDIS_REST_TOKEN: 설정됨")
else:
    print("UPSTASH_REDIS_REST_TOKEN: 없음")


if not redis_url or not redis_token:
    print("\n.env 파일에 Upstash Redis 값을 먼저 입력해 주세요.")
    print("예시:")
    print("UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io")
    print("UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token")
else:
    print("\nUpstash Redis 연결 실습을 진행할 준비가 되었습니다.")
