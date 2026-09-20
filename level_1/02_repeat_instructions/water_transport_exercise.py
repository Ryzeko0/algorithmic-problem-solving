# Objective: Control the robot using loops to fetch a bucket and deliver it to the house.

from robot import *

for loop in range(2):
    gauche()
print("Bonjour, laissez-moi vous aider")
ramasser()
for loop in range(32):
    droite()
deposer()