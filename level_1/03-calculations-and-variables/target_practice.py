#objectif : Calculate and display the cumulative sum of candies earned over 50 shots.

total_candies = 0
current_shot = 0

for _ in range(50):
   current_shot = current_shot + 1
   total_candies = total_candies + current_shot
   print(total_candies)
