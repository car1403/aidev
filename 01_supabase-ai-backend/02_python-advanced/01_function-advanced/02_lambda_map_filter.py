"""lambda, map, filter 예제입니다."""

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda number: number * number, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("원본:", numbers)
print("제곱:", squared)
print("짝수:", even_numbers)
