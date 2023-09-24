special_number = int(input())

for current_number in range(1, special_number + 1):
    current_num_as_str = str(current_number)
    digit_sum = 0
    for digit in current_num_as_str:
        digit_sum += int(digit)
    is_special = False
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f"{current_number} -> {is_special}")