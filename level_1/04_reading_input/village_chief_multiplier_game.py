#objectif : Calculate and display a sequence of numbers with an incrementing multiplier.

number = int(input())
value = 66
multiple = 2 

for _ in range(number):
   print(value)
   value = value * multiple 
   multiple = multiple + 1
