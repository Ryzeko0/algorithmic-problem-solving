# Objective: Read the distances walked each day and print the longest one.

nbDay = int(input())
longestDistance = 0

for _ in range(nbDay):
    distance = int(input())
    if distance > longestDistance:
        longestDistance = distance

print(longestDistance)