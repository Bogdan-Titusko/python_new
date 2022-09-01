import pandas as pd
import matplotlib.pyplot as plt

import re



df = pd.read_csv('2019.csv', header=1)
df.to_excel('output.xlsx')



# new_df2 = df[['GDP per capita']]
# new_df2.plot()
# plt.show()
# print(df.loc[df['Country or region'].str.contains('on|an')]['Country or region'])
# print(df.loc[df['GDP per capita']< 1, ['Country or region', 'Overall rank']])

# print(df.groupby('Score').mean().sort_values('Score', ascending=False))

# large = df.nlargest(5, ['Generosity', 'Overall rank'  ])
# large = df.nlargest(5, ['Generosity'])
# small = df.nsmallest(5, 'Overall rank')
# print(large)
# print(small)
#
# print(pd.concat([large, small]))
#

# df.info()

# print(df['Freedom to make life choices'])
# df = df.dropna()
# print(df['Freedom to make life choices'])
#


# pd.set_option('display.max_columns', 10)
# print(df['Country or region'])
# print(df.iloc[0]['Score'])
# print(df.iloc[0:3]) # от 0 строчки до 3
# print(df.iloc[[2, 45, 115]])
# print(df.iloc[[1, 2, 3]])

# print(df.loc[1, 'Country or region'])
# print(df.loc[[2, 3, 1]])
# # print(df.loc[['Country or region','Score']])
# print(df.loc[[2, 3, 1 ], 'Country or region':'Perceptions of corruption'])
# data = df.loc[2]
# print(data['Country or region'] + ' ' + str(data['Score']))
# print(list(df.iterrows()))
# for index, series in df.iterrows():
#     print(index)
#     print(series['Country or region'])
# for x in df:
#     print(x)
# print(df.loc[df['Country or region'] == 'Estonia'])
# print(df.loc[df['Overall rank'] > 50])
# print(df.describe())
# print(df.memory_usage(deep=True))
# print (df.sort_values('Country or region', ascending=True))
# print (df.sort_values(['Country or region', 'Generosity'], ascending=True))
# print (df.sort_values(['Country or region', 'Generosity'], ascending=[True,False])) #   True сортирует первое country or region False второе значение generosity
# df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Score']
# print(df)
#
# df.insert(loc=0, column='New column', value=(df['GDP per capita'] ** 2 ))
# print(df)
# df = df.drop(columns=['Total', 'New column'])
# print(df)
# print(df[['Country or region', 'Score']])
# в [] скобках можно одно значени , чтоб больше одного добавить нужно делать так [[]]
# pd.set_option('display.max_rows', 160)
# pd.set_option('display.max_columns', 9)
#
# print(df.head())
# print(df.tail())
# people = {
#     'name': ['Bob', 'Alex', 'John'],
#     'surname': ['Smith', 'Brown', 'Gold'],
#     'email': ['bob@example.com', 'alex@example.com', 'john@example.com']
#
# }
# df2 = pd.DataFrame(people)
# print(df2)
# print(df2['name'])
# print(type(df2['name']))
# print(type(df2[['name', 'surname']]))
# #
# with open('sample2.json', 'r',encoding='utf-8') as file:
#     data = json.load(file)
# df = pd.DataFrame(data['people'])
# print(df)
# print(type(df))
# df = pd.read_csv('2019.csv', header=None, nrows=10)
# print(df)
# df.to_csv('new_csv.csv')
# skiprows  проуписть какой то ряд
# header назначает какой  хедер выводить
# header None если нет хедера эта функция может сделать так что  паданс проидексирует все столбы без их названчения на хедер
# если нету хедера можно сделать так что header None  . names = ['NAME', 'DATE OF BITTH' и т.д] главное писать именна столько сколько столбиков данных есть
# когда нужно вытащить некоторое кол-во рядом из огромной тоблицы используем nrows 5  5 записей в таблице
# сохранить файл df.to_csv (new.csv')