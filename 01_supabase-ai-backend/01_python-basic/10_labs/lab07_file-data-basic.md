# Lab 07 - File Data Basic

파일에 데이터를 저장하고 다시 읽는 실습입니다.

## 목표

- `Path`로 폴더와 파일 경로를 만들 수 있습니다.
- 텍스트 파일을 저장하고 읽을 수 있습니다.
- CSV 파일을 저장하고 읽을 수 있습니다.
- JSON 파일에 dict와 list를 저장할 수 있습니다.

## 실습 1. 메모 파일 저장

`practice\lab07_memo.py` 파일을 만듭니다.

요구사항:

```text
1. data 폴더를 만듭니다.
2. memo.txt 파일에 문자열을 저장합니다.
3. 저장한 파일을 다시 읽어 출력합니다.
```

## 실습 2. 학습 로그 추가 저장

`practice\lab07_daily_log.py` 파일을 만듭니다.

요구사항:

```text
1. daily_log.txt 파일을 만듭니다.
2. 여러 줄의 학습 내용을 저장합니다.
3. append 모드로 한 줄을 추가합니다.
4. 전체 내용을 줄 번호와 함께 출력합니다.
```

## 실습 3. CSV 학생 목록

`practice\lab07_students_csv.py` 파일을 만듭니다.

요구사항:

```text
1. 학생 이름과 점수를 CSV로 저장합니다.
2. 저장한 CSV를 다시 읽습니다.
3. 각 줄을 출력합니다.
```

## 실습 4. JSON 설정 파일

`practice\lab07_config_json.py` 파일을 만듭니다.

요구사항:

```text
1. app_name, debug, default_model 값을 dict에 저장합니다.
2. config.json 파일로 저장합니다.
3. 다시 읽어 각 설정값을 출력합니다.
```

## 실습 5. JSON 로그 목록

`practice\lab07_logs_json.py` 파일을 만듭니다.

요구사항:

```text
1. list 안에 dict 형태로 로그 3개를 저장합니다.
2. service_logs.json으로 저장합니다.
3. 다시 읽어 로그 level과 message를 출력합니다.
```

## 확인 질문

```text
1. 텍스트 파일과 JSON 파일은 어떤 차이가 있나요?
2. CSV는 어떤 데이터에 적합한가요?
3. ensure_ascii=False는 왜 사용하나요?
```
