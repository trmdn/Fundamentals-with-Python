def smallest_num(num1, num2, num3: int):
    return min(num1, num2, num3)


first_number = int(input())
second_number = int(input())
third_number = int(input())
min_num = smallest_num(first_number, second_number, third_number)
print(min_num)