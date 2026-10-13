# Objective: Compute the room price based on arrival time, capped at a maximum of 53.

arrival_hour = int(input())

price = 10 + 5 * arrival_hour
if price > 53:
    price = 53

print(price)