# Objective: Move the robot 108 times around a 13x13 perimeter using sequential directional loops.

from robot import *

for _ in range(108):
   for _ in range(13):
      haut()
   for _ in range(13):
      droite()
   for _ in range(13):
      bas()
   for _ in range(13):
      gauche()