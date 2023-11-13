word_for_remove = input()
word = input()

while word_for_remove in word:
    word = word.replace(word_for_remove, "")

print(word)