# 04_ch4_github-actions-cicd

GitHub Actions로 자동 빌드와 테스트 흐름을 구성하는 방법을 학습합니다.

## CI/CD란?

CI는 코드가 바뀔 때 자동으로 검사하는 흐름입니다.
CD는 검사된 코드를 자동으로 배포하는 흐름입니다.

이 단원에서는 먼저 Docker 이미지가 빌드되는지 확인하는 CI 흐름을 다룹니다.

## 기본 흐름

```text
git push
-> GitHub Actions 실행
-> Python 문법 검사
-> Docker Compose 설정 검증
-> Docker image build
-> 성공/실패 확인
```

## workflow 파일 위치

실습 파일은 아래 위치에 있습니다.

```text
02_service-deployment-and-automation/04_ch4_github-actions-cicd/.github/workflows/docker-build-check.yml
```

실제 GitHub 저장소에서 자동 실행하려면 저장소 최상위의 `.github/workflows` 폴더 아래에 있어야 합니다.

예시:

```text
C:\aidev\.github\workflows\docker-build-check.yml
```

06 과정만 별도 저장소로 운영한다면 아래 위치도 가능합니다.

```text
C:\aidev\06_multi-agent-service-ops\.github\workflows\docker-build-check.yml
```

## 현재 workflow가 하는 일

```text
1. 저장소 코드 checkout
2. Python 3.12 준비
3. Python 문법 검사
4. docker compose config로 Compose 설정 검증
5. Docker image build
```

이 workflow는 `C:\aidev` 전체를 GitHub 저장소로 사용하는 경우와 `06_multi-agent-service-ops`만 별도 저장소로 사용하는 경우를 모두 고려해 경로를 확인합니다.

처음에는 AWS 배포까지 자동화하지 않습니다. 먼저 “코드와 Docker 구성이 깨졌는지 자동으로 확인하는 CI”를 이해하는 것이 목표입니다.

## 주의

- 실제 API Key는 GitHub에 올리지 않습니다.
- 필요한 값은 GitHub Repository Secrets에 저장합니다.
- AWS 배포는 다음 챕터에서 개념을 연결하고, 실제 자동 배포는 비용과 권한을 확인한 뒤 진행합니다.
