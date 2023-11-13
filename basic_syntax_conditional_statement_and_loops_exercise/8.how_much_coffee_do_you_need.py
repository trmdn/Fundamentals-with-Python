events = input()
coffee_count = 0

while events != "END":

    if events.lower() == "coding" \
            or events.lower() == "cat" \
            or events.lower() == "dog" \
            or events.lower() == "movie":
        if events.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    events = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)