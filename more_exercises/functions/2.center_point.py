import math


def center_point(arg_one, arg_two):
    if arg_one <= arg_two:
        return f"({x1}, {x2})"
    elif arg_two <= arg_one:
        return f"({y1}, {y2})"


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))

result = center_point(sum_x, sum_y)
print(result)