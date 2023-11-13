quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
pigs_weight = float(input()) * 1000

cover = pigs_weight / 3
feed_eaten = 0

for day in range(1, 31):
    feed_eaten += 300
    quantity_of_food -= 300
    if day % 2 == 0:
        hay = quantity_of_food * 0.05
        quantity_of_hay -= hay
        feed_eaten += hay
    if day % 3 == 0:
        quantity_of_cover -= cover

if quantity_of_food > 0 and quantity_of_hay > 0 and quantity_of_cover > 0:
    print(
        f"Everything is fine! Puppy is happy! Food: {quantity_of_food / 1000:.2f}, "
        f"Hay: {quantity_of_hay / 1000:.2f}, "
        f"Cover: {quantity_of_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
