word = [n for n in input()]
letter_position = list()

for position, letter in enumerate(word):
    if letter.isupper():
        letter_position.append(position)
print(letter_position)