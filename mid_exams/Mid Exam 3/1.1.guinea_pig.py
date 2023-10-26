def pig(food_kg, hay_kg, cover_kg, pig_kg):
    feed_eaten = 0

    for days in range(1, 31):
        feed_eaten += 300
        food_kg -= 300

        if days % 2 == 0:
            hay = food_kg * 0.05
            hay_kg -= hay
            feed_eaten -= hay_kg
        if days % 3 == 0:
            cover_kg -= cover

    if food_kg > 0 and hay_kg > 0 and cover_kg > 0:
        return f"Everything is fine! Puppy is happy! Food: {food_kg / 1000:.2f}, Hay: {hay_kg / 1000:.2f}, Cover: {cover_kg / 1000:.2f}. "
    else:
        return "Merry must go to the pet store!"


food_in_kg = float(input()) * 1000
hay_in_kg = float(input()) * 1000
cover_in_kg = float(input()) * 1000
pig_in_kg = float(input()) * 1000

cover = pig_in_kg / 3

result = pig(food_in_kg, hay_in_kg, cover_in_kg, pig_in_kg)
print(result)