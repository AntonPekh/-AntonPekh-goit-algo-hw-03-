from datetime import datetime

curency_date= '2020-10-09'

get_days_from_today=datetime.strptime(curency_date, '%Y-%m-%d').date()

today_date=datetime.now().date()


diff_day=((get_days_from_today-today_date).days)

print(diff_day)








