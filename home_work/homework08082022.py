

# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке (по одному слову в строке).



with open('../Test/trimushketera.txt', 'r', encoding='utf8')as book:
    data = book.read().lower()#.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('"', '').replace(';', '').replace('*', '').replace('(', '').replace(')', '') тоже можно
    for x in '1234567890;:,.-*[](){}:|/!?"':
        data = data.replace(x, '')
    data = data.split()
    unique = list(set(data))

    with open('../Test/trimushketera_copy.txt', 'w', encoding='utf8')as result:
        result.write(f'There are{len(data)} words in {book.name}.\n')
        result.write(f'There are {len(unique)} unique words in {book.name}.\n')
        unique.sort()
        for word in unique:
            result.write(word + '\n')








o