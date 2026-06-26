# 00 Course Guide

이 폴더는 전체 AI 개발 과정을 처음 이해하고, 필요한 공통 기준을 빠르게 확인하기 위한 안내서입니다.

상세한 실습은 각 과정 폴더의 `README.md`와 `SETUP.md`에서 진행합니다. 이곳에서는 전체 흐름, 학습 준비, 프로젝트와 평가 기준만 압축해서 봅니다.

## 구성

| 폴더 | 역할 |
| --- | --- |
| [01_course-overview](./01_course-overview/README.md) | 01~08 과정의 순서, 목표, 큰 흐름 |
| [02_learning-guide](./02_learning-guide/README.md) | 시작 방법, 환경 준비, 막혔을 때 확인할 기준 |
| [03_project-and-evaluation](./03_project-and-evaluation/README.md) | 프로젝트 진행, 필수 산출물, 평가와 제출 기준 |

강사용 운영 자료는 로컬 전용 `04_instructor-guide`에 둘 수 있습니다. 이 폴더는 Git에 올리지 않도록 `.gitignore`에 등록되어 있으며, 학생 배포본에는 포함하지 않습니다.

## 처음 보는 순서

1. [과정 순서](./01_course-overview/course-sequence.md)를 보고 전체 학습 흐름을 확인합니다.
2. [과정 지도](./01_course-overview/course-map.md)에서 각 과정의 역할을 확인합니다.
3. [시작 가이드](./02_learning-guide/getting-started.md)를 따라 기본 준비를 점검합니다.
4. [환경 준비 가이드](./02_learning-guide/environment-guide.md)에서 Python, VS Code, `.venv`, `.env` 기준을 확인합니다.
5. 막히면 [트러블슈팅 가이드](./02_learning-guide/troubleshooting.md)를 먼저 봅니다.
6. 프로젝트 전에는 [프로젝트 가이드](./03_project-and-evaluation/project-guide.md)와 [제출 체크리스트](./03_project-and-evaluation/submission-checklist.md)를 확인합니다.

## 핵심 기준

- `01`은 Python/Git 기초를 분리해서 초반 병목을 줄입니다.
- `02`~`04`는 Supabase 기반 AI 웹 서비스 흐름을 다룹니다.
- `05`~`06`은 LLM Agent, Tool Use, RAG, LangGraph를 다룹니다.
- `07`~`08`은 Docker Compose, 운영 자동화, 멀티 에이전트 서비스 프로젝트를 다룹니다.
- `01`~`04`, `06`~`08`은 과정 최상위 `.venv` 하나를 기본으로 사용합니다.
- `05`는 단원별 의존성이 달라질 수 있어 단원별 `.venv` 방식을 우선 권장합니다.
- `.env`, API Key, token, password는 제출하거나 GitHub에 올리지 않습니다.

