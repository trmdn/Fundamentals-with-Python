def positive(list_of_nums):
    return ', '.join([number for number in list_of_nums if int(number) >= 0])


def negative(list_of_nums):
    return ', '.join([number for number in list_of_nums if int(number) < 0])


def even(list_of_nums):
    return ', '.join([number for number in list_of_nums if int(number) % 2 == 0])


def odd(list_of_nums):
    return ', '.join([number for number in list_of_nums if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive(numbers)}")
print(f"Negative: {negative(numbers)}")
print(f"Even: {even(numbers)}")
print(f"Odd: {odd(numbers)}")
