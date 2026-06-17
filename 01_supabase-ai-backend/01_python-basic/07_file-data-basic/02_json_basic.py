"""JSON 파일 저장과 읽기 예제입니다.

JSON은 데이터를 저장하거나 API로 주고받을 때 자주 사용하는 형식입니다.
Python의 딕셔너리와 리스트는 JSON 형식으로 변환해 파일에 저장할 수 있습니다.
"""

import json
from pathlib import Path

# 데이터를 저장할 data 폴더를 준비합니다.
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# 딕셔너리는 key와 value로 구성된 데이터입니다.
# JSON으로 저장하기 좋은 형태입니다.
student = {
    "name": "Jean",
    "score": 95,
    "passed": True,
}

# 저장할 파일 경로를 정합니다.
file_path = data_dir / "student.json"

# json.dumps()는 Python 딕셔너리를 JSON 문자열로 바꿉니다.
# ensure_ascii=False는 한글을 유니코드 코드가 아니라 실제 글자로 저장하게 합니다.
# indent=2는 JSON 파일을 사람이 읽기 좋게 들여쓰기합니다.
file_path.write_text(json.dumps(student, ensure_ascii=False, indent=2), encoding="utf-8")

# 파일에서 읽어온 JSON 문자열을 json.loads()로 다시 Python 딕셔너리로 바꿉니다.
loaded = json.loads(file_path.read_text(encoding="utf-8"))
print("읽어온 데이터:", loaded["name"])
