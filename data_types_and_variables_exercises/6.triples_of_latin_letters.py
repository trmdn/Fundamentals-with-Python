combinations = int(input())

for i in range(0, combinations):
    for j in range(0, combinations):
        for k in range(0, combinations):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")