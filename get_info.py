import json
from bs4 import BeautifulSoup
from requests import *
from string import *
import re
""""YYYYMMDD"""


# site = get(url=url, headers=headers)
# content = site.text
#
# soup = BeautifulSoup(content, 'html.parser')
# types = soup.select(selector='ol li')

"""Gets 16 personalities"""
# with open('16_personalities.json')as f:
#     data = json.load(f)
# for i in types:
#     name = i.find('img').get('data-animation')
#     code_url = i.get('href')
#     personality_code = i.find('h5').text
#     data[name] = {'code': personality_code,
#                   'url': code_url}
#
# with open('16_personalities.json', 'w')as file:
#     json.dump(data, file)
# p = {'architect': {
#     'code': 'INTJ-A / INTJ-T',
#     'url': 'https://www.16personalities.com/intj-personality'}}

"""Gets zodiac symbol """
# with open('zodiac.json')as f:
#     data = json.load(f)
#
# for i in types.find_all('p'):
#     t = i.text.split(' ')
#     emoji = i.text.split()[0]
#     name = i.text.split()[1]
#     animal = re.sub(r"\W+", '', i.text.split()[2])
#     date_range = i.text.split(': ')[1]
#     from_date = date_range.split("–")[0]
#     to_date = date_range.split("–")[1]
#
#     data[name] = {
#         'emoji': emoji,
#         'animal': animal,
#         'from': from_date,
#         'to': to_date
#
#     }

"""Hair colors"""
"""Gets from https://www.latest-hairstyles.com/color/chart.html"""
# with open('physical_features.json')as f:
#     data = json.load(f)
# for i in types:
#     t = i.select(selector='tr')[1::2]
#     for hair in t:
#         # data['hair color'].append(hair.text)+
#         hair_list = hair.text.split('\n')
#         hair_list.pop(0)
#         hair_list.pop(-1)
#         for i in hair_list:
#             data['hair color'].append(i)
#
#
#
# with open('physical_features.json', 'w')as file:
#     json.dump(data, file)
"""This gets from https://www.reddit.com/r/theouterworlds/comments/k7zrr3/character_creator_hair_colour_list/"""
# hair_list = []
# for i in types:
#     hair_list.append(i.text)
# with open('hair_color.json', 'w+')as f:
#     json.dump(hair_list, f)

"""
face_shape
eye shape
male female
body shape
height

"""
# with open('physical_features.json')as f:
#     data = json.load(f)
#
# t = [i.lower() for i in data['face shape']]
# data['face shape'] = t
#
# with open('physical_features.json', 'w')as file:
#     json.dump(data, file)

