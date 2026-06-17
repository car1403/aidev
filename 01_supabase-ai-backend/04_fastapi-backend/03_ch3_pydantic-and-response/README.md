# 03_ch3_pydantic-and-response

Pydantic 모델과 응답 구조 설계를 학습합니다.

Pydantic은 요청 데이터가 올바른 형식인지 검사하고, FastAPI가 Swagger 문서를 자동으로 만드는 데 사용됩니다.

## 예제 파일

```text
01_pydantic-models.py
02_request-validation.py
03_response-model.py
04_standard-response.py
```

## 확인할 것

- 필수 필드를 빼면 422 오류가 발생하는가?
- 문자열 길이, 숫자 범위 검증이 동작하는가?
- response_model이 내부 데이터를 안전하게 제한하는가?
- 응답 구조를 `success`, `message`, `data` 형태로 통일할 수 있는가?

