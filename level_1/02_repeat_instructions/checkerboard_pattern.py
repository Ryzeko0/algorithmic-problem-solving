# Objective: Print a 40x40 checkerboard pattern alternating 'O' and 'X'.

for _ in range(20):
   for _ in range(20):
      print("OX", end = "")
   print("")
   for _ in range(20):
      print("XO", end = "")
   print("")
   