from math import  sqrt
# Написать программу которая:
# 	1. Высчитывает возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
# 	2. Найти недостающую часть кода (code_2)
# 		a. найдите остаток от x деленого на y
# 		b. полученый результ умножте на 13
# 		c. извлеките квадратный корень из полученного результата
# 		d. возьмите целую часть от результа
# 	3. Соединить код в отдельную переменную
# 	    пример:
# 	        475-12-967
# 	4. Вывести строку:
# 		пример:
# 			Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.

# years
current_year = 2022
year_of_birth = 1988
#age = current_year - year_of_birth

# code parts
code_1 = '354'
code_3 = 132


# name
user_name = 'John'
user_surname = 'Smith'
#full_name  = user_name + ' ' + user_surname

# code 2 data
x = 152
y = 132
code_2 = int(x % y * 13) ** 0.5
#code_2 = sqrt(code_2)
code_2 = int(code_2)

secret_code = (int(code_1),code_2,code_3,)  #надо было str(code_1) + '-' + str(code_2) + '-' + str(code_3)





print('Hello ' + user_name ,  user_surname + '.You are', current_year - year_of_birth , 'years old.' + 'Your secret code is ',end='')
print(*secret_code,sep='-',end='.')







#a = 'Hello '
#b = '.You are '
#c = ' years old.'
#d = 'Your secret code is '

#print(a + full_name + b + str(age) + c + d , end='' )
#print(*secret_code,sep='-',end='.')
