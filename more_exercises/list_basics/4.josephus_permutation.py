numbers = input().split()
single_number = int(input())
list_with_numbers = list()

pos = single_number - 1
index = 0
len_list = len(numbers)

while len_list > 0:
    index = (pos + index) % len_list
    list_with_numbers.append(numbers.pop(index))
    len_list -= 1

print(f"[{','.join(list_with_numbers)}]")