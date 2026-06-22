# Lab 04. Multi-turn mock 대화 이력

Multi-turn 호출은 이전 대화 내용을 함께 보내서 AI가 문맥을 이어가도록 만드는 구조입니다.

이 실습에서는 대화 이력을 리스트로 관리하고, 최근 메시지를 LLM 요청에 포함하는 흐름을 연습합니다. 실제 서비스에서는 이 대화 이력이 Supabase에 저장될 수 있습니다.

## 학습 목표

- `user`, `assistant` 메시지를 순서대로 저장합니다.
- 최근 대화만 잘라서 요청 메시지로 구성합니다.
- 대화 이력을 Supabase 저장 대상 데이터로 바라봅니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\10_labs\lab-04_mock-multi-turn-memory\starter.py
```
