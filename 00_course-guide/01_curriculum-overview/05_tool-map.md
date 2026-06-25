# 05. Tool Map

이 문서는 전체 과정에서 사용하는 주요 도구와 등장 시점을 정리합니다.

| 도구 | 사용 과정 | 역할 |
| --- | --- | --- |
| Python | 01~08 | 예제 코드, API 서버, Agent, 자동화 스크립트 |
| VS Code | 01~08 | 코드 편집, 문서 읽기, 터미널 실행 |
| PowerShell | 00~08 | 폴더 이동, 가상환경 활성화, 예제 실행 |
| Git | 01~08 | 변경 이력 관리, diff 확인, 커밋 |
| GitHub | 01~08 | 원격 저장소, 협업, 제출, 계정 기반 로그인 |
| GitHub Copilot Chat | 01~08 | VS Code 안에서 코드 설명, 오류 분석, 개선 아이디어 확인 |
| FastAPI | 02, 04, 07, 08 | API 서버와 백엔드 서비스 |
| Streamlit | 03, 04, 08 | UI와 대시보드 |
| Supabase | 02~04 | 데이터베이스, 인증, 저장소, RLS |
| Upstash Redis | 02~04 | 캐시, TTL, 간단한 세션 상태 |
| Gemini | 02~04 | 초반 AI 응답 생성 기본 모델 |
| OpenAI API | 02 이후 선택 | 비교 실습, 확장 실습, Agent 모델 연동 |
| Docker Desktop | 05~08 | 컨테이너 기반 로컬 실행 환경 |
| PostgreSQL/pgvector | 05~06 | Memory, RAG, Vector DB |
| LangGraph | 05~06 | Agent 상태 흐름과 그래프 구성 |
| Docker Compose | 07~08 | 여러 서비스를 함께 실행 |
| GitHub Actions | 07~08 | CI/CD 기본 검증과 배포 파이프라인 |
| AWS | 07~08 | 배포와 운영 환경 확장 |
| CloudWatch | 07~08 | 로그와 모니터링 |

## 준비 우선순위

처음에는 아래 도구부터 준비합니다.

```text
1. GitHub 계정
2. Python
3. VS Code
4. PowerShell
5. Git
6. VS Code GitHub 로그인
7. GitHub Copilot Chat
```

Docker Desktop, AWS, GitHub Actions는 `05_llm-agent-orchestration` 이후 필요한 시점에 본격적으로 다룹니다.
