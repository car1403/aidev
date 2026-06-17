"""리스트와 딕셔너리 기초 예제입니다.

리스트(list)는 여러 값을 순서대로 담는 자료구조입니다.
딕셔너리(dict)는 key와 value를 한 쌍으로 담는 자료구조입니다.

실제 백엔드 개발에서는 사용자 목록, 게시글 목록, API 응답 데이터 등을
리스트와 딕셔너리 형태로 자주 다룹니다.
"""

# 리스트는 대괄호 [ ]로 만들고, 여러 값을 순서대로 저장합니다.
todos = ["Python 설치", "변수 연습", "조건문 연습"]

# append()는 리스트 끝에 새 값을 추가합니다.
todos.append("반복문 연습")

# type()으로 todos가 list인지 확인합니다.
print(type(todos))

print("[할 일 목록]")

# enumerate()는 리스트의 값과 함께 번호를 만들어 줍니다.
# start=1을 주면 번호가 1부터 시작합니다.
for index, todo in enumerate(todos, start=1):
    print(index, todo)

# 딕셔너리는 중괄호 { }로 만들고, "key": value 형태로 값을 저장합니다.
# key는 데이터를 꺼낼 때 사용하는 이름입니다.
student = {
    "name": "Jean",
    "score": 95,
    "passed": True,
}

print(type(student))
print("\n[학생 정보]")

# items()는 딕셔너리의 key와 value를 함께 꺼냅니다.
for key, value in student.items():
    print(key, "=", value)

# 딕셔너리를 리스트 안에 여러 개 넣으면 여러 명의 학생 정보를 표현할 수 있습니다.
students = [{
    "name": "Jean",
    "score": 95,
    "passed": True,
}, {
    "name": "Jean2",
    "score": 96,
    "passed": True,
}, {
    "name": "Jean",
    "score": 97,
    "passed": True,
}]

print(type(students))

# 바깥 반복문은 학생 한 명씩 꺼냅니다.
for index, student in enumerate(students, start=1):
    print(f"\n[학생 정보 {index}]")

    # 안쪽 반복문은 한 학생의 key와 value를 꺼냅니다.
    for key, value in student.items():
        print(key, "=", value)
