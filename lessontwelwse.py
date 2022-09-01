import re

import requests
from requests.exceptions import HTTPError
from bs4 import  BeautifulSoup as BS

# 200  sucess
# 300 redirect
# 400 client errors
# 500  server errors


# r = requests.get('https://xkcd.com/353/', timeout=10) # timeout не обязательная пауза
# # print(r.status_code)
# # print(dir(r))
# print(r.text)
# print(r.content)
# print(r.ok)
# print(r.encoding)
# print(r.cookies)
# print(r.headers)
# print(r.headers['Server'])
# # r2 = requests.get("https://imgs.xkcd.com/comics/python.png")
# # with open('comic.png', 'wb')as file:
# #     file.write(r2.content)



# r = requests.get('http://wwww.google.com', headers=headers)
# for url in ['http://api.github.com', 'http://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         print(response)
#         response.raise_for_status()
#         x = 1 / 0
#     except HTTPError as http_err:
#         print(f'HTTP error occurred : {http_err}')
#     except Exception as err:
#         print(f'Other error occured:{err}')
#     else:
#         print('Success')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
# url = 'https://rus.postimees.ee'
# request = requests.get(url)
#
# soup = BS(request.content,  'html.parser')
#                                                                                             # print(soup.prettify()) #для красоты prettyfy
#                                                                                             # print(soup.title.parent.text)
                                                                                            # print(soup.get_text())
                                                                                            # print(soup.get_attribute_list('tag_name'))
                                                                                            # print(soup.div['class'])
                                                                                            # print(soup.div)
# match = soup.find('div', class_='header')
# print(match)

# match = soup.find_all('div', class_='col-md-4')
# for x in match:
#     links = x.findall('a')
#     print(x)


# print(len(match))
# print(soup.a.get_attribute_list('href'))

# matches = soup.find_all('article', class_='list-article')
# for match in matches:
#     links = match.find_all('a', class_='list-article__url')
#     for link in links:
#         print(link['href'])
#


# url = 'https://gammatest.net/course/python/'
# request = requests.get(url)
# soup = BS(request.content, 'html.parser')
# print(soup.find_all(['a', 'table']))
# print(soup.find_all(text=True)) #найти все где есть текс
# print(soup.find_all(True))
#print(soup.find_all(class_=re.compile('\d+ EUR')))
# print(soup.find_all(string =re.compile('Словари')))
# print(soup.find_all('a',text='Eesti keeles'))
# print(soup.find_all('a', text='Перейти')) #все ссылки со словом перейти
# print(soup.find_all('a', text='Перейти', limit=2)) #лимит в две ссылки
# print(soup('a'))
# print(soup.find_all('a'))#одинакоый результат по методу a
# test_link = soup.find('a', string='Eesti keeles')
# print(test_link)
# print(test_link.find_parent('div')) #поиск по ближнему родителю
# print(test_link.find_parents('div'))#поиск по родственнику
# print(test_link.find_parent('div').h2)
# print(test_link.find_next())
# print(test_link.find_previous_sibling())
# print(test_link.find_parent().find_previous_sibling())
# test_link = soup.find('table').tr
# print(test_link.td.find_next_siblings())
# print(soup.f)
#

#
# next sibling nahodit sledujewego rodstvennika
# parent nahodit roditelja
# parents nahodit roditelej
# siblings nahodit rodsvtennikov
# all previus vseh prededuwij
# all next vseh posludujuwih
# child nahodit vseh detej ('td il a il br i .td smotja po kakomu classu  iwem')




# def get_btc_eur_value():
#     url ='https://www.google.com/search?q=btc+to+eur&oq=btc+to+e&aqs=edge.0.0i512j69i57j0i512l7.2327j0j1&sourceid=chrome&ie=UTF-8'
#     r = requests.get(url, headers=headers)
#     soup = BS(r.content, 'html.parser')
#     result = soup.find('span', class_='pclqee')
#     # print(result.text.encode('utf-8')) как мы сделали строку 119
#     # print(result.text.encode('utf-8').replace(b'xc2\xa0',b'').replace(b',',b'.').decode('utf-8'))
#     # return int(result.text.replace('.',' ').replace(',',' '))
#     return float(result.text.encode('utf-8').replace(b'\xc2\xa0',b'').replace(b',',b'.').decode('utf-8'))




# print(get_btc_eur_value())


# def main():
#     while True:
#         user_choce = input('Please choose: \n'
#                         '1. EUR to BTC\n'
#                         '2.BTC to EUR\n'
#                         'O.Exit')
#         if user_choce == '0':
#             print('gg')
#             break
#         elif user_choce == '1':
#             user_amount = float(input('Enter amount: '))
#             print(user_amount / get_btc_eur_value())
#         elif user_choce == '2':
#             user_amount = float(input('Enter amount: '))
#             print(user_amount * get_btc_eur_value())
#         else:
#             print('Choice out of range')
# main()

# def get_wheater():
#     url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
#     r = requests.get(url, headers=headers)
#     soup = BS(r.content,'html.parser')
#     result = soup.find('div', class_='float-thead-table-container')
#
#
# headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
#
#
#
# get_wheater()
#
# def main():
#     while True:
#         user_choice = input('Please choose\n'
#                             '1.Choose city\n'
#                             '0.Exit\n')
#         if user_choice == '0':
#             print('Good bye')
#         elif user_choice == '1':
#             user_city = input('Enter city : ')
#             soup = BS(r.content,'html.parser')
#             print((soup.find_parents('td' + user_city, class_='number' )))
#         else:
#             print('Error')
# main()

#
# url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
# r = requests.get(url, headers=headers)
# soup = BS(r.content, 'html.parser')
# result = soup.find_all('div', class_='float-thead-table-container')
# for match in result:
#     links = match.find_all('td', class_='number')
#     print(links)
#

#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def write_csv(data):
#     with open('cmc.csv', 'a') as f:
#         writer = csv.writer(f)
#         pass
#
# def get_page_data(html):
#     soup = BS(html, 'lxml')
#     trs = soup.find('table').find('tbody').find_all('tr')
#     print(len(trs))
#
#
# def main():
#     url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
#     get_page_data(get_html(url))
#
# if __name__ == '__main__':
#     main()