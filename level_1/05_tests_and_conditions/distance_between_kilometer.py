# Objective: Read two kilometer markers and print the positive distance between them.

borneOne = int(input())
borneTwo = int(input())

if borneOne <= borneTwo:
   print(borneTwo - borneOne)
else:    
   print(borneOne - borneTwo)