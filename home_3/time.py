#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
from datetime import datetime, date, timedelta


dt_now = datetime.now()
print(dt_now.strftime('%H:%M %d/%m/%Y'))

delta = timedelta(days = 1)
delta_m = timedelta(weeks = 4, days = 3)

y = dt_now - delta
print(y.strftime('%H:%M %d/%m/%Y'))

m_ago = dt_now - delta_m
print(m_ago.strftime('%H:%M %d/%m/%Y'))

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)