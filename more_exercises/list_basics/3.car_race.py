sequence_in_timers = input().split()
timer_as_int = []
for timer in sequence_in_timers:
    timer_as_int.append(int(timer))
middle_timer = len(timer_as_int) // 2
left_racer = timer_as_int[0:middle_timer]
right_racer = timer_as_int[middle_timer + 1:][::-1]

left_time = 0
right_time = 0

for seconds in left_racer:
    left_time += seconds
    if seconds == 0:
        left_time -= 0.2 * left_time
for seconds_two in right_racer:
    right_time += seconds_two
    if seconds_two == 0:
        right_time -= 0.2 * right_time

if left_time > right_time:
    print(f"The winner is right with total time: {right_time:.1f}")
else:
    print(f"The winner is left with total time: {left_time:.1f}")