
#В ПАЙТОНЕ ЛЮБОЙ ОТЧЕТ ЧЕГО ЛИБО НАЧИНАЕТСЯ С 0
#len - измеряет длинну строки
# string_sample = 'Hello world world'
#                 #01234 56789
#                 #        -5-4-3-2-1
# string_sample2 = 'first letteR is lowErcase'
# string_sample3 = '**extra  whitespace  string ,,,'
#german_sample = 'def Fluß'

#[START : END : STEP ]
# print(string_sample[0])
# print(string_sample[-1])
#
# print(string_sample[4:11]) #[START : END]
# print(string_sample[-5 : -1 ])  #логика остается с лева на право [ -1 : -5 ] не будет выдавать значение
# print(string_sample[:10]) # Когда отсутсвует значение start берем с начало строки и до 10 го символа в этом примере
# print(string_sample[5:]) # тоже самое только отсутсвует значени end
# print(len(string_sample))
#
# print(string_sample[1:14:2]) # третье значение обозначает шаг [ : STEP ] тоесть каждое второе значение будет выдаваться
# print(string_sample[::3])
# print(string_sample[::-3])
#
#
# new_str = string_sample[:5] + ' ' + string_sample2[:5]
# print(new_str)



# print('word' in string_sample)  #проверяет есть ли данное слово 'word' в переменной  string_sample
# print('world' in string_sample) #проверяет есть ли данное слово 'world' в переменной  string_sample
# print('World' in string_sample) #Большая буква не тоже самое что маленькая
#
# print(string_sample.upper()) #На выходе получаем строку только в заглавных буквах
# print(string_sample.lower()) #На выходе получаем строку только с  прописными буквами
# print('WORLD' in string_sample.upper()) #значение верно так как мы задаем команду чтоб текст стал заглавный
#
#
# print(len(german_sample.lower())) # метод lower
#print(german_sample.casefold()) #метод casefold

# print(string_sample[4:8].lower())
# print(string_sample[4:8].upper())
#
# print('Hello World'.upper())
# print('Hello World'.lower())
#
# user_name = input('Enter name ').upper()
# print(user_name)
# user_name1 = input('Enter name ').lower()
# print(user_name1)

# print('hello world'.upper())
# print(string_sample2.capitalize())#делает первую букву заглавную ,остальные остаются в писмьемнной форме,не работает на предложения!
#
# print(string_sample.title())#делает  заглавную букву в каждом слове.
# print('hELLO hOW aRe yOU'.title())#делает  заглавную букву в каждом слове.а остальные остаются в нижнем регистре.
#
#
# print(string_sample.title().capitalize().upper().lower())



#print(string_sample3.strip()) #метод strip удаляет пробелы в начале и в конце строки  ()
# print(string_sample3.strip('*')) #метод strip удаляет пробелы в начале и в конце строки  *
# print(string_sample3.lstrip('*'))
# print(string_sample3.rstrip(','))
# print(string_sample.replace('world', 'planet ')) #можем модифицировать с помощью команды replace удалять , добавлять
# print(string_sample.replace('world','planet'))


#
# print('123123123'.zfill(10))  # заполняем нулями
#
# print(string_sample2.swapcase()) #меняем большие буквы на маленькие а маленькие на большие !


# print(string_sample.count('world')) #метод count показывает как часто встречаются слова в предложении
# print(string_sample.count('l')) #сколько букв l считает
#print(string_sample.count('world', 2 , 11 ))

# print(string_sample.find('world' , 7))#мето find находит первое подходящее  слово, или начинает искать с 7 строки первое подхожящее слово,и получается что на 12 строчке у нас находит слово world

#список
# # a , b , c =[1 , 2 ,3 ]
# # print(a)
# # print(b)
# # print(c)
# print(string_sample.split())
# a, b, c = input('Enter sides A, B and C:').split(', ')
# print(a, b, c)




# a = 'Hello'
# b = 'World'
# #
# # sample = """Hello
# # world"""     #\t 4 пробела \n перенос строки
# # print(sample)
# # print(len(sample))
#
#
#
# print('First word is ' + a)
# print(a, b, False, None, 1231231)
# sample_str = a +str(True) +b
# print(sample_str)


# salary = 1000
# salary_msg = '{1} salary is {0}.'
# print(salary_msg.format('Johns', salary))

# salary_msg ='This {product:} costs {price:.2f}$'
# print(salary_msg.format(price=1000, product='computer'))
#
#
# name = 'Jack'
# surname = 'Smith'
#
#
#
#
# employed = True
# salary = 2000
#
# print(f'This is {name} {surname}. It s {employed} thath he is employed. His salary is {salary:.2f}$ ')
#




# if elif else


# x = input('How old are you :')
#
# if x < str(15):
#     print('You are child!')
# elif x < str(18):
#     print('You are teenager')
# else:
#     print('You are adult!')
#
#
# print('Goodbye')



#
# isikukood = input('Please enter national ID:')
#
# if len(isikukood) == 11:
#     print('Your id :' + isikukood)
# elif len(isikukood) > 11:
#     print('Your ID is too long')
# else:
#     print('Your ID is too short')



