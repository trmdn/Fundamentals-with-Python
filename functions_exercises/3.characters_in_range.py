def other_characters(first_char: str, second_char: str) -> list:
    characters = []
    for current_char_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_char_as_digit))
    return characters


first_symbol = input()
second_sybmol = input()
result = other_characters(first_symbol, second_sybmol)
print(*"".join(result))
