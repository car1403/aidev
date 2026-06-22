"""공통 .venv에 설치된 외부 패키지를 확인하는 예제입니다."""

# httpx는 파이썬에 기본 포함된 표준 라이브러리가 아닙니다.
# pip install -r requirements.txt로 설치해야 사용할 수 있는 외부 패키지입니다.
import httpx

# __version__은 패키지 버전을 확인할 때 자주 사용하는 속성입니다.
httpx_version = httpx.__version__

# 현재 설치된 httpx 버전을 출력합니다.
print("설치된 httpx 버전:", httpx_version)

# 이 단원에서는 네트워크 요청을 실제로 보내지는 않습니다.
# 외부 API 호출은 07_api-external-data 단원에서 자세히 다룹니다.
print("httpx import 성공: 공통 .venv와 requirements.txt 설정이 정상입니다.")
