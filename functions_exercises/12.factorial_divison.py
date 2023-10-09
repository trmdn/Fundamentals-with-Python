def factorial_division(character):
    for numbers in range(1, character):
        character *= numbers
    return character


first_number = int(input())
second_number = int(input())
first_num_factorial = factorial_division(first_number)
second_num_factorial = factorial_division(second_number)
final_result = first_num_factorial / second_num_factorial
print(f"{final_result:.2f}")