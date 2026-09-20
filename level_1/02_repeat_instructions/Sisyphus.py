# Objective: Move up 21 steps using (up, right) loops and down using (left, down) loops.

from robot import *

for loop in range(21):
   haut()
   droite()
for loop in range(21):
   gauche()
   bas()
   