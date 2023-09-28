number = int(input())
number_as_string = str(number)

for i in range(len(number_as_string) -1, -1, -1):
    print(number_as_string[i], end="")