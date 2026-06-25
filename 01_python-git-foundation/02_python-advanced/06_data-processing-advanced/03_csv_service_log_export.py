"""서비스 로그를 CSV 파일로 내보내는 예제입니다."""

import csv
from pathlib import Path

# data 폴더를 준비합니다.
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# 서비스 로그 예시입니다.
# 실제 과정 후반에서는 Supabase의 service_logs 테이블과 연결됩니다.
service_logs = [
    {"event_type": "chat.request", "message": "사용자 질문 수신", "status": "success"},
    {"event_type": "chat.response", "message": "AI 응답 생성", "status": "success"},
    {"event_type": "cache.miss", "message": "캐시 데이터 없음", "status": "warning"},
]

# CSV 파일 경로를 만듭니다.
csv_path = data_dir / "service_logs.csv"

# newline=""은 Windows에서 CSV 줄바꿈이 중복되는 문제를 줄이기 위해 사용합니다.
with csv_path.open("w", encoding="utf-8", newline="") as file:
    # CSV 컬럼 이름을 정합니다.
    fieldnames = ["event_type", "message", "status"]

    # DictWriter는 dict 목록을 CSV로 저장할 때 편리합니다.
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 첫 줄에 컬럼 이름을 씁니다.
    writer.writeheader()

    # 로그 목록을 CSV에 씁니다.
    writer.writerows(service_logs)

print("CSV 저장 파일:", csv_path)
print("로그 개수:", len(service_logs))
