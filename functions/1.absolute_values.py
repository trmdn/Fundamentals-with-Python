# list_of_values = [abs(float(i)) for i in input().split(" ")]
# print(list_of_values)

list_of_values = input().split()


def values(my_list):
    absolute_list = []
    for number in my_list:
        number = float(number)
        absolute_number = abs(number)
        absolute_list.append(absolute_number)
    return absolute_list


print(values(list_of_values))
