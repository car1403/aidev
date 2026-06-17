# 02_ch2_prompt-input-and-response

사용자 프롬프트를 입력받고 응답을 생성하는 기본 흐름을 학습합니다.

이 챕터에서는 프롬프트 문장 자체와 화면 표시 흐름을 먼저 다룹니다. 실제 LLM API 호출, 토큰 비용, 모델 파라미터는 `01_supabase-ai-backend`에서 다루고, 이 과정에서는 백엔드 API 응답을 화면에 잘 보여주는 역할에 집중합니다.

## 예제 파일

```text
01_prompt-validation.py
02_mock-ai-response.py
03_response-template.py
04_prompt-options.py
```

## 실행 예시

```powershell
streamlit run .\04_ai-chatbot-interface\02_ch2_prompt-input-and-response\02_mock-ai-response.py
```

## 확인할 내용

- 빈 질문을 처리할 수 있는가?
- 응답 생성 함수를 화면 코드와 분리할 수 있는가?
- 옵션에 따라 응답 방식이 달라지는가?
- 응답 생성 중 사용자에게 로딩 상태 또는 안내 문구를 보여줄 수 있는가?


