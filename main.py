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

# class Dog():
#
#
#     def __init__(self, name, origin):
#         self.name = name
#         self.origin = origin
#     def say(self):
#         print(f"{self.name} умеет лаять")
#
# white_dog = Dog("Шарик", "Asian")
# brown_dog = Dog("Пушок", "Еврей")
#
#
#
# print(white_dog.name)
# print(brown_dog.name)
# print(f"{white_dog.name} порода {white_dog.origin}")
#
# white_dog.say()

# class Human:
#         def input_data(self):
#             self.fio = input("Введите ФИО ")
#             self.number = input("Введите Номер Телефона ")
#             self.birthday = input("Введите Днюху")
#
#         def print_data(self):
#             print(self.fio)
#             print(self.number)
#             print(self.birthday)
#         def get_fio(self):
#             return self.fio
#         def get_number(self):
#             return self.number
#         def get_birthday(self):
#             return self.birthday
#
# class Builder(Human):
#
#         def input_parametr(self):
#             self.specialization = input("Ввкдите специализацию строителя?:")
#             self.main_tools = input("Введите основной инструмент:")
#             self.post = input("Введите должность:")
#
#         def print_data(self):
#             print(self.fio)
#             print(self.number)
#             print(self.birthday)
#             print(self.post)
#             print(self.main_tools)
#             print(self.specialization)
#
#         def get_post(self):
#             return self.post
#
#         def get_main_tools(self):
#             return self.main_tools
#
#         def get_specialization(self):
#             return self.specialization
# # object_1 = Human()
# # object_1.input_data()
# list.employee=[]
# for i in range(3):
#     employee = Builder()
#     employee.input_data()
#     employee.input_parametr()
#     employee.print_data()

# class City:
#
#         def input_data(self):
#             self.name_city = input("Введите город: ")
#             self.count_resident = int(input("Введите количество жителей: "))
#             self.cod_phone = int(input("Введите тел.код города: "))
#
#         def print_data(self):
#             print(self.name_city)
#             print(self.count_resident)
#             print(self.cod_phone)
#
#         def get_name_city(self):
#             return self.name_city
#
#         def get_count_resident(self):
#             return self.name_city
#
#         def get_cod_phone(self):
#             return self.cod_phone
#
# city_1 = City()
# city_1.input_data()
# city_1.print_data()

# class Passport:
#
#     def input_data(self):
#         self.name = input("Введите Имя: ")
#         self.sname = input("Введите Фамилия: ")
#         self.faser_name = input("Введите Отчество: ")
#         self.birthday = int(input("Введите Днюху: "))
#         self.registration = input("Введите адрес: ")
#         self.number = int(input("Введите серию и номер: "))
#         self.data = int(input("Введите дату выдачи: "))
#
#     def print_data(self):
#         print(self.name)
#         print(self.sname)
#         print(self.faser_name)
#         print(self.birthday)
#         print(self.registration)
#         print(self.number)
#         print(self.data)
# class Foreign(Passport):
#
#     def input_parametr(self):
#
#         self.country = input("Введите Страну: ")
#         self.fin_data = input("Введите окончание срока действия: ")
#         self.number_1 = int(input("Введите серию и номер: "))
#         self.data_1 = int(input("Введите дату выдачи: "))
#
#     def print_data1(self):
#         print(self.country)
#         print(self.fin_data)
#         print(self.number_1)
#         print(self.data_1)
#
#
# object_1 = Foreign()
# object_1.input_data()
# object_1.input_parametr()
# object_1.print_data1()
# object_1.print_data()

# class Car:
#
#     def __init__(self, year_model, make, speed=0):
#         self.year_model = year_model
#         self.make = make
#         self.speed=speed
#
#     def accelerate(self):
#         self.speed +=5
#
#     def break_(self):
#         self.speed -=5
#
#     def get_speed(self):
#         return self.speed
#
# car=Car("2015", "VW Polo")
# for i in range(5):
#     car.accelerate()
#     print(f"Текущая скорость авто {car.get_speed()}")
# for i in range(5):
#     car.break_()
#     print(f"Текущая скорость авто {car.get_speed()}")

# class Patient():
#     def __init__(self, name, adr, tel, tel2):
#         self.name = name
#         self.adr = adr
#         self.tel = tel
#         self.tel2 = tel2
#
#
#     def print_data(self):
#         print(self.name)
#         print(self.adr)
#         print(self.tel)
#         print(self.tel2)
#
#     def get_name(self):
#       return self.name
#
#     def get_adr(self):
#         return self.adr
#
#     def get_tel(self):
#         return self.tel
#
#     def get_tel2(self):
#         return self.tel2
#
#     def edit_name(self, name):
#         self.name = name
#
#     def edit_adr(self, adr):
#         self.adr = adr
#
#     def edit_tel(self, tel):
#         self.tel = tel
#
#     def edit_tel2(self, tel2):
#         self.tel2 = tel2
#
# Patient_1 = Patient(input("Введите Фамилию Имя Отчество: "), input("Введите Адрес с индексом: "),input("Введите телефон: "),input("Введите телефон контактного лица: "))
# Patient_1.print_data
# class Procedure:
#
#     def __init__(self, code, dat, name_doc, price):
#         self.code = code
#         self.dat = dat
#         self.name_doc = name_doc
#         self.price = price
#
#
#     def print_data2(self):
#         print(self.code)
#         print(self.dat)
#         print(self.name_doc)
#         print(self.price)
#
#     def get_code(self):
#         return self.code
#
#     def get_dat(self):
#         return self.dat
#
#     def get_name_doc(self):
#         return self.name_doc
#
#     def get_price(self):
#         return self.price
#
#     def edit_code(self, code):
#         self.code = code
#
#     def edit_dat(self, dat):
#         self.dat = dat
#
#     def edit_name_doc(self, name_doc):
#         self.name_doc = name_doc
#
#     def edit_price(self, price):
#         self.price = price
#
#
# Procedure_1 = Procedure(input("Введите Название процедура: "), input("Введите Дату процедуры: "), input("Введите Имя врача: "), input("Введите Стоимость процедуры: "))
#
# Procedure_1.print_data2()
import math
class Square:
    def square_triangle(self, a, h):
        self.s = 0.5*a*h
        return self.s

    @staticmethod
    def square_triangle_2(a,h):
        return 0.5*a*h

    @staticmethod
    def square_triangle_3(a,sin_a, sin_b):
        return math.pow(a,2)*(math.sin(sin_a)*math.sin(sin_b))/2/math.sin(sin_a+sin_b)


sy = Square()
sy.square_triangle(15,20)
print(sy.s)

print(Square.square_triangle_2(15,5))

print(Square.square_triangle_3(12,30, 60))


