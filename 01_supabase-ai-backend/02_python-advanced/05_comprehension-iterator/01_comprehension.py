"""list/dict comprehension 예제입니다."""

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]
even_squares = [number * number for number in numbers if number % 2 == 0]
score_map = {f"student_{number}": number * 10 for number in range(1, 6)}

print("squares:", squares)
print("even_squares:", even_squares)
print("score_map:", score_map)
