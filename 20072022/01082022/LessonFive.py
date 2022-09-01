# people =[('Jack', 'Smith', 30, 'male'), ('Sarah', 'Gold', 25, 'female'),
#          ('Mary', 'Summers', 20, 'female'), ('Bob', 'Dyllan', 25, 'male') ]
#
# for person in people:
#     print(f'This is  {person[0]} {person[1]}. He is {person[2]} years old.')
# else:
#     print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')
#
#
#     for name, surname , age, gender in people:
#         if gender == 'male':
#             print(f'this is {name} {surname}. he is {age} years old')
#         else:
#             print(f'this is {name} {surname}. She is {age} years old.')
#



# while True:
#     print('I can\'t stop!')
#
# x = 0
# while x < 100:
#     print(x ** 2)
#     x += 1

# x = 2
# while x < 100:
#     print(x ** 2)

# distance_to_target = float(input('Please enter distance in km: '))
# step = 0.8
# step_cnt = 0
#
# current_postition = 0
#
# while current_postition < distance_to_target * 1000:
#     print(step_cnt)
#     current_postition += step
#     step_cnt += 1

# condition = True
# while condition:
#     isikukood = input('Please enter ID:  ')
#     if len(isikukood) != 11:
#         if len(isikukood) >11:
#             print('iD Is too long')
#             continue
#         else:
#             print('Id is too short')
#             continue
#     else:
#             print('your id is ' + isikukood)
#     break
#     print("Somethig")
#
# print("Good bye")

# break #полный разрыв цикла для разрыва цикла  в if не работают
        # continue # разывает опеределанный круг и продолжает следующий цикл   в if не работают
        # pass  в if не работают

# for letter in 'We learn python':
#     if letter == 'y':
#         print(letter)
#
#
#
#

#

# for num in range(0, 101):
#     if num % 12 == 0:
#         print(num, 'Something')
#         continue
#     elif num % 15 == 0:
#         print(num, 'FizzBuzz')
#         continue
#     elif num % 3 == 0:
#         print(num, 'Fizz')
#         continue
#     elif num % 5 == 0:
#         print(num, 'Buzz')
#         continue




# user_choice = input('Hi:    ')
# if user_choice == '1':
#     pass#ignoriruet oststcuie koda
# elif user_choice == '2':
#     pass
# elif user_choice == '3':
#     print('pass')


# try:
#     user = input('Please enter ID:  ')
#     int(user)
# except:
#     print('Error')
# else:
#     print(user)
# finally:
#     print('Good bye')

#                                                  #https://docs.python.org/3/library/exceptions.html   Errors
# try:
#     user = input('Please enter ID:  ')
#     int(user)
#     if len(user) != 11:
#         if len(user) > 11:
#             print('ID is too long')
#         else:
#             print('Id is too short')
#             raise Exception
# except ValueError:  # ошибка числа
#     print('Error')
# except Exception:  # ошибки длинные
#     print('Error lenght')
# else:
#     print('Your id is ' + user)

# except ZeroDivisionError:
# except ValueError:



#ЦИКЛ

# while True:
#     try:
#         user = input('Please enter ID:  ')
#         int(user)
#         if len(user) != 11:
#             if len(user) > 11:
#                 print('ID is too long')
#             else:
#                 print('Id is too short')
#                 raise Exception
#     except ValueError:  # ошибка числа
#         print('Error')
#     except Exception:  # ошибки длинные
#         print('Error lenght')
#     else:
#         print('Your id is ' + user)





# x = 5
# y = 10
# while x > 0:
#     while y > 0:
#         print(y, 'y')
#         y -= 1
#     print(x, 'x')      #-=
#     x -= 1

# empty_dict = {}
# print(type(empty_dict))
#
x = 5
#
student = {'name': 'Jack', 'age': 32, 'courses':['Math', 'Art', 'Programming'],
           1: 'integer key', 0.23: 'float key', x: 'variable', 'var ley': 5,
           'dict key': {'x': 10, 'y':20}}
           #True: 'Hello world'}
# print(student)
# print(student['name'])
# print(student[1])
# print(student[0.23])
# #print(student[True]) # не стоит использовать так как заберает некторые себе значения себе например 1 является integer key а true присваивает его себе и выдает hello world
# #print(student[1])
# print(student.get('job', None)) #метод гет заменяет обращение через квадртаные скобки.но если вставить то чего не существует метод гет возваращает none. через запятую можно добавить что вернуть

# key = 'job'
# if student.get(key):
#     print(student.get(key))
# else:
#     print(key, 'Not found')
#




# student['name'] = 'John'
# student['phone'] = '555-555-5555'
# print(student)
#
# #student.pop('phone')# не может работать без аргумента # удаляет в словаре ключ требуя значение этого ключа
# deleted = student.pop('phone')
# print(deleted)
# print(student)
#
# deleted = student.popitem() #не можем выбрать что удаляет поп итем удаляет последний элемент в словаре, но не всегда понятен порядок поэтому может удалить любой элемент
# print(student)
# print(deleted)
#
# del student['name'] #метод дел не сохраняет элемент после удаления
# print(student)

