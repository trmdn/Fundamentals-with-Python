num_of_str = int(input())

for i in range(num_of_str):
    string = str(input())

    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")