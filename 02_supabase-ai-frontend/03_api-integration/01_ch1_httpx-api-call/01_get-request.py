import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.

API_URL = "http://127.0.0.1:8000/health"  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

response = httpx.get(API_URL, timeout=5.0)  # GET 요청의 응답을 response 변수에 저장해 상태 코드와 JSON 데이터를 확인합니다.

print("status code:", response.status_code)  # 터미널에 값을 출력해 코드 실행 결과를 확인합니다.
print("json:", response.json())  # 터미널에 값을 출력해 코드 실행 결과를 확인합니다.

