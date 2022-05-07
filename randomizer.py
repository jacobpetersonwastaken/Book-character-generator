import json
import random


class Randomizer:
    def __init__(self):
        with open('16_personalities.json') as p:
            self.personalities = json.load(p)
        with open('love_language.json') as li:
            self.love = json.load(li)
        with open('physical_features.json') as physical:
            self.physical_features = json.load(physical)
        with open('zodiac.json') as z:
            self.zodiac = json.load(z)
        with open('top_names_1880_to_2018.json') as n:
            self.names = json.load(n)

    def rand_person(self, gender_type: str):
        rand_zodiac = self.rand_zodiac()
        love_language = self.love_language()
        rand_personality = self.rand_personality()
        print(f"""
        Name: {self.rand_name(gender_type=gender_type)}\n
        Personality: {rand_personality[0]} {rand_personality[1]['url']}\n
        Love language: {love_language[0]}\n {love_language[1]}\n
        Zodiac: {rand_zodiac[0]} {rand_zodiac[1]} From {rand_zodiac[2]} to {rand_zodiac[3]}\n
        Hair color: {self.hair_color()}\n
        Eye color: {self.eye_color()}\n
        Eye shape: {self.eye_shape()}\n
        Face shape: {self.face_shape()}\n
        """)

    def rand_personality(self):
        personality_key = random.choice(list(self.personalities))
        personality_value = self.personalities[personality_key]
        return [personality_key.title(), personality_value]

    def love_language(self):
        love_key = random.choice(list(self.love))
        love_value = self.love[love_key]
        return [love_key, love_value]

    def eye_color(self):
        eye_key = random.choice(list(self.physical_features['eyes']))
        if eye_key == 'heterochromatic':
            while True:
                right_eye = self.physical_features['eyes'][random.randint(0, len(eye_key[-2]))]
                left_eye = self.physical_features['eyes'][ random.randint(0, len(eye_key[-2]))]
                if right_eye != left_eye:
                    return [eye_key.title(), right_eye.title(), left_eye.title()]
                else:
                    continue
        else:
            return eye_key.title()

    def hair_color(self):
        hair_key = random.choice(list(self.physical_features['hair color']))
        return hair_key.title()

    def eye_shape(self):
        eye_shape_key = random.choice(list(self.physical_features['eye shape']))
        return eye_shape_key.title()

    def face_shape(self):
        face_key = random.choice(list(self.physical_features['face shape']))
        return face_key.title()

    def rand_zodiac(self):
        zodiac_key = random.choice(list(self.zodiac))
        zodiac_value = self.zodiac[zodiac_key]
        emoji = zodiac_value['emoji']
        from_date = zodiac_value['from']
        to_date = zodiac_value['to']

        return [zodiac_key.title(), emoji, from_date, to_date]

    def rand_name(self, gender_type: str):
        if gender_type == 'male':
            name = random.choice(list(self.names['male']))
            return name.title()
        else:
            name = random.choice(list(self.names['female']))
            return name.title()
