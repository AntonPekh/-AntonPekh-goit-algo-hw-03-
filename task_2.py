from random import randint, sample

min= 1
max= 1000
quality= 6


get_numbers_ticket=set()

while len(get_numbers_ticket) !=quality:
    get_numbers_ticket.add(randint(min,max))

print(sorted(list(get_numbers_ticket)))

print(sorted(sample(range(min, max), quality)))

