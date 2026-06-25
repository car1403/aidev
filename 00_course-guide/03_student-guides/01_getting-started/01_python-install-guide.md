# 01. Python Install Guide

Python은 이 과정에서 가장 기본이 되는 실행 도구입니다.


## 1. Python 설치 여부 확인

PowerShell을 열고 아래 명령어를 입력합니다.

```powershell
python --version
```

또는:

```powershell
py --version
```

정상 예시:

```text
Python 3.12.x
```

`Python` 버전이 보이면 설치되어 있는 것입니다.

## 2. pip 확인

`pip`는 Python 패키지를 설치하는 도구입니다.

```powershell
pip --version
```

정상 예시:

```text
pip 24.x from...
```

## 3. Python 설치 방법

설치가 되어 있지 않다면 Python 공식 사이트에서 설치합니다.

```text
https://www.python.org
```

Windows 설치 시 가장 중요한 체크박스:

```text
[x] Add python.exe to PATH
```

이 항목을 체크해야 PowerShell에서 `python` 명령어를 바로 사용할 수 있습니다.

## 4. 권장 버전

현재 수업에서는 Python 3.12 계열을 권장합니다.

```text
권장: Python 3.12.x
가능: Python 3.11.x 이상
비권장: Python 3.10 이하
```

## 5. 설치 후 다시 확인

설치가 끝나면 PowerShell을 완전히 닫았다가 다시 열고 확인합니다.

```powershell
python --version
pip --version
```

## 6. 자주 만나는 문제

### `python` 명령을 찾을 수 없습니다

가능한 원인:

```text
Python이 설치되지 않았다.
설치 시 Add python.exe to PATH를 체크하지 않았다.
PowerShell을 설치 전부터 열어 두었다.
```

해결:

```text
1. PowerShell을 닫고 다시 연다.
2. py --version을 실행해 본다.
3. 그래도 안 되면 Python을 다시 설치하면서 Add python.exe to PATH를 체크한다.
```

### Microsoft Store가 열립니다

Windows에서 `python`을 입력했을 때 Microsoft Store가 열릴 수 있습니다.

해결:

```text
1. Python 공식 사이트에서 설치한다.
2. Windows 설정에서 App execution aliases를 확인한다.
3. python.exe, python3.exe alias를 끄는 방법도 있다.
```

초보자는 수업 중 함께 확인하는 것이 좋습니다.
