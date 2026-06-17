# README Writing Template

README는 프로젝트를 처음 보는 사람이 무엇을 해야 하는지 알 수 있게 안내하는 문서입니다.

## 기본 구조

````markdown
# 프로젝트 이름

이 프로젝트가 무엇을 하는지 한두 문장으로 설명합니다.

## 목표

- 목표 1
- 목표 2
- 목표 3

## 사용 기술

- Python
- FastAPI
- Supabase

## 실행 방법

```powershell
cd 프로젝트폴더
.\.venv\Scripts\Activate.ps1
python main.py
```

## 환경변수

```env
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-supabase-anon-key
```

실제 key는 README에 적지 않습니다.

## 학습 기록

- 배운 점
- 어려웠던 점
- 다음에 개선할 점
````

## 좋은 README 기준

```text
처음 보는 사람이 프로젝트 목적을 이해할 수 있다.
실행 순서가 위에서 아래로 정리되어 있다.
필요한 환경변수가 예시로 안내되어 있다.
실제 secret 값은 포함되어 있지 않다.
오류가 났을 때 확인할 항목이 있다.
```