student.update({'name': 'John', 'age': 50, 'phone': '555-555-5555'})#метод обновления словаре на несколько значений
# print(student)
# print(bool(student))

# sample = {'one': 1}
# print(bool(sample))

# for val in student:
#     print(val, student[val])


# print(student.keys())


# print(student.items())
# for pair in student.items():
#     print(pair)
#
# for key, values in student.items():
#     print(key, values)
# #
# for key in student.keys(): #кеис возвращают ключи
#     print(key)
#
# for value in student.values(): #значения возвращает
#     print(value)



# student.setdefault('def', 'default')
#
#
# student2 = student.copy() #создает копию
# student2['name'] = 'Bob'
# student['age'] = 13
# print(student['def'])
# print(student)
# print(student2)



#38803160272


# Домашка  исикукод

while True:
    try:
        isikukood = input('Enter your ID: or type exit!:  ')
        if isikukood.lower() == 'exit':
            break
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
    except UserWarning:
        if len(isikukood) > 11:
            print('Code is long')
        else:
            print('Code is short')
            continue
    except ValueError:
        print('Code is not numeric!')
        continue
    else:
        while True:
            user_choice = input('Please choose:\n1.Get gender\n'
                                '2.Get date of birth\n3.Get region of birth\n'
                                '4.Valuidate\n5.Change ID\n'
                                '0.Exit\n--> ')
            if user_choice == '1':
                if isikukood[0] not in ['9', '0']:
                    if int(isikukood[0]) % 2 == 0:
                        gender = 'female'
                    else:
                        gender = 'male'
                    print('You are ' + gender)
                else:
                    print('Unable to determine gender!')
            elif user_choice == '2':
                if isikukood[0] not in ['9', '0']:
                    if isikukood[0] in ['1', '2']:
                        bcent = '18'
                    elif isikukood[0] in ['3', '4']:
                        bcent = '19'
                    elif isikukood[0] in ['5', '6']:
                        bcent = '20'
                    elif isikukood[0] in ['7', '8']:
                        bcent = '21'  # 39710173734
                    print(f'Your date of birth is {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}.')
                else:
                    print('Can\' determine date of birth! ')
            elif user_choice == '3':
                if int(isikukood[7:10]) in range(0, 11):
                    haigla = 'Kuressaare haigla'
                elif int(isikukood[7:10]) in range(10, 20):
                    haigla = 'Tartu Ülikooli Naistekliinik'
                elif int(isikukood[7:10]) in range(20, 151):
                    haigla = ' Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                elif int(isikukood[7:10]) in range(150, 161):
                    haigla = ' Keila haigla'
                elif int(isikukood[7:10]) in range(160, 221):
                    haigla = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
                elif int(isikukood[7:10]) in range(220, 271):
                    haigla = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
                elif int(isikukood[7:10]) in range(270, 371):
                    haigla = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif int(isikukood[7:10]) in range(370, 421):
                    haigla = 'Narva haigla'
                elif int(isikukood[7:10]) in range(420, 471):
                    haigla = 'Pärnu haigla'
                elif int(isikukood[7:10]) in range(470, 491):
                    haigla = 'Haapsalu haigla'
                elif int(isikukood[7:10]) in range(490, 521):
                    haigla = 'Järvamaa haigla (Paide)'
                elif int(isikukood[7:10]) in range(520, 571):
                    haigla = 'Rakvere haigla, Tapa haigla'
                elif int(isikukood[7:10]) in range(570, 601):
                    haigla = 'Valga haigla'
                elif int(isikukood[7:10]) in range(600, 651):
                    haigla = ' Viljandi haigla'
                elif int(isikukood[7:10]) in range(650, 701):
                    haigla = ' Lõuna-Eesti haigla (Võru), Põlva haigla'
                print(f'Your region is {isikukood[7:10]}.{haigla}')
                continue
            if user_choice == '4':
                if int(isikukood[0]):
                    validate = int(isikukood[0]) * 1 + int(isikukood[1]) * 2 + int(isikukood[2]) * 3 + int(
                        isikukood[3]) * 4 + int(isikukood[4]) * 5 + int(isikukood[5]) * 6 + int(isikukood[6]) * 7 + int(
                        isikukood[7]) * 8 + int(isikukood[8]) * 9 + int(isikukood[9]) * 1
                    validate2 = (validate / int(11))
                    validate3 = (int(validate2) * 11)
                    validate4 = (validate - validate3)
                    print(f'Your validate number is :' + str(validate4))
            if user_choice == '5':
                break
            if user_choice == '0':
                print('Good bye')
                quit()














































