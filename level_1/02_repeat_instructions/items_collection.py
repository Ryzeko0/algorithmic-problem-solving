# Objective: Collect items across 15 cases using a loop and drop them at the final position.

from robot import *

for loop in range(15):
   droite()
   ramasser()
droite()
deposer()