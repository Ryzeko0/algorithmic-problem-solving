# Objective: Calculate and display the cumulative distances for a 3-day algoreathlon.

run = 2 + 34 + 6
daily = run

for _ in range(3):
   print(daily, end = " ")
   daily = daily + run
