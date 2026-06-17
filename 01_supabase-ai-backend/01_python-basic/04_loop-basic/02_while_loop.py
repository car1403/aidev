"""while 반복문 예제입니다.

`while` 반복문은 조건이 참(True)인 동안 계속 실행됩니다.
반복 조건이 계속 참이면 무한 반복이 될 수 있으므로,
반복 안에서 조건을 바꾸는 코드가 필요합니다.
"""

# count는 반복 횟수를 세기 위한 변수입니다.
count = 1

# count가 5 이하인 동안 반복합니다.
while count <= 5:
    print("현재 count:", count)

    # count를 1씩 증가시켜야 언젠가 count <= 5 조건이 거짓이 됩니다.
    # 이 줄이 없으면 반복이 끝나지 않을 수 있습니다.
    count += 1

print("반복이 끝났습니다.")

# 아래 for 반복문은 continue와 break의 차이를 보여줍니다.
for number in range(1, 6):
    # continue는 이번 반복의 나머지 코드를 건너뛰고 다음 반복으로 넘어갑니다.
    # number가 3이면 아래 print는 실행되지 않습니다.
    if number == 3:
        continue

    # break는 반복문 전체를 즉시 끝냅니다.
    # number가 5가 되면 반복문이 종료됩니다.
    if number == 5:
        break

    print("number:", number)
