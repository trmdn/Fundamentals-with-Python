number = int(input())
total_sum = 0

for characters in range(number):
    current_char = input()
    total_sum += ord(current_char)
print(f"The sum equals: {total_sum}")