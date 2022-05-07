from randomizer import Randomizer

randomizer = Randomizer()

def menu():
    user_options = ['random male', 'random female']
    while True:
        user_text_input = input('What would you like to do today? Type (help) for options. \n').lower()
        if user_text_input == 'help':
            print(user_options)
            continue
        elif user_text_input not in user_options:
            print('That is not a valid response. Try again.')
            continue
        elif user_text_input in user_options:
            """menu items"""
            if user_text_input == user_options[0]:
                """random male"""
                randomizer.rand_person(gender_type='male')
            elif user_text_input == user_options[1]:
                """random female"""
                randomizer.rand_person(gender_type='female')


menu()