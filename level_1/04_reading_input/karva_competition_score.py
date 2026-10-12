#objectif : Calculate and display the score of competing Karvas based on their attributes.

nb_comp = int(input())

for _ in range(nb_comp):
    weight = int(input())
    age = int(input())
    horn_length = int(input())
    height_at_the_withers = int(input())
    print(horn_length * height_at_the_withers + weight)