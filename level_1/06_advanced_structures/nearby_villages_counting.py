# Objective: Count the villages located at most 50 km from the current position on the road.

position = int(input())
nbVillage = int(input())
nbCloseVillages = 0

for _ in range(nbVillage):
    villagePosition = int(input())

    distance = villagePosition - position
    if distance < 0:
        distance = -distance

    if distance <= 50:
        nbCloseVillages = nbCloseVillages + 1

print(nbCloseVillages)