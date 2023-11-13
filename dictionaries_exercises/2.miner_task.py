resources = {}

while True:
    count_of_resources = input()
    if count_of_resources == "stop":
        break
    quality = int(input())
    if count_of_resources not in resources.keys():
        resources[count_of_resources] = 0
    resources[count_of_resources] += quality


for key, value in resources.items():
    print(f"{key} -> {value}")