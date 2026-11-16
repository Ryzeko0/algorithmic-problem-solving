# Objective: Compute the perimeter of the smallest axis-aligned rectangle enclosing all houses.

house_number = int(input())
max_x = 0
min_x = 1000000
max_y = 0
min_y = 1000000

for _ in range(house_number):
    x = int(input())
    if x >= max_x:
        max_x = x
    if x <= min_x:
        min_x = x
    y = int(input())
    if y >= max_y:
        max_y = y
    if y <= min_y:
        min_y = y

width = max_x - min_x
height = max_y - min_y
print((width + height) * 2)