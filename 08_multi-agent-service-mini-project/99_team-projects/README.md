# 99_team-projects

이 폴더는 07 최종 미니 프로젝트 작업 공간입니다.

기본 템플릿은 `multi-agent-service-team-template`입니다. 실제 프로젝트를 시작할 때는 이 폴더를 복사해서 팀별 폴더를 만듭니다.

## 팀 프로젝트 시작

```powershell
cd C:\aidev\08_multi-agent-service-mini-project
Copy-Item .\99_team-projects\multi-agent-service-team-template .\99_team-projects\team-01-auto-healing-service -Recurse
```

복사한 뒤 새 폴더에서 실행합니다.

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\99_team-projects\team-01-auto-healing-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 주의 사항

- 원본 템플릿은 기준으로 남겨 둡니다.
- 팀별 작업은 복사한 폴더에서 진행합니다.
- `.env`, `.venv`, API Key는 커밋하지 않습니다.
