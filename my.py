# Завдання 1

from datetime import datetime

curency_date= '2020-10-09'

get_days_from_today=datetime.strptime(curency_date, '%Y-%m-%d').date()

today_date=datetime.now().date()


diff_day=((get_days_from_today-today_date).days)

print(diff_day)

###

#Завдання 2

from random import randint

min=1
max=49
quality=6

get_numbers_ticke= set()

while len(get_numbers_ticke) !=6:
    get_numbers_ticke.add(randint(min,max))

print(sorted(list(get_numbers_ticke)))








