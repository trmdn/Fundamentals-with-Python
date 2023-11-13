words = [characters for characters in input() if characters != " "]
words_dict = {}

for symbol in words:
    if symbol not in words_dict.keys():
        words_dict[symbol] = 0
    words_dict[symbol] += 1

for keys, values in words_dict.items():
    print(f"{keys} -> {values}")