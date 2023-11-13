numbers = [int(x) for x in input().split(", ")]
for _ in numbers:
    numbers.append(numbers.pop(numbers.index(0)))
print(numbers)