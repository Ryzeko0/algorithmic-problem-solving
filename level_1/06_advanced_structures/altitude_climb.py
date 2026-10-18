# Objective: Read altitude variations and print the total climb and the total descent.

nbSections = int(input())
totalClimb = 0
totalDescent = 0

for _ in range(nbSections):
    variation = int(input())
    if variation > 0:
        totalClimb = totalClimb + variation
    elif variation < 0:
        totalDescent = totalDescent - variation

print(totalClimb)
print(totalDescent)