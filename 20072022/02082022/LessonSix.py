import math



#функции

#функция всегда начинается со слова def
#
#
# a = 10
# b = 20
#
# # def sum_two_numbers(a, b):       #функци может принимать параметры и может не принимать  в скобках могут быть параметры / аргументы . a и b
# #     print(a + b)
# #
# # sum_two_numbers(1, 2) # вызов функци без скобок ошибки не будет но и не будет вывода функции #складывает только те которые мы доабвили в скобки
# # sum_two_numbers(a, b)
#
# x = 10
# y = 20
#
# # def sum_two_numbers():
# #     x = 5          #считает сначада в внутри функции если данных нет ищет из функции
# #     y = 1
# #     print(x + y)
# #
# # sum_two_numbers()
#
# # def sum_two_numbers():
# #     x = 5
# #
# #     print(x + y)  # даже если в нутри есть функция но она лишь одна вторую будет брать из функции
# #
# # sum_two_numbers()
# #
# # def sum_two_numbers():
# #     global x
# #     x +=10 #нужно обявить его глобальным  x = x + 10 ( x = 10+ 10)
# #
# #     print(x + y)  # даже если в нутри есть функция но она лишь одна вторую будет брать из функции
# # x = 10
# # y = 20
# #
# # sum_two_numbers()
# #
# # print(x)
#
#
# # def no_parameters():
# #     x = double(200) ** 2
# #
# #     return x #функция которая может возвращать
# #
# #
# #
# # def double(number):
# #     return number * 2
# #
# # print(double(10))
# # print(no_parameters())
# #
# #
# # students = {'name': 'Jack', 'surname': 'Smith', 'age': 30, 'courses':['Art', 'Math', 'Programming']}
# #
# # def greet_student(data):
# #     print(f'Hello {data["name"]} {data["surname"]}. You are {data["age"]} years old. Your subjects are {",".join(data["courses"])}.')  #join добавляет
# #
# # greet_student(students)
#
# # def tester(a, b, c=10, *args, **kwargs):
# #     print(a, b, c)
# #     print(args)  #агрументы без ключа
# #     print(kwargs) #агрументы с ключа
# #
# # tester(10, 20, 30, 5, 45, 74, name='Jack', surname='Smith')
#
#
# # программа по подсчету материала
# def perimeter(width, height):
#     return (width + height) * 2
#
#
# def area(width, height):
#     return width * height
#
#
# def count_materials(order):
#     result = {}
#     for key in order:
#         result[key] = [perimeter(order[key][0], order[key][1]) * order[key][2],
#                        area(order[key][0], order[key][1],) * order[key][2]]
#
#     return  result
#
# def count_total_materials(materials_dict):
#     total_p, total_a = 0, 0
#     for key in materials_dict:
#         total_p += materials_dict[key][0] /100 #высчитаываем см
#         total_a += materials_dict[key][1] /1000 #выситываем квадтраные см
#     return [total_p, total_a]
#
# carpets = {'small': [60, 60, 15],'medium':[60, 90, 47], 'large':[90, 90,  20], 'xlarge':[125, 125, 5]}
#
# def main():
#     user_choice = input('1.Material by type\n2. Total material\n-->')
#     if user_choice == '1':
#         print(count_materials(carpets))
#     elif user_choice == '2':
#         print(count_total_materials(count_materials(carpets)))
#     else:
#         quit()
#
# main()
#
#


# домашка создать функции для вывода исикукода ,



print('Hi please enter your name ')
user_name = input("Name : ")
last_name = input("Last name : ")
age = input("Age : ")
print( 'Hello ' + last_name + ' ' + user_name + '.' + 'Your age is '  + age)



a = 3
b = 4
c = None


hypotenuse = c = math.sqrt(a * a + b * b)

print(int(hypotenuse))



a  = float(input('Enter first lenght '))  #6
b  = float(input('Enter second lenght ')) #8
c = float(input('Enter third lenght '))   #10

trianlge =(c*c == a * a + b * b )
print(trianlge)


user = input(['Enter list'])

print(user[::-1])


a = ('1', '2', '3', '5', '8')
b = ('8', '2', '5')

a = list(a)
a.insert(2, b[2])
a.insert(2, b[1])
a.insert(2, b[0])
a = tuple(a)


print(a)
