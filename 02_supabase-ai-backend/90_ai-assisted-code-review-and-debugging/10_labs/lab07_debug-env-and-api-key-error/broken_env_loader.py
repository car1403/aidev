"""환경변수 디버깅 실습용 예제.

이 파일은 일부러 잘못된 변수명을 사용합니다.
실제 key를 출력하는 습관이 왜 위험한지도 함께 점검합니다.
"""

import os

from dotenv import load_dotenv


load_dotenv()

# 리뷰 포인트:
# 실제 .env에서는 SUPABASE_URL을 사용하는데 여기서는 이름이 다릅니다.
supabase_url = os.getenv("SUPABASE_PROJECT_URL")

# 리뷰 포인트:
# 실제 key를 그대로 print하면 화면 공유, 로그, 터미널 기록에 노출될 수 있습니다.
openai_key = os.getenv("OPENAI_API_KEY")

print("Supabase URL:", supabase_url)
print("OpenAI key:", openai_key)

if not supabase_url:
    raise RuntimeError("Supabase URL이 없습니다. 변수명을 확인해 주세요.")

