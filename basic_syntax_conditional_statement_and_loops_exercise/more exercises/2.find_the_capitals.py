def find_capital(word):
    capital_index = [i for i, char in enumerate(word) if char.isupper()]
    return capital_index

words = input()
print(find_capital(words))