# # # empty_list = list('123')
# # # print(type(empty_list))
# # # print(bool(empty_list))
# # #
# # # world = 'Hello world'
# # # filled_list = [123, [1, 2, 3, ['hello', 5, 6], 7], 0.2312, True, None, 'Test', world]
# # # print(len(filled_list))  #дляинна данного списка 7 так как в списке считают елементы а не символы.
# # # # print(filled_list[1][3][0][1:4])
# #
# #
# # cources = ['History', 'Math', 'Literature', 'Physics', 'Progaramming', str(12), '123213', 'asdasdasd','Fsasd']
# # numbers = [1, 5, 6, 8, 3, 4, 2]
# # #
# # # cources[0] = 'Art'
# # # print(cources)
# #
# # # cources.append('Art')  #добавляет один обьект в список
# # # print(cources)
# # # print(cources[3])
# # # cources.insert(0,'English') #добавляем елемент в позицию которую хотим
# # # print(cources)
# #
# # # cources.extend(['English', 'Art'])  #несколько значений может добавить в список
# # # print(cources)
# # #
# # # cources.remove('Math') #удаляет первое попавшийся элемент,если их два в списке второй не удалится
# # # print(cources)
# # #
# # # deleted_item = cources.pop(-2)#удаляет последний аргумент в списке если ему не указали другое значение.
# # # print(cources)
# # # print(deleted_item)
# # #
# # # print(cources.pop())
# #
# #
# # # cources.reverse() #разворачивается
# # # print(cources)
# # # print(cources[::-1])
# #
# # # cources.sort() #сортирует в алфавитном порядке # от меньшего к большему
# # # print(cources)
# # # #print(cources[::-1])
# # # cources.sort(reverse=True)
# # # numbers.sort(reverse=True)#от больше к меньшему
# # # print(cources)
# # # print(numbers)
# #
# # # print(sorted(cources, reverse=True)) #сортировонная список
# # # print(sorted(numbers, reverse=True))#сортировонная список
# # # print(cources)
# # # print(numbers)
# #
# #
# #
# # print(min(cources)) #минимальное число если про числа а про строки минимальные прописные
# # print(max(cources)) #максимальное число если про числа а про строки максимальные заглваные
# # print(sum(numbers)) #общая сумма чисел
# # from hashlib import new
# #
cources = ['History', 'Math', 'Literature', 'Physics', 'Progaramming', str(12), '123213', 'asdasdasd','Fsasd']
# # numbers = [1, 5, 6, 8, 3, 4, 2]
# #
#
print(type(cources))
#
# # print(cources.index('Math', 1, 2))
# # print('Math' in cources)
#
#
# # print(str(cources))
# # print(*cources)
#
# cources_str = ', '.join((cources))  #соеденяем в одну строку ubiraem skobki
# print(cources_str)
# print(type(cources_str))

# print(cources_str.split((', ')))
# print(list(cources_str))
# # #
# # a, b, c = [1, 2, 3]
# # print(a, b, c)
#
# # cources2 = cources
# #
# # cources[0] = 'English' #две переменные которые ведут к одной и той же ссылке
# # cources2[-1] = 'English'
# # print(cources2)
# # print(cources)
# #
# # #как обойти и сделать два отдельных списков с помозью copy
# #
#
# # cources2 = cources.copy()
# #
# # cources[0] = 'English' #две переменные которые ведут к одной и той же ссылке
# # cources2[-1] = 'English'
# # print(cources)
# # print(cources2)
# #
# #
# # empty_tuple = (1, )   #кортеш
# # print(type(empty_tuple))
#
#
# #
# cources = ('History', 'Math', 'Literature', 'Physics', 'Progaramming', str(12), 'Wakakaka','Fsasd')
# # numbers = [1, 5, 6, 8, 3, 4, 2]
# #
# # #cources[0] = 'English' # ошибка кортеш не изменяемый в отличие от списка
# #
#
cources = ('1', '2', '3', '8')('8','2','5')
# numbers = {1, 5, 6, 8, 3, 4, 2}
#
# #set не разрешает дубликатов
# #set не упорядоченный
# # print(cources) #удаляет дубликат physics
# # cources.add('English')   # у set хаотичный порядок вывода
# # print(cources)
# # print(numbers) #данные выглядят упордячонными но нам это ничего не дает мы не можем применить и использовать этот порядок
# # cources.pop() #выкидывает случайный элемент
# # print(cources)
#
# # cources.clear()
# # print(cources)
#
# #
# # set1 = {'Math', 'Physics', 'Programming', 'History'}
# # set2 = {'History', 'Math', 'Art'}
# # print(set1.intersection(set2)) # ищем общее между двуями переменными
# #
# # print(set1.difference(set2))# ищем отличия чем отличая set1 от set 2
# # print(set2.difference(set1))# ищем отличия чем отличая set1 от set 2
# #
# # print(set1.union(set2)) #соеденение
#
# # print(set1.issubset(cources))
# # print(cources.issuperset(set1))
# #
# #
# # print(list(set(cources)))
#
# #
# # for subject in cources:
# #     print(subject)
# #
# #
# # for subject in cources:
# #         print(subject.upper())
# #
# # for number in numbers:
# #     print(number **2)
# #
# # # for number in numbers:
# # #     new.append(number ** 2)
# # # print(new)
# #
# # for subject in enumerate(cources):
# #     print(subject[0])
# #     print(subject[1])
# #

for index, subject in enumerate(cources):
    print(subject, index)
# #
# # for num in numbers:
# #     if num % 2 == 0:
# #         print(num,'Even')
# #     else:
# #         print(num, '0dd')
#
#
#
# # for num1 in range(10):  # 10 raz krutitsja
# #     for num2 in range(10):  # 10 na 10 krutitsja raz
# #         for num3 in range(10): # 10 na 10 na 10
# #             for num4 in range(10): # 10 na 10 na 10 na 10  krutitsja raz
# #                 print(num1, num2, num3, num4)
# #
#
#
#
#
# #Задача физ баз
#
# #Для диапозона чисел от 1 до 100
# #Если число делится на 3 без остатка , напиши число и FIZZ ВВЫВОД ЧИСЕЛ ДЕЛЯЩИХСЯ НА 3
# #Если число делится на 5 без остатка ,напиши число и BUZZ ВВЫВОД ЧИСЕЛ ДЕЛЯЩИХСЯ НА 5
# #Если число делится на 3 и на 5 напиши число и FIZZ BUZZ ВВЫВОД ЧИСЕЛ ДЕЛЯЩИХСЯ НА 5 И 3
#
# for