# 02. venv Troubleshooting

`.venv` 관련 오류 해결 문서입니다.

##.venv 활성화가 안 될 때

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

그 뒤 다시 실행합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

## ModuleNotFoundError

패키지가 설치되지 않은 경우입니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## pip install 실패

확인:

```text
인터넷 연결
requirements.txt가 있는 폴더인지
.venv가 활성화되어 있는지
Python 버전이 맞는지
```
