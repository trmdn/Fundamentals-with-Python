n = int(input())
word = input()
strings = []

for i in range(n):
    special_word = input()
    strings.append(special_word)
print(strings)

filtered_strings = []

for current_string in strings:
    if word in current_string:
        filtered_strings.append(current_string)
print(filtered_strings)