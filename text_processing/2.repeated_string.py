words = input().split(" ")
result = ""

for word in words:
    length_of_word = len(word)
    result += word * length_of_word

print(result)