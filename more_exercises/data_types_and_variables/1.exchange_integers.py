def exchange_int(num_one, num_two):
    return f"Before:\na = {num_one}\nb = {number_two}\nAfter:\na = {number_two}\nb = {number_one}"


number_one, number_two = int(input()), int(input())
result = exchange_int(number_one, number_two)
print(result)