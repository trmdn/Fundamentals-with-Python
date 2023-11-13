def palindrome_int(char):
    return char == char[::-1]


numbers = input().split(", ")
for number_as_digit in numbers:
    print(palindrome_int(number_as_digit))