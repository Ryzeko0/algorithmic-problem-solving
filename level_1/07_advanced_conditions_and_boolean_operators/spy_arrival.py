# Objective: Count the people who entered the city within a given time interval (inclusive).

start_of_interval = int(input())
end_of_interval = int(input())
nbEntries = int(input())
nb_possible_spies = 0

for _ in range(nbEntries):
    entry_date = int(input())
    if start_of_interval <= entry_date and entry_date <= end_of_interval:
        nb_possible_spies = nb_possible_spies + 1

print(nb_possible_spies)