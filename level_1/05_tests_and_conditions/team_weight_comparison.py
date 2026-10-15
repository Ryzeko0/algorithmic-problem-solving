# Objective: Read the weights of two alternating teams, compute their totals and print which team has the advantage.

nbPlayer = int(input())
team1 = 0
team2 = 0

for _ in range(nbPlayer):
    weight = int(input())
    team1 = team1 + weight
    weight = int(input())
    team2 = team2 + weight

if team1 > team2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 :", team1)
print("Poids total pour l'équipe 2 :", team2)