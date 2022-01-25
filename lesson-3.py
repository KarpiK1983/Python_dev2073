# # Задание 1. 2.
#
# number_1 = input('Число на английском строчными буквами: ')
# number_2 = input('Число на английском: ')
# interpreter = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
#                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
# #
# def num_translate(number_1):
#     return interpreter.get(number_1)
# #
# print(num_translate(number_1))
# ############################################
#
# def num_translate_adv(number_2):
#     if number_2[0] == number_2[0].upper():
#         number_2 = number_2.lower()
#         return interpreter[number_2].capitalize()
#     else:
#         return interpreter[number_2]
#
#
# print(num_translate_adv(number_2))

# Задание 3.

# def thesaurus(*names):
#     result_dict = {}
#     for name in names:
#         result_dict.setdefault(name[0], [])
#         result_dict[name[0]].append(name)
#     return result_dict
#
# print(thesaurus('Коля', 'Света', 'Карина', 'Клеопатра', 'Саня', 'Анна', 'Александр'))

# Задание 4.

# def thesaurus_adv(*names_surnames):
#     result_dict = {}
#     for name_surname in names_surnames:
#         name, surname = name_surname.split()
#         result_dict.setdefault(surname[0], {})
#         result_dict[surname[0]].setdefault(name[0], [])
#         result_dict[surname[0]][name[0]].append(name_surname)
#     return result_dict
#
# print(thesaurus_adv('Алекс Блок', 'Александр Пушкин', 'Сергей Есенин', 'Иван Сусанин', 'Саша Грей', 'Джемс Бонд',))


# Задание 5.

# import random
#
# name = ['Коля', 'Вова', 'Дима', 'Саня', 'Платон', 'Александр']
# when = ['сегодня', 'вчера был', 'завтра будет', 'позавчера был', 'ночью будет']
# situation = ['пьяный', 'в ударе', 'в огне', 'голый', 'злой', 'в неадеквате']
# number = int(input('Сколько хотите шуток?: '))
# 
#
# def get_jokes(num):
#     joke_list = []
#     for i in range(num):
#         cur_name = random.choice(name)
#         cur_when = random.choice(when)
#         cur_situation = random.choice(situation)
#         joke_list.append(f'{cur_name} {cur_when} {cur_situation}')
#     return joke_list
# print(get_jokes(number))