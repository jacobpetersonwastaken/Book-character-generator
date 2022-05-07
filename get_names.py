import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
year = 1880


# load_dotenv('.env')
# chrome_driver_path = os.getenv('CHROME_PATH')
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
# driver.get(url='https://www.ssa.gov/oact/babynames/')
#
#
# birth_input = driver.find_element(By.NAME, 'year')
# birth_input.click()
# birth_input.clear()
# birth_input.send_keys(year)
# quantity = Select(driver.find_element(By.NAME, 'top'))
# quantity.select_by_value('1000')
# num_of_birth = driver.find_element(By.ID, 'number').click()
# submit = driver.find_element(By.XPATH, '//*[@id="content"]/section[4]/div/div/div[1]/form/p[3]/input[1]').click()
#
# """scrapes the ssa website and downloads max names and stores inside a name.json file."""
# def get_names():
#     global year
#     counter = 0
#     with open('names.json') as f:
#         data = json.load(f)
#     quantity_tr = len(driver.find_elements(By.CSS_SELECTOR, 'p table tbody tr'))
#     for i in range(2, quantity_tr):
#         try:
#             name_rank = driver.find_element(By.XPATH, f'/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[{i}]/td[1]')
#             male_first_name = driver.find_element(By.XPATH,
#                                                   f'/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[{i}]/td[2]')
#
#             num_of_male = driver.find_element(By.XPATH, f'/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[{i}]/td[3]')
#             female_first_name = driver.find_element(By.XPATH,
#                                                     f'/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[{i}]/td[4]')
#             num_of_female = driver.find_element(By.XPATH, f'/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[{i}]/td[5]')
#         except:
#             pass
#         if counter == 0:
#             data[str(year)] = {
#                 'male': {
#                     male_first_name.text: {
#                         'rank': name_rank.text,
#                         'number of males': num_of_male.text
#                     }
#                 },
#                 'female': {
#                     female_first_name.text: {
#                         'rank': name_rank.text,
#                         'number of female': num_of_female.text
#                     }
#                 }
#             }
#             counter += 1
#         else:
#             data[str(year)]['male'][male_first_name.text] = {
#                 'rank': name_rank.text,
#                 'number of males': num_of_male.text
#             }
#             data[str(year)]['female'][female_first_name.text] = {
#                 'rank': name_rank.text,
#                 'number of female': num_of_female.text
#             }
#     with open('names.json', 'w') as file:
#         json.dump(data, file)
#     year += 1
#
#
# def second_page():
#     global year
#     birth_input = driver.find_element(By.NAME, 'year')
#     birth_input.click()
#     birth_input.clear()
#     birth_input.send_keys(year)
#     submit = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[1]/form/input[4]').click()
#
#
# for i in range(139):
#     get_names()
#     second_page()
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_column', 100)
# pd.set_option('display.max_rows', 500)
# data = pd.read_json('names.json').transpose()
#
#
#
# with open('names_sorted_by_year.json')as f:
#     data = json.load(f)
#
# names = {}
# for i in data:
#     names[i] = {'male': [],
#                 'female': []}
#     for t in data[i]['male']:
#         names[i]['male'].append(t)
#     for t in data[i]['female']:
#         names[i]['female'].append(t)
#
# with open('names_sorted_by_year.json', 'w')as file:
#     json.dump(names, file)
#
#
# filtered_names_male = []
# filtered_names_female = []
# for i in data:
#     for b in data[i]['male']:
#         if b not in filtered_names_male:
#             filtered_names_male.append(b)
#     for g in data[i]['female']:
#         if g not in filtered_names_female:
#             filtered_names_female.append(g)
#
#
# names = {
#     'male': filtered_names_male,
#     'female': filtered_names_female
# }
# print(len(filtered_names_male))
# print(len(filtered_names_female))
#
#



