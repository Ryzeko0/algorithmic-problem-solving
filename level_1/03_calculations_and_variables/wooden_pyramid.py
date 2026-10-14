#objectif : Calculate and display the total number of wooden cubes needed to build the pyramid.

side_lenght = 17
total_cube = 0

while side_lenght >= 1:
   total_cube = total_cube + (side_lenght * side_lenght * side_lenght)
   side_lenght = side_lenght - 2
print(total_cube)