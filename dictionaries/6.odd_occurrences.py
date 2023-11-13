words = input().split()
dictionary = {}

for word in words:
    lower_words = word.lower()
    if lower_words not in dictionary:
        dictionary[lower_words] = 0
    dictionary[lower_words] += 1

for key, values in dictionary.items():
    if values % 2 != 0:
        print(key, end=" ")
