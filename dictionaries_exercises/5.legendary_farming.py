elements = {"shards" : 0, "fragments" : 0, "motes" : 0}
obtained = False

while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()

        if key not in elements.keys():
            elements[key] = 0
        elements[key] += value

        if elements["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            elements["shards"] -= 250
            obtained = True
        elif elements["fragments"] >= 250:
            print("Valanyr obtained!")
            elements["fragments"] -= 250
            obtained = True
        elif elements["motes"] >= 250:
            print("Dragonwrath obtained!")
            elements["motes"] -= 250
            obtained = True
        if obtained:
            break

for material, values in elements.items():
    print(f"{material}: {values}")