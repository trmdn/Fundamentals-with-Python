# n = int(input("Enter a number: "))
#
# for i in range(n, n + 1):
#     for j in range(n, 0, -1):
#         print("*" * n)

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print('*', end=' ')
    print()
