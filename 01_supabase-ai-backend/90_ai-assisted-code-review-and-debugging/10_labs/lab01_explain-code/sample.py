scores = [90, 80, 70]  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
average = sum(scores) / len(scores)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if average >= 80:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    result = "Pass"  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    result = "Retry"  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

print("Average:", average)  # 터미널에 값을 출력해 코드 실행 결과를 확인합니다.
print("Result:", result)  # 터미널에 값을 출력해 코드 실행 결과를 확인합니다.

