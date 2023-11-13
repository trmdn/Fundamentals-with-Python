numbers = input().split()
even_numbers = []

for number in numbers:
    even_numbers.append(int(number))

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, even_numbers))
print(result)