"""텍스트 파일 저장과 읽기 예제입니다.

프로그램이 종료되어도 데이터를 남기고 싶을 때 파일을 사용합니다.
이 예제는 `data/memo.txt` 파일을 만들고, 글자를 저장한 뒤 다시 읽어옵니다.
"""

from pathlib import Path

# Path는 파일과 폴더 경로를 다룰 때 사용하는 표준 라이브러리 도구입니다.
# "data"라는 폴더 경로를 Path 객체로 만듭니다.
data_dir = Path("data")

# mkdir()은 폴더를 만드는 함수입니다.
# exist_ok=True는 폴더가 이미 있어도 오류를 내지 말라는 뜻입니다.
data_dir.mkdir(exist_ok=True)

# / 연산자를 사용하면 폴더 경로와 파일 이름을 자연스럽게 합칠 수 있습니다.
# 결과 경로는 data/memo.txt입니다.
file_path = data_dir / "memo.txt"

# write_text()는 문자열을 텍스트 파일에 저장합니다.
# encoding="utf-8"은 한글이 깨지지 않도록 UTF-8 방식으로 저장하겠다는 뜻입니다.
file_path.write_text("Python 파일 저장 연습입니다.", encoding="utf-8")

# read_text()는 텍스트 파일의 내용을 문자열로 읽어옵니다.
content = file_path.read_text(encoding="utf-8")
print("파일 내용:", content)
