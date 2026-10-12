#objectif : Check if the total weight of packages exceeds the limit and print a warning.

nbPack = int(input())
wePack = int(input())

if nbPack * wePack > 105:
   print("Surcharge !")