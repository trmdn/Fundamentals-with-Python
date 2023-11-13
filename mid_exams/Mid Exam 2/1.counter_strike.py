initial_energy = int(input())
battles_won_counter = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {battles_won_counter}. Energy left: {initial_energy}")
        break

    if battles_won_counter % 3 == 0:
        initial_energy += battles_won_counter

    distance_to_enemy = int(command)

    if initial_energy >= distance_to_enemy:
        initial_energy -= distance_to_enemy
        battles_won_counter += 1
    else:
        print(f"Not enough energy! Game ends with {battles_won_counter} won battles and {initial_energy} energy")
        break
