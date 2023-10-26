def main():
    sequence_of_elements = input().split()
    count_moves = 0

    while True:
        count_moves += 1
        command = input()

        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break

        index_one, index_two = map(int, command.split())

        if is_invalid_input(index_one, index_two, sequence_of_elements):
            handle_valid_input(sequence_of_elements, count_moves)
        else:
            handle_valid_input(index_one, index_two, sequence_of_elements, count_moves)


def is_invalid_input(index_one, index_two, sequence):
    return (
            index_one == index_two
            or index_one < 0
            or index_two < 0
            or index_one > len(sequence)
            or index_two > len(sequence)
    )


def handle_valid_input(sequence, count_moves):
    mid_index = len(sequence) // 2
    sequence.insert(mid_index, f'-{count_moves}a')
    sequence.insert(mid_index, f'-{count_moves}a')
    print("Invalid input! Adding additional elements to the board")
