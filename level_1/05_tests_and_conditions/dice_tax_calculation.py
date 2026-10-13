# Objective: Read two dice values and print the special or regular tax with the amount to pay.

diceOne = int(input())
diceTwo = int(input())

if diceOne + diceTwo >= 10:
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print((diceOne + diceTwo) * 2)