fire_size = input().split("#")
water = int(input())
effort, total_fire = 0, 0
cells = []

for i in range(len(fire_size)):
    split_cell = fire_size[i].split()
    value = int(split_cell[-1])
    if water >= value:
        if split_cell[0] == "High":
            if 81 <= value <= 125:
                water -= value
                total_fire += value
                effort += value * 0.25
                cells.append(value)
            else:
                continue
        elif split_cell[0] == "Medium":
            if 51 <= value <= 80:
                water -= value
                total_fire += value
                effort += value * 0.25
                cells.append(value)
            else:
                continue
        elif split_cell[0] == "Low":
            if 1 <= value <= 50:
                water -= value
                total_fire += value
                effort += value * 0.25
                cells.append(value)
            else:
                continue

print("Cells:")
for i in range(len(cells)):
    print(f" - {cells[i]}")
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')