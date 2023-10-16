number_list = list(map(int, input().split(", ")))
even_or_not = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))
even_indices = list(filter(lambda a: a != 'no', even_or_not))
print(even_indices)