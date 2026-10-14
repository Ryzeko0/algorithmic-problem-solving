#objectif : Fetch and return 10 rings one by one to the starting square.

from robot import *

move_forward = 1

for _ in range(10):
   for _ in range(move_forward):
      droite()
   ramasser()
   for _ in range(move_forward):
      gauche()
   deposer()
   move_forward = move_forward + 1 