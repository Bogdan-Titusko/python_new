import datetime
"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

print(datetime.datetime.strptime(sample1, '%b %d %Y %H:%M%p'))
print(datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d'))
print(datetime.datetime.strptime(sample3, '%A, %B %d, %Y'))
print(datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S'))

# Write a program to print yesterdays, today and tomorrow dates
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days = 1)
tommorow = today + datetime.timedelta(days = 1)
print(f'Yesterday : {yesterday} \nToday : {today}\nTommorow {tommorow} ')


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
print(datetime.datetime.fromtimestamp(some_day))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

def main():
    time_stamp=int(input('Enter time stamp: '))
    time = datetime.datetime.fromtimestamp(time_stamp)
    two_weeks = time - datetime.timedelta(days = 14 )
    new_time_stamp = two_weeks.timestamp()
    print(f'Your new timestamp is : {new_time_stamp}\nGMT input time is :{time}\nGMT output time is :{two_weeks} ')

main()


