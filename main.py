# from selenium import webdriver
# import os
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# service = Service(executable_path=r"C:\Users\ADMIN\PycharmProjects\qa\pythonProject1\chrom driver\chromedriver.exe")
# option = webdriver.ChromeOptions()
# #option.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1")
# #option.add_argument("--disable-blink-features=AutomationControlled")
# #option.add_argument("--incognito")
# #option.add_argument("--window-size=1920,1080")
# #option.add_argument("--ignore-certificate-errors")
# #Стратегия загрузки страниц normal / eager
# #option.page_load_strategy = 'normal'
# prefs = {
#     "download.default_directory":fr"{os.getcwd()}\download"
# }
# option.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(service=service, options=option)
# url = "https://eng.utorr.cc/fantastika/2576-terminator-1984.html"
# #start_time = time.time()
# driver.get(url)
# time.sleep(5)
# driver.find_elements("xpath", "/html/body/div[2]/div[4]/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[6]/a")[0].click()
# #end_time = time.time()
#
# #result = end_time-start_time
# #print(f"fkj {result}")
# time.sleep(5)
#
# driver.close()
# print('Задача 17')
# import math
# pup = {'Ростислав': 18, 'Тимур': 24, 'Радмила': 22, 'Гари': 30}
# print(f'Имеем словарь с данными: {pup}')
# Key_max = max(zip(pup.values(), pup.keys()))[1]
# Key_min = min(zip(pup.values(), pup.keys()))[1]
# print(f'Максимальное значение возраста у человека по имени {Key_max}')
# print(f'Минимальное значение возраста у человека по имени {Key_min}')
#
# print('Задача 18 \n')
# arr1 = [1, 8, 5, 47, 9, 64]
# arr2 = [2, 1, 6, 8]
# arr3 = arr1[:-1] + arr2
# print(f'Первый список {arr1}')
# print(f'Второй список {arr2}')
# print(f'Измененный список список, полученный заменой последнего элемента Первого списка на элементы Второго списка {arr3}')

import requests
# responce=requests.get('https://randomuser.me/api/')
# print(responce.status_code)
# print(responce.reason)
# print(responce.text)


# responce_2=requests.get('https://api.thedogapi.com/v1/breeds')
# print(responce_2.status_code)
# print(responce_2.reason)
# new_dog_firstLetter_C =[]
# for i in range(len(responce_2.json())):
#
#     if responce_2.json()[i]["name"][0]=='W':
#         new_dog_firstLetter_C.append(responce_2.json()[i]["name"])
# print(new_dog_firstLetter_C)

# import json
# import io
# from collections import Counter
# def driving_expirience(name_bd):
#     dr_ex_list = []
#     try:
#         with io.open(name_bd,encoding='utf-8') as read_file:
#             data=json.load(read_file)
#             for i in range(len(data['features'])):
#                 if len(data['features'][i]['properties']['vehicles']) >= 2:
#                     for j in range(len(data['features'][i]['properties']['vehicles'])):
#                         if len(data['features'][i]['properties']['vehicles'][j]['participants']) >= 2:
#                             for k in range(len(data['features'][i]['properties']['vehicles']['participants'])):
#                                 dr_ex_list.append(data['features'][i]['properties']['vehicles'][j]['participants'][k]['years_of_driving_experience'])
#                     else:
#                         dr_ex_list.append(data['features'][i]['properties']['vehicles'][j]['participants'][0]['years_of_driving_experience'])
#                 else:
#                     dr_ex_list.append(data['features'][i]['properties']['vehicles'][0]['participants'][0]['years_of_driving_experience'])
#
#     except Exception as ex:
#          print(ex)
#
#     finally:
#         counter = Counter(dr_ex_list)
#         print(counter)
# x='smolenskaia-oblast.json'
# driving_expirience(x)
#
# def color_of_vehicle(name_bd):
#     dr_ex_list2 = []
#     try:
#
#         with io.open(name_bd, encoding='utf-8') as read_file:
#             # получаем весь файл в рид файл
#             # форматируем файл в json и присваиваем его переменной data
#             data = json.load(read_file)
#     #         с помощью цикла проходимся по файлу
#             for i in range(len(data['features'])):
#                 if len(data['features'][i]['properties']['vehicles']) >= 2:
#                     for j in range(len(data['features'][i]['properties']['vehicles'])):
#                         dr_ex_list2.append(data['features'][i]['properties']['vehicles'][j]['color'])
#                 elif len(data['features'][i]['properties']['vehicles']) ==0:
#                     dr_ex_list2.append('нет ТС')
#
#                 else:
#                     dr_ex_list2.append(data['features'][i]['properties']['vehicles'][0]['color'])
#     except Exception as ex:
#         print(ex)
#
#     finally:
#         counter = Counter(dr_ex_list2)
#         print(counter)
#
# color_of_vehicle(x)

class Dog()


