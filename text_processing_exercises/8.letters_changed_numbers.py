strings = input().split()
alphabet_lower_case = "".join([chr(x) for x in range(ord("a"), ord("a") + 26)])
total = []

for string in strings:
    number = int(string[1:-1])
    first_letter = string[0]
    last_letter = string[-1]
    first_letter_position = alphabet_lower_case.index(first_letter.lower()) + 1
    last_letter_position = alphabet_lower_case.index(last_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_position
    elif first_letter.islower():
        number *= first_letter_position

    if last_letter.isupper():
        number -= last_letter_position
    elif last_letter.islower():
        number += last_letter_position

    total.append(number)

print(f"{sum(total):.2f}")