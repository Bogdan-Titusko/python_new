# # Комментарий   (выеделение большого количества строк в комментарии комбинаци ctrl + /

'''
print(type(500)) #Метод определения типа данных = type  (int = integer - целое число)
print(type('Hello')) #Метод определения типа данных = type  (str = string - строка)
print(type('1234.5'))#Метод определения типа данных = type  (str = string - строка) так как цисла находятся в кавычках ' 1324 '
print(type(20.3)) #Метод определения типа данных = type  (float - дробное число )
print(type(True))#Метод определения типа данных = (Bool- boolean -истинное значение)
print(type(False))#Метод определения типа данных = (Bool- boolean -отрицательное значение)
print(type(None))#Метод определения типа данных = (None -  ничего)

#Переменные никогда не начинаются с цифры
number = 10
print(number)
text = "Hello"
print(text)


# + #addition  x + y
# - #subtraction  x - y
# * #multiplication x * y
# / divisoin x / y
# % moduls x % y
# ** exponentiation x ** y
# // floor division x // y


a =  20
b = 5

print(str(a + 100 + 200 +  b ) + ': Hello world ')

s1 = 'Hello'
s2 = 'Roman'
print(s1 + s2)
print(s1 + s2 * 3)
print(('world '+  "-") * 20)
print(('world '+  "\n") * 20) #перенос строки \n





#Operators операторы
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)


a = 100
b = 20
print(a / b)
print(type(a / b))
print(a // b)
print(type(a // b)) #// округление

print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))


print(((5 + 5) * 2 ) ** 2)
print(500 // 200)
print(200 % 500 ) # 200+200+100


int_var = 500
float_var = 100.123
string_var_txt = 'Hello World'
string_var_num = '123'

#print(float(string_var_num)) #конвертация строки str в тип данных float

#print(str (int_var + float_var ) +'\n' + string_var_txt +'\n' + string_var_num ) #конвертнация числовых типов int в строку str с выносом на другие строки
#print(float_var - int(string_var_num)) #конвертация строки str с числовым значением в  тип данных int с выводом числового значения
#print(float(int_var + float(string_var_num)))#конвертация  числового значения int и строки str в тип данных float
#print(int(string_var_num))#конвертация строки str с чилосвым значением в тип данныъ int
print(float(False))
print(float(True))



print(bool(1))
print(bool(0))
print(bool('text'))
print(bool(''))
print(bool(None))


print('Hello ' + str(123456) + ' ' + str(True) + str('123.12'))
print('Hello', 13224 , + + True , None)


#shift + enter перенос строки без задевания текста


print('Hello world' , end =' ')

print('Hello planet')



print('Hi please enter your name ')
user_name = input("Name : ")
last_name = input("Last name : ")
age = input("Age : ")
print( '\n' + user_name + '\n' + last_name + '\n' + age)



side_a = float(input('Enter side A :'))
side_b = float(input('Enter side B :'))
side_c = float(input('Enter side C :'))

half_perimetr = (side_a + side_b + side_c ) / 2
print(half_perimetr)
triangle_area = half_perimetr * (half_perimetr - side_a) *\
                (half_perimetr - side_b) * (half_perimetr - side_c) ** 0.5
print('The area of triangle is : ' + str(triangle_area))

#comments asdasd asd asd asd
'''

print('Hello ', True , None , 123123, sep='__')







