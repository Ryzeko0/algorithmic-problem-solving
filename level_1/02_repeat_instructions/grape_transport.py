# Objective: Transport grapes by making 20 round trips between position 0 and 15.

from robot import * 

for _ in range(20):
   ramasser()
   for _ in range(15):
      droite()
   deposer()
   for _ in range(15):
      gauche()

