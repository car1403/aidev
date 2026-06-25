# 99_basic-mini-project

Python 기초 문법을 사용해 **파일 저장형 학습 기록 관리 프로그램**을 만듭니다.

이 미니 프로젝트는 `01_python-basic`에서 배운 내용을 한 번에 연결하는 최종 실습입니다. 단순히 문법을 따로 확인하는 것이 아니라, 입력, 조건문, 반복문, 자료구조, 함수, JSON 저장을 묶어 작은 프로그램으로 완성합니다.

## 프로젝트 목표

```text
1. 메뉴 기반 프로그램을 만들 수 있습니다.
2. 학습 기록을 list 안의 dict 형태로 저장할 수 있습니다.
3. 함수로 기능을 나누어 코드를 정리할 수 있습니다.
4. JSON 파일에 데이터를 저장하고 다시 읽을 수 있습니다.
5. 프로그램을 종료해도 기록이 유지되는 구조를 이해할 수 있습니다.
```

## 실행

```powershell
cd C:\aidev\01_python-git-foundation
.\.venv\Scripts\Activate.ps1
python .\01_python-basic\99_basic-mini-project\learning_record_app.py
```

## 사용하는 문법

```text
input()
if / elif / else
while True
break
list
dict
function
Path
json
```

## 데이터 구조

학습 기록 하나는 아래와 같은 dict로 저장합니다.

```python
{
    "title": "반복문 복습",
    "minutes": 30,
    "done": True
}
```

전체 학습 기록은 list에 저장합니다.

```python
records = [
    {"title": "조건문 복습", "minutes": 20, "done": True},
    {"title": "파일 저장 연습", "minutes": 40, "done": False},
]
```

## 기능

| 메뉴 | 기능 |
| --- | --- |
| 1 | 학습 기록 추가 |
| 2 | 전체 학습 기록 보기 |
| 3 | 완료한 학습만 보기 |
| 4 | 총 학습 시간 보기 |
| 5 | JSON 파일로 저장 |
| 6 | JSON 파일에서 읽기 |
| q | 프로그램 종료 |

## 생성되는 파일

프로그램을 실행하면 아래 파일이 만들어질 수 있습니다.

```text
data/learning_records.json
```

이 파일은 학습 기록을 JSON 형태로 저장합니다. 나중에 Supabase에 대화 이력, 서비스 로그, 피드백 데이터를 저장할 때도 같은 구조적 사고가 필요합니다.

## 완료 기준

```text
1. 기록을 2개 이상 추가할 수 있습니다.
2. 전체 기록을 출력할 수 있습니다.
3. 완료한 기록만 출력할 수 있습니다.
4. 총 학습 시간을 계산할 수 있습니다.
5. JSON 파일로 저장할 수 있습니다.
6. 프로그램을 다시 실행한 뒤 JSON 파일에서 읽어올 수 있습니다.
7. q를 입력하면 종료됩니다.
```
