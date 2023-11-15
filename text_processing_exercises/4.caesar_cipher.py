message = input()
encrypted_message = ""

for char in message:
    encrypted_character = chr(ord(char) + 3)
    encrypted_message += encrypted_character
print(encrypted_message)