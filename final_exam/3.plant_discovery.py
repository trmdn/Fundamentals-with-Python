number_of_pants = int(input())

plant_info = {}
rarity_d, rating_d = "Rarity", "Rating"
for plant in range(number_of_pants):
    plant_name, plant_rarity = input().split("<->")
    plant_info[plant_name] = plant_info.get(plant_name, {})
    plant_info[plant_name][rarity_d] = float(plant_rarity)
    plant_info[plant_name][rating_d] = []


def check_plant_name(plant_name):
    if plant_name not in plant_info:
        print("error")
        return
    return True


def rate_plant(plant_name, plant_rating):
    if check_plant_name(plant_name):
        plant_info[plant_name][rating_d].append(plant_rating)


def update_plant(plant_name, new_rarity):
    if check_plant_name(plant_name):
        plant_info[plant_name][rarity_d] = new_rarity


def reset_plant(plant_name):
    if check_plant_name(plant_name):
        plant_info[plant_name][rating_d] = []


def show_result():
    print("Plants for the exhibition:")
    for plant in plant_info:
        average = 0.00
        if sum(plant_info[plant][rating_d]) != 0:
            average = sum(plant_info[plant][rating_d]) / len(plant_info[plant][rating_d])
        print(
            f"- {plant}; Rarity: {plant_info[plant][rarity_d]:.0f}; Rating: {average:.2f}")


command = input()

while command != "Exhibition":
    if "Reset" in command:
        _, plant_name = command.split(": ")
        reset_plant(plant_name)
        command = input()
        continue
    plant_name, rating_or_rarity = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]
    if "Rate" in command:
        rate_plant(plant_name, rating_or_rarity)
    elif "Update" in command:
        update_plant(plant_name, rating_or_rarity)
    command = input()

show_result()