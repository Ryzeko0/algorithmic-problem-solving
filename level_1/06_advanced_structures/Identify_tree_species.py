# Objective: Identify a tree species from its height and number of leaflets.

height = int(input())
number_of_leaflets = int(input())

if height <= 5:
    if number_of_leaflets >= 8:
        print("Tinuviel")
if height >= 10:
    if number_of_leaflets >= 10:
        print("Calaelen")
if height <= 8:
    if number_of_leaflets <= 5:
        print("Falarion")
if height >= 12:
    if number_of_leaflets <= 7:
        print("Dorthonion")