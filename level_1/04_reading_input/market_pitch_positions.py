#objectif : Calculate and display the positions of market pitches based on starting point, width, and number of sellers.

starting_position = int(input())
pitch_width = int(input())
nb_sellers = int(input())

for _ in range(nb_sellers + 1):
   print(starting_position)
   starting_position = starting_position + pitch_width