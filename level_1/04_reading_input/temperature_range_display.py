#objectif : Display all temperatures between a minimum and maximum value, inclusive.

min_temp = int(input())
max_temp = int(input())

current_temp = min_temp

while current_temp <= max_temp:
    print(current_temp)
    current_temp = current_temp + 1