# 09. Common Errors For Beginners

##.venv 활성화가 안 됨

증상:

```text
패키지를 설치했는데 import 오류가 발생함
```

확인:

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
python --version
```

## 패키지 import 오류

증상:

```text
ModuleNotFoundError
```

해결:

```powershell
pip install -r requirements.txt
```

## Docker가 실행되지 않음

증상:

```text
docker ps 오류
```

해결:

```text
Docker Desktop 실행
PowerShell 재시작
docker ps 다시 실행
```

## 포트 충돌

증상:

```text
port is already allocated
```

자주 쓰는 포트:

```text
5678: n8n
8900: 99 sample backend
8901: 99 sample frontend
```

해결:

```powershell
docker ps
docker stop 컨테이너이름
```

또는 실행 포트를 바꿉니다.

## n8n에서 Webhook이 안 됨

확인:

```text
workflow가 활성화되어 있는가?
Webhook URL이 정확한가?
POST/GET method가 맞는가?
요청 JSON 구조가 맞는가?
```

## Dify API 호출이 안 됨

확인:

```text
Dify 서버가 실행 중인가?
API Key가 맞는가?
앱이 publish 되었는가?
요청 Body가 문서 형식과 맞는가?
```

## 한글 출력이 깨져 보임

PowerShell 출력 인코딩 문제일 수 있습니다.

파일 자체가 UTF-8이면 VS Code나 Cursor에서는 정상 표시될 수 있습니다.
