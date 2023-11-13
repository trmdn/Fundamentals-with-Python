forces = {}

def add_user_to_side(name, side):
    for users in forces.values():
        if name in users:
            return
    forces[side] = forces.get(side, []) + [name]

def switch_side(side, name):
    for sides, users in forces.items():
        if name in users:
            forces[sides].remove(name)
            break
    forces[side] = forces.get(side, []) + [name]
    print(f"{name} joins the {side} side!")


command = input()

while command != "Lumpawaroo":
    if "|" in command:
        side, name = command.split("|")
        add_user_to_side(side, name)
    elif "->" in command:
        side, name = command.split("->")
        switch_side(name, side)

    command = input()

for key, value in forces.items():
    if value:
        print(f"Side: {key}, Members: {len(value)}")
    for values in value:
        print(f"! {values}")
        