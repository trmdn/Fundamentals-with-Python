main_string = input.split()

def insert_space(index, main_string):
    return main_string[:index] + " " + main_string[index:]

def reverse_string(substring, main_string):
    if substring in main_string:
        word_find = main_string.find(substring)
        main_string = main_string[:word_find] + main_string[word_find + len(substring):]

    if substring not in main_string:
        print("error")