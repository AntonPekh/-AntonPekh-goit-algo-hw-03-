from random import randint

min=1
max=49
quality=6

get_numbers_ticke= set()

while len(get_numbers_ticke) !=6:
    get_numbers_ticke.add(randint(min,max))

print(sorted(list(get_numbers_ticke)))
