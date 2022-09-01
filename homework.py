# import requests
# from bs4 import BeautifulSoup
# import json
#
#
# def get_weather_data():
#     url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
#     r = requests.get(url, timeout=10, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     data_rows = soup.tbody.find_all('tr')
#     data_names = ['Air temp average', ' Air temp maximum', 'Air temp minimum', 'Graund temp 2cm', 'Humidity average', 'Humidity minimal', 'Air speed maximum', ]
#     result = {}
#     for tr in data_rows:
#        key = tr.findChild('td').text
#        data = [x.text for x in tr.findChildren('td') if x != key]
#        full_data = list(zip(data_names, data))
#        data_dict = {}
#        for entry in full_data:
#            data_dict[entry[0]] = entry[1]
#            result[key] = data_dict
#            print(result)
#
#     return result
#
# def wrtie_data_to_file(data):
#     with open('wheater.json', 'r', encoding='cp1257') as file:
#         data2 = json.load(file)
#     if str(datetime.date.today()) not in data2.keys():
#         data2[str(datetime.date.today)] = data
#         with open('wheater,json','w') as file:
#             json.dump(data2, file, indent=2)
#     else:
#         print('DATA IS UP TODATE')
#
# def main():
#         pass
# wrtie_data_to_file(get_weather_data())
#
#
# #
# # # 2 метода
# # # метод мап и зип в  пайтоне первй мап итерирует через функцию должна быть функция  например
# # def squares(number):
# #     return number ** 2
# #
# #
# # spisok_cifr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # novqj_spisok = []#пустой
# # for x in spisok_cifr:
# #     novqj_spisok.append(squares(x))
# #
# # print(novqj_spisok)
# # print([squares(x)for x in spisok_cifr])
# #
# # print(list(map(squares, spisok_cifr))) #
# #
# #
# #
# #
# # data1 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
# #
# # data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# #
# # combination = zip(data1, data2, spisok_cifr)
# #
# # print(list(combination))
#
# #
# #
# #
# # def wheather(url):
# #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36' }
# #     response = requests.get(url, headers=headers)
# #     text = response.content.decode('utf-8')
# #     soup = BeautifulSoup(text, 'lxml')
# #     tables = soup.find('div', class_='float-thead-table-container').find_all('tbody')
# #     for table in tables:
# #         trs = table.find_all('tr')[0:]
# #         for index, tr in enumerate(trs):
# #             tds = tr.find_all('td')
# #             city_td = tds[0]
# #             if index == 0:
# #                 city_td = tds[0]
# #             city = list(city_td.stripped_strings)
# #             max_temp = list(tds[-10].stripped_strings)
# #             mid_temp = list(tds[-11].stripped_strings)
# #             min_temp = list(tds[-9].stripped_strings)
# #             windmax_speed = list(tds[-3].stripped_strings)
# #             windmid_speed = list(tds[-4].stripped_strings)
# #             precipitation = list(tds[-2].stripped_strings)
# #             humidity_min = list(tds[-5].stripped_strings)
# #             humidity_mid = list(tds[-6].stripped_strings)
# #             print({'Город ':city, 'Максимальная температура ->': max_temp, 'Средняя температура->':mid_temp, 'Минимальная температура->':min_temp, 'Wind max speed->':windmax_speed,
# #                    'Wind mid speed->': windmid_speed, 'Precipitation->': precipitation, 'Humidity min->' :humidity_min, 'Himidity mid->':humidity_mid})
# #
# # if __name__ == '__main__':
# #     url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
# #     wheather(url)
# #
#
#
