def office_chairs(number_of_rooms):
    free_chairs = 0

count_of_rooms = int(input())
total_free_chairs = office_chairs(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")