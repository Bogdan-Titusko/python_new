# # import re
# # # Sample string
# # text_to_search = '''
# # abcdefghijklmnopqurtuvwxyz
# # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# # 1234567890
# # Ha HaHa HaHaHa
# # MetaCharacters (Need to be escaped):
# # . ^ $ * + ? { } [ ] \ | ( ) #символы которые стоит избегать
# # example.com
# # 321-555-4321
# # 123.555.1234
# # 123*555*1234
# # 800-555-1234
# # 900-555-1234
# # 889-345-1234
# # 909-123-1233
# # Mr. Jones
# # Mr Smith
# # Ms Davis
# # Mrs. Robinson
# # Mr. T
# # abc
# # ball hall mall wall tall basketball
# # '''
# #
# # sentence = 'Start a sentence and then bring it to an end Добрый вечер'
# #
# # # patern = re.compile(r'abc') #R  ЭТО СЫРАЯ СТРОКА
# # #
# # # matches = patern.finditer(text_to_search)
# #
# #
# # # # for value in matches:
# # # #     print(value)
# # # #     print(value.start())
# # # #     print(value.end())
# # # #     print(value.group()) #возваращет само значение которое мы искали
# # # #     print(value.span()) #оба  выражения
# # # #
# # # # print(text_to_search[1:4])
# # # print(text_to_search[264:267]) #ищет идекс
# #
# #
# #
# #
# #
# # #sample = (1, 2, 3, 4, 5, 6)
# # # #print(iter(sample))
# # # sample1 = iter('123456')
# # # for val in sample1:
# # #     print(val)
# # # for val in sample1:
# # #     print(val)
# #
# #
# #
# #
# # #
# # # x = re.compile(r'example.com')
# # #
# # # c  =  x.finditer(text_to_search)
# # #
# # # for value in c:
# # #     print(value)
# #
# #
# #
# # x = re.compile(r'M(r|s|rs)\.? [A-Z]\w*')
# # #x = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*')
# # #x = re.compile(r'M(r|s|rs)\.')
# # #x = re.compile(r'M(rs|s|r)')
# # # x = re.compile(r'\d{3,5}')
# # # x = re.compile(r'\d{3,4}')
# # #x = re.compile(r'\d{3}.\d{3}.\d{4}')
# # #x = re.compile(r'\b[^w\d]all\b') #если стваим два \b то он будет искать именно слова которое начинается и заканчивается которое мы ищем
# # # x = re.compile(r'[^b\d]all')
# # # x = re.compile(r'[^w\d]all')
# # #x = re.compile(r'[a-z]all')
# # # x = re.compile(r'\wall')
# # #x = re.compile(r'[a-zA-Z-А-ё]')
# # # x = re.compile(r'[a-zA-Z]')
# # #x = re.compile(r'[1-a]') #unicode_character wikipedia 49 - 96
# # # x = re.compile(r'[A-D]')
# # #x = re.compile(r'[a-b]')
# # # x = re.compile(r'[f-r]')
# # # x = re.compile(r'[15-]')
# # # x = re.compile(r'[1-5]')
# # #x = re.compile(r'[90]00.\d\d\d.\d\d\d\d')
# # # x = re.compile(r'[80]00.\d\d\d.\d\d\d\d')
# # # x = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# # # x = re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d')
# # c  =  x.finditer(text_to_search)
# # #c  =  x.finditer(sentence)
# #
# # for value in c:
# #     print(value)
# #
# #
# #
# #
#
#
#
#
# #
# # import re
# #
# # with open('../txtfiles_123/people.txt', 'r', encoding='utf8')as file:
# #     data = file.read()
# #
# #     pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# #     matches = pattern.finditer(data)
# #
# #     result = []
# #     for match in matches:
# #         result.append(match.group())
# #         print(len(result))
# #
# #
# #
# import re
#
# #Sample string
# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# example.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
# Mr. Jones
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# abc
# '''
#
# sentence = 'Start a sentence and then bring it to an end'
#
# emails = '''
# SampleMaiL@example.com
# john.sample@my-work.net
# jack-125-production@colledge.edu
# bob.Samples@example.co.uk
# example@example.org
# '''
#
# urls = '''
# https://www.google.com
# http://www.wordpress.org
# https://www.nasa.gov
# https://example.net
# www.example.net
# example.net
# '''
#
# sentence = 'Start a sentence and then bring it to an end'
#
#
# #
#
# #
# # pattern = re.compile(r'(http://|https://)?(www\.)?([\w-]+)(\.[\w.]+)')
# # # subbed_urls = pattern.sub(r'\3\4', urls)
# # # print(subbed_urls)
# #
# # matches = pattern.finditer(urls)
# # for match in matches:
# #     print(match.group(3) + match.group(4))
# # # matches = pattern.finditer(urls)
# # # for match in matches:
# # #     print(match)
# # pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# # pattern = re.compile(r'abc', re.IGNORECASE)
# # pattern = re.compile(r'^\d', re.M)
# # pattern = re.compile(r'abc', re.VERBOSE)
# #pattern = re.compile(r'abc', re.MULTILINE)
#
# # #
# matches = pattern.split(text_to_search)
# # matches = pattern.finditer(text_to_search)
# #
# #
# #
# # for match in matches:
# #     print(match)
# # #
# # # while matches:
# # #     print(matches)
# # #     matches = pattern.search(text_to_search, matches.end())



