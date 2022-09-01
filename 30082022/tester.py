
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.com/search?q=translate'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

accept_all = driver.find_element(By.ID , 'L2AGLb')
accept_all.click()

open_full_translater = driver.find_element(By.ID, 'tw-gtlink')
open_full_translater.click()
time.sleep(2)

open_transler_list = driver.find_element(By.CLASS_NAME, 'VfPpkd-Bz112c-RLmnJb')
open_transler_list.click()
time.sleep(1)
driver.execute_script('window.scrollTo(0,600)')
time.sleep(3)

choose_rus_language = driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/div[89]/div[2]')
choose_rus_language.click()
time.sleep(2)

open_transler_list2 = driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]')
open_transler_list2.click()
time.sleep(2)


choose_est_language = driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[132]/div[2]')
choose_est_language.click()
time.sleep(2)

enter_words = driver.find_element(By.CLASS_NAME, 'er8xn')
enter_words.send_keys('Привет, мы изучаем парсинг сайтов.')
time.sleep(10)

voice_on = driver.find_element(By.CLASS_NAME, 'material-icons-extended VfPpkd-Bz112c-kBDsod')
voice_on.click()


































# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get('http://www.github.com')
#
# def check_element(locator):
#     try:
#         element = WebDriverWait(driver, 10).until(
#             # EC.presence_of_element_located((By.ID, 'user_email')) #монжно и 'id'
#             EC.presence_of_element_located((locator))
#         )
#         return True
#     except:
#         return False
#
# if check_element(('id', 'user_email')):
#     print('OK')
# else:
#     print('Nok')
#
#



# print(driver.title)
# email_field = driver.find_element('name', 'user_email')
#
#
# # print(email_field.is_enabled() )
# # print(email_field.is_selected())
# # print(email_field.is_displayed())
# #
#
#
# email_field.send_keys('python@exmaple.com')
# email_field.send_keys(Keys.RETURN)
#
# # print(email_field)
# # print(email_field.parent)
#
# time.sleep(6)
# continue_button = driver.find_element('class name', 'signup-continue-button')
# continue_button.click()
#
#
# password_field = driver.find_element('xpath', '/html/body/div[4]/main/div[2]/text-suggester/div[1]/form/div[2]/div[2]/div/visible-password/auto-check/input[1]')
# password_field.send_keys('109283741123aaaesd')
#
# # time.sleep(5)
# continue_button = driver.find_element('css selector', 'button.signup-continue-button')
# continue_button.click()








# time.sleep(5)
# driver.close()
# driver.quit()