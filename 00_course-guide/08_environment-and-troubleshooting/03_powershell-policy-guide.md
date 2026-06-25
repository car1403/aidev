# 03. PowerShell Policy Guide

PowerShell 실행 정책 오류 해결 문서입니다.

## 오류 예시

```text
running scripts is disabled on this system
```

## 해결

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

`Y`를 입력하고 Enter를 누릅니다.

## 다시 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```
