# Objective: Count how many places have a population strictly greater than 10,000.

nbPlace = int(input())
nbCities = 0

for _ in range(nbPlace):
    population = int(input())
    if population > 10000:
        nbCities = nbCities + 1

print(nbCities)