people = int(input())
places = [int(i) for i in input().split()]

for wagon in range(len(places)):
    max_people = min(4 - places[wagon], people)
    places[wagon] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any([wagon < 4 for wagon in places]):
    print("The lift has empty spots!")

print(*places)
