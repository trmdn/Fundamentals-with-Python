number_of_pieces = int(input())

music_info = {}


def piece_exists(piece_name):
    if piece_name in music_info:
        return True
    return False


def add_music_info(piece_name, composer_name, key_name, first_input):
    if piece_exists(piece_name):
        if not first_input:
            print(f"{piece_name} is already in the collection!")
            return
    if not piece_exists(piece_name):
        music_info[piece_name] = music_info.get(piece_name, {})
        music_info[piece_name][key_name] = composer_name
        if not first_input:
            print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")


def remove_music_info(piece_name):
    if piece_exists(piece_name):
        del music_info[piece_name]
        print(f"Successfully removed {piece_name}!")
        return
    print(f"Invalid operation! {piece_name} does not exist in the collection.")


def change_key(piece_name, key_name):
    if piece_exists(piece_name):
        _, name_compositor = music_info[piece_name].popitem()
        music_info[piece_name] = {}
        music_info[piece_name][key_name] = name_compositor
        print(f"Changed the key of {piece_name} to {key_name}!")
        return
    print(f"Invalid operation! {piece_name} does not exist in the collection")


def show_result():
    for piece_name in music_info:
        for key_name, composer_name in music_info[piece_name].items():
            print(f"{piece_name} -> Composer: {composer_name}, Key: {key_name}")


for piece in range(number_of_pieces):
    piece_name, composer_name, key_name = input().split("|")
    add_music_info(piece_name, composer_name, key_name, True)


command = input()

while command != "Stop":
    command_type, *info = command.split("|")
    if command_type == "Remove":
        piece_name = info[0]
        remove_music_info(piece_name)
    elif command_type == "Add":
        piece_name, composer_name, key_name = info
        add_music_info(piece_name, composer_name, key_name, False)
    elif command_type == "ChangeKey":
        piece_name, new_key = info
        change_key(piece_name, new_key)

    command = input()

show_result()