colors = '''
Black	#000000	 
Navy	#000080	 
DarkBlue	#00008B	 
MediumBlue	#0000CD	 
Blue	#0000FF	 
DarkGreen	#006400	 
Green	#008000	 
Teal	#008080	 
DarkCyan	#008B8B	 
DeepSkyBlue	#00BFFF	 
DarkTurquoise	#00CED1	 
MediumSpringGreen	#00FA9A	 
Lime	#00FF00	 
SpringGreen	#00FF7F	 
Aqua	#00FFFF	 
Cyan	#00FFFF	 
MidnightBlue	#191970	 
DodgerBlue	#1E90FF	 
LightSeaGreen	#20B2AA	 
ForestGreen	#228B22	 
SeaGreen	#2E8B57	 
DarkSlateGray	#2F4F4F	 
LimeGreen	#32CD32	 
MediumSeaGreen	#3CB371	 
Turquoise	#40E0D0	 
RoyalBlue	#4169E1	 
SteelBlue	#4682B4	 
DarkSlateBlue	#483D8B	 
MediumTurquoise	#48D1CC	 
Indigo	#4B0082	 
DarkOliveGreen	#556B2F	 
CadetBlue	#5F9EA0	 
CornflowerBlue	#6495ED	 
MediumAquaMarine	#66CDAA	 
DimGray	#696969	 
SlateBlue	#6A5ACD	 
OliveDrab	#6B8E23	 
SlateGray	#708090	 
LightSlateGray	#778899	 
MediumSlateBlue	#7B68EE	 
LawnGreen	#7CFC00	 
Chartreuse	#7FFF00	 
Aquamarine	#7FFFD4	 
Maroon	#800000	 
Purple	#800080	 
Olive	#808000	 
Gray	#808080	 
SkyBlue	#87CEEB	 
LightSkyBlue	#87CEFA	 
BlueViolet	#8A2BE2	 
DarkRed	#8B0000	 
DarkMagenta	#8B008B	 
SaddleBrown	#8B4513	 
DarkSeaGreen	#8FBC8F	 
LightGreen	#90EE90	 
MediumPurple	#9370D8	 
DarkViolet	#9400D3	 
PaleGreen	#98FB98	 
DarkOrchid	#9932CC	 
YellowGreen	#9ACD32	 
Sienna	#A0522D	 
Brown	#A52A2A	 
DarkGray	#A9A9A9	 
LightBlue	#ADD8E6	 
GreenYellow	#ADFF2F	 
PaleTurquoise	#AFEEEE	 
LightSteelBlue	#B0C4DE	 
PowderBlue	#B0E0E6	 
FireBrick	#B22222	 
DarkGoldenRod	#B8860B	 
MediumOrchid	#BA55D3	 
RosyBrown	#BC8F8F	 
DarkKhaki	#BDB76B	 
Silver	#C0C0C0	 
MediumVioletRed	#C71585	 
IndianRed	#CD5C5C	 
Peru	#CD853F	 
Chocolate	#D2691E	 
Tan	#D2B48C	 
LightGray	#D3D3D3	 
PaleVioletRed	#D87093	 
Thistle	#D8BFD8	 
Orchid	#DA70D6	 
GoldenRod	#DAA520	 
Crimson	#DC143C	 
Gainsboro	#DCDCDC	 
Plum	#DDA0DD	 
BurlyWood	#DEB887	 
LightCyan	#E0FFFF	 
Lavender	#E6E6FA	 
DarkSalmon	#E9967A	 
Violet	#EE82EE	 
PaleGoldenRod	#EEE8AA	 
LightCoral	#F08080	 
Khaki	#F0E68C	 
AliceBlue	#F0F8FF	 
HoneyDew	#F0FFF0	 
Azure	#F0FFFF	 
SandyBrown	#F4A460	 
Wheat	#F5DEB3	 
Beige	#F5F5DC	 
WhiteSmoke	#F5F5F5	 
MintCream	#F5FFFA	 
GhostWhite	#F8F8FF	 
Salmon	#FA8072	 
AntiqueWhite	#FAEBD7	 
Linen	#FAF0E6	 
LightGoldenRodYellow	#FAFAD2	 
OldLace	#FDF5E6	 
Red	#FF0000	 
Fuchsia	#FF00FF	 
Magenta	#FF00FF	 
DeepPink	#FF1493	 
OrangeRed	#FF4500	 
Tomato	#FF6347	 
HotPink	#FF69B4	 
Coral	#FF7F50	 
Darkorange	#FF8C00	 
LightSalmon	#FFA07A	 
Orange	#FFA500	 
LightPink	#FFB6C1	 
Pink	#FFC0CB	 
Gold	#FFD700	 
PeachPuff	#FFDAB9	 
NavajoWhite	#FFDEAD	 
Moccasin	#FFE4B5	 
Bisque	#FFE4C4	 
MistyRose	#FFE4E1	 
BlanchedAlmond	#FFEBCD	 
PapayaWhip	#FFEFD5	 
LavenderBlush	#FFF0F5	 
SeaShell	#FFF5EE	 
Cornsilk	#FFF8DC	 
LemonChiffon	#FFFACD	 
FloralWhite	#FFFAF0	 
Snow	#FFFAFA	 
Yellow	#FFFF00	 
LightYellow	#FFFFE0	 
Ivory	#FFFFF0	 
White	#FFFFFF
'''


math_example = '''
(Примеры выражений “2*9-6*5” или (3+5)-9*4)
'''


clock_example = '''
«Завтрак в 09:00». Учтите, что «47:98» 

'''





# 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
# 	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

import re

# find_color = re.compile('#\w[A-F].\w[0-9].')
# html_color = find_color.finditer(colors)
#
# for color in html_color:
#     print(color)

# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)
# #
# number = re.compile(r'\d[-*()]')
# example = number.finditer(math_example)
#
# for num in example:
#     print(num)

# 3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.


#
# hours = re.compile(r'[А-я]|[00]?\d|2[0-3]|[0-5]?\d')
# hours_time = hours.finditer(clock_example)
# for hour in hours_time:
#     print(hour)
#
#


# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
# 	2) Все адреса

with open('../txtfiles_123/people.txt', 'r', encoding='utf8')as file:
    data = file.read()
    pattern = re.compile(r'')
    matches = pattern.split(data)
    for match in matches:
        print(match)





# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.
#




# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)
#
# Все строки произвольные.


