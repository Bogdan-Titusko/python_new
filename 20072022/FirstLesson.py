from ast import If
import math
from tokenize import Floatnumber
from unicodedata import name

"""
test= 5   #Переменной присвоили значение 5 
test2 = "Bogdan" #Переменной присвоили имя

#Целое число называется int (integer)
age = 24
#Вещественное ,дробное число (Float)
Floatnumber= 5.7
#Строка , text   str
name ='Bogdan'
#Bool Булевое значение /True/False
status = True
#Print  функция ввывода
print('Функция ввывода на экран')
#экранирование , выделяем слово в кавычки
print('Это "человек-паук "был ?')
#Перевод строки
print('Hello \nWorld')
#Кокатенация
print ( 'Привет меня зовут '  +  name + '!')
print('Мне '  + str(age) +  ' года!')#Переводим переменную int 'age' в переменную string
#ТЕСТ
name = input ('Введите свое имя : ')
age = input ('Введите свой возраст : ')

print('Привет ' + name + ' Тебе уже ' + age + ' Года !'  )
#Базовые операции
#+, -, *, /, **, %,унарный минус, округление,Пи

a = 5
b = 10

c = a * b
d = a - b
e = a / b
f = a + b

print(c,d,e,f)
#Унарный минус
a = 10

a = -a
a = -a

print(a)
#Округление
a = 5.65

print(round(a))
print(math.floor(a))
