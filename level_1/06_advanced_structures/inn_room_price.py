# Objective: Compute the room price based on age and luggage weight.

age = int(input())
luggage_weight = int(input())

price = 30

if age == 60:
    print(0)
elif age < 10:
    print(5)
else:
    if luggage_weight >= 20:
        print(price + 10)
    else:
        print(price)