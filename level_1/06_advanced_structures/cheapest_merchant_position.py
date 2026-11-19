# Objective: Find the position of the cheapest merchant, taking the last one in case of a tie.

nbMerchant = int(input())
min_price = 1000000
min_price_position = 0

for i in range(nbMerchant):
    galette_price = int(input())
    if galette_price <= min_price:
        min_price = galette_price
        min_price_position = i + 1

print(min_price_position)