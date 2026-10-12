#objectif : Read 20 integers and display their total sum.

total_animals = 0

for _ in range(20):
    nb_animals = int(input())
    total_animals = total_animals + nb_animals

print(total_animals)