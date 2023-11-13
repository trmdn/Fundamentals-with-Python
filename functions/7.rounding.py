list_of_numbers = input().split()


def numbers(number):
    round_list = []
    for numbs in number:
        numbs = float(numbs)
        rounding = round(numbs)
        round_list.append(rounding)
    return round_list


print(numbers(list_of_numbers))