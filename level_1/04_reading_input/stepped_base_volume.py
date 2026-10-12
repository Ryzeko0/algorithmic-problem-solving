#objectif : Calculate and display the total volume of a stepped base.

base = int(input())
upper_base = int(input())
volume = 0

while base >= upper_base:
    volume = volume + (base * base)
    base = base - 1

print(volume)