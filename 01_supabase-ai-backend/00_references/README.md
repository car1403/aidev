# 00_references

`01_supabase-ai-backend`를 시작하기 전에 읽는 참고 자료입니다.

이 폴더는 별도 수업 단원이 아니라, 수업 참여자가 수업 중 계속 찾아보는 기준 문서 모음입니다. Python, FastAPI, Supabase를 배우기 전에 AI 도구를 어떻게 사용할지, AI 답변을 어떻게 검증할지, API key를 어떻게 안전하게 관리할지 먼저 정리합니다.

## 문서 목록

```text
ai-tools-comparison-guide.md
prompt-and-answer-validation-guide.md
```

## 먼저 확인할 내용

- AI 리터러시는 AI 답변을 그대로 믿는 것이 아니라 검토하고 실행해 보는 습관입니다.
- Vibe Coding은 AI에게 모두 맡기는 방식이 아니라, 요구사항을 설명하고 결과를 확인하는 개발 방식입니다.
- Python, VS Code, `.venv`, `pip`, `requirements.txt`의 역할을 구분합니다.
- Gemini API, OpenAI API, Upstash Redis, Supabase key는 비용과 보안 이슈가 있을 수 있으므로 `.env`와 환경변수로 관리합니다.
- 01~03 과정의 기본 LLM API는 Gemini입니다. OpenAI API는 선택/비교 실습용으로 다룹니다.
- Codex, NotebookLM, Perplexity AI, ChatGPT/Claude/Gemini는 목적에 따라 다르게 사용합니다.

## 확인 질문

```text
AI가 만든 코드를 실행 전에는 어떤 기준으로 검토해야 하나요?
API key를 코드에 직접 적으면 왜 위험한가요?
Codex와 NotebookLM, Perplexity AI는 각각 언제 사용하면 좋나요?
좋은 프롬프트에는 어떤 요소가 들어가야 하나요?
```
