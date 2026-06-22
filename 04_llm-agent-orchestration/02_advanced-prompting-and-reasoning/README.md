# 02 Advanced Prompting and Reasoning

이 단원은 프롬프트를 더 안정적으로 설계하는 방법을 학습합니다. 단순히 질문을 던지는 수준을 넘어 역할, 지시문, 맥락, 출력 형식을 명확히 나누어 LLM 응답 품질을 개선합니다.

## 학습 목표

- Role, Instruction, Context 구조로 프롬프트를 작성합니다.
- Few-shot 예시를 사용해 원하는 답변 스타일을 유도합니다.
- JSON 형식 응답과 Pydantic 기반 Structured Output을 이해합니다.
- Plan-Act-Review, ReAct 스타일 사고 흐름을 코드로 살펴봅니다.
- Prompt Injection을 이해하고 입력 검증과 안전한 시스템 지시문을 적용합니다.

## 폴더 구성

```text
02_advanced-prompting-and-reasoning
├─.env.example
├─ 01_ch1_prompt-design-patterns
│ ├─ 01_role-and-context-prompt.py
│ └─ 02_few-shot-style-prompt.py
├─ 02_ch2_structured-output-json
│ ├─ 01_json-output-request.py
│ └─ 02_structured-output-pydantic.py
├─ 03_ch3_reasoning-and-react-basics
│ ├─ 01_plan-act-review-pattern.py
│ └─ 02_react-style-without-tools.py
└─ 04_ch4_prompt-safety-and-evaluation
 ├─ 01_prompt-injection-defense.py
 └─ 02_prompt-version-evaluation.py
```

## 실습 시작 순서

```powershell
cd C:\aidev\04_llm-agent-orchestration\02_advanced-prompting-and-reasoning
python -m venv.venv
.\.venv\Scripts\Activate.ps1
pip install openai python-dotenv pydantic
Copy-Item.env.example.env
```

## 실행 순서

```powershell
python.\01_ch1_prompt-design-patterns\01_role-and-context-prompt.py
python.\01_ch1_prompt-design-patterns\02_few-shot-style-prompt.py
python.\02_ch2_structured-output-json\01_json-output-request.py
python.\02_ch2_structured-output-json\02_structured-output-pydantic.py
python.\03_ch3_reasoning-and-react-basics\01_plan-act-review-pattern.py
python.\03_ch3_reasoning-and-react-basics\02_react-style-without-tools.py
python.\04_ch4_prompt-safety-and-evaluation\01_prompt-injection-defense.py
python.\04_ch4_prompt-safety-and-evaluation\02_prompt-version-evaluation.py
```

## 수업 중 확인 질문

- Role, Instruction, Context를 나누면 어떤 점이 좋아지나요?
- JSON 응답을 요청하는 것과 Pydantic으로 검증하는 것은 어떤 차이가 있나요?
- ReAct 구조에서 Reasoning과 Action은 각각 어떤 역할을 하나요?
- Prompt Injection은 왜 위험하고, 어떤 방식으로 방어할 수 있나요?

