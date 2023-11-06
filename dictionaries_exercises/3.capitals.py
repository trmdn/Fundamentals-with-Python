countries = input().split(", ")
capitals = input().split(", ")
final_result = dict(zip(countries, capitals))

for key, value in final_result.items():
    print(f"{key} -> {value}")