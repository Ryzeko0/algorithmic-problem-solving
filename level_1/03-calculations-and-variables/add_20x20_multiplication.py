#objectif : Generate and display a 20x20 multiplication table.

row = 1

while row <= 20:
    column = 1
    while column <= 20:
        print(row * column, end=" ")
        column = column + 1
    print()
    row = row + 1