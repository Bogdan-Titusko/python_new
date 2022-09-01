#import calendar     # библиотеки
#from math import pi, sqrt
#from math import * # все методы библиотеки
#from math import  pi as math_pi  # даем новое название методу
import time
import calendar
import datetime

#rint(calendar.month(2022, 10, w=10, l=2))
#print(calendar.calendar(2022, w=4, l=2, c=0, m=4 )) # w ширина l высота c   расстояние между  месяцами m сколько месяцев в одной строке

#print(calendar.weekday(2022, 8, 10)) #опеределяет день недели 0 понедельник - 1 вторник 2 среда и т.д

# print(calendar.isleap(2023)) #  будет ли високосный год
#
# print(calendar.leapdays(2000, 2020)) #количество високосных лет

# print('Hello')
# time.sleep(7) #пауза вывода последующего действия
# print('Good bye')



# start = time.time()  # start   время которое выводится это время в секундах которое начинало свой отчет 1 января 1970 года  53 года назад
# print(time.time())
# #time.sleep(5)
# stop = time.time()
# print(stop - start)

# print(time.asctime()) # вывод дня месяца  числа  времени и года  #невозоможно изменить

# print(time.gmtime())
# print(time.localtime()[1])  # 0 год 1 месяц 2 день 3 час 4 минута 5 секунда 6 день недели 7 день года 8 летнее зимнее время
#
# print(time.tzname)

# d = datetime.date(2022, 5, 12)  # год месяц число правильно так
# print(d)
# print(type(d))

# today = datetime.date.today()
# # print(today)
# # print(type(today))
# # print(today.year, today.month, today.day)
# print(today.weekday())
# print(today.isoweekday())
#
# x = today - d
# print(x)
# print(type(x))

today = datetime.date.today()
#
# tdelta = datetime.timedelta()
# date1 = datetime.date(2015, 5, 12)
# date2 = datetime.date(2018, 5, 12)
# print(date1 - date2)
#
# tdelta = datetime.timedelta(weeks=4)
# print(tdelta)
#timedelta i date отдельные друг от друга и по разному вывод дают



# date1 - date2 = timedelta
# date1 - timedelta =date2
# date2 + timedelta = date1

# next_bday = datetime.date(2022, 10, 17)
# print((next_bday - today).days)



dt = datetime.datetime(1960, 5, 12, 10, 30, 45)
today = datetime.datetime.now()
# print(today)
# print(dt.year, dt.hour)
# print(dt.date)
# print(dt.time)
# print(type(dt.time()))
# print(type(dt.date))

# print(today - dt)
# print(type(today - dt))

# print(today + datetime.timedelta(hours=24, minutes=0))
# print(today.timestamp())#возомжонсть приставить дату в юникс тиме штамп
# tstamp = 1659979476.596315 # отрицаттельного штампа быть не может
# print(datetime.datetime.fromtimestamp(tstamp))


#timedelta показывает в днях
# print( today - dt)
# print((today - dt).days // 365.25) # в годах  1960 - 2022 получаем  кол- во дней и получаем в годах


print(today)
print(today.strftime('%d %B %y'))      #   представление даты в строку. #%с вывод локальныого форматы вывода даты  https://docs.python.org/3/library/time.html#module-time


date1 = 'November 30, 2020, 10:30pm'


print(datetime.datetime.strptime(date1, '%B %d, %Y, %I:%M%p')) # НУЖНО ОДИН В ОДИН ПОВТОРИТЬ ЧТО В ПЕРЕМЕННОЙ ЗА ДАТА НА ВЫХОДЕ БУДЕТ ОНА ВЫГЛЯДИТЬ ПО ДРУГОМУ  ДАНО 'November 30, 2020, 10:30pm' ВЫВОД 2020-11-30 22:30:00


date2 = '8. Juuni 2022, 18:06'
date2 = date2.replace('Juuni', 'June')
print(datetime.datetime.strptime(date2, '%d. %B %Y, %H:%M'))