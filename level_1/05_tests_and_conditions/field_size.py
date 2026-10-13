# Objective: Compare two field areas and print which family has a field larger by more than 10 m².

arignon_field = int(input())
evaran_field = int(input())

if arignon_field - evaran_field > 10:
    print("La famille Arignon a un champ trop grand")
if evaran_field - arignon_field > 10:
    print("La famille Evaran a un champ trop grand")