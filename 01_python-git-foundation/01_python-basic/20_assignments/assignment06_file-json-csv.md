# Assignment 06 - File JSON CSV

파일에 데이터를 저장하고 다시 읽는 과제입니다.

## 과제 파일

```text
submissions/assignment06_file_data.py
```

## 요구사항

```text
1. data 폴더를 만듭니다.
2. 학습 메모를 memo.txt로 저장합니다.
3. 학생 목록을 students.csv로 저장합니다.
4. 설정 정보를 config.json으로 저장합니다.
5. 서비스 로그 목록을 service_logs.json으로 저장합니다.
6. 저장한 파일들을 다시 읽어 화면에 출력합니다.
```

## config.json에 들어갈 정보

```text
app_name
debug
default_model
max_messages
```

## service_logs.json에 들어갈 정보

```text
level
message
user
```

## 확인 기준

```text
Path를 사용했는가?
텍스트, CSV, JSON을 각각 저장했는가?
저장한 파일을 다시 읽었는가?
ensure_ascii=False를 사용해 한글이 잘 보이게 저장했는가?
```
