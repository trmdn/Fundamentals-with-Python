message = input()
encrypted_message = ""

for cipher in message:
    encrypted_char = chr(ord(cipher) + 3)
    encrypted_message += encrypted_char
print(encrypted_message)