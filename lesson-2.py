# Задание 1

# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))


# Задание 2.

# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# my_list2 = []
# temp_list = [] # лист для манипуляций
#
# for inxt in my_list:
#     if inxt.isdigit(): # ищу число в исходном списке.
#         temp_list.append(''.join(['"', f'{int(inxt):02}', '"']))
#         my_list2.extend(temp_list) # добавляю в список результат
#         temp_list.clear() # но это совсем ломает работу кода
#
#     elif (inxt.startswith('+') or inxt.startswith('-')) and inxt[1:].isdigit():
#         temp_list.append(''.join(['"', f'{inxt[0]}{int(inxt[1:]):02}', '"']))
#         my_list2.extend(temp_list)  # добавляю в список результат
#         temp_list.clear()  # но это совсем ломает работу кода
#     else:
#         my_list2.append(inxt) # если это не число до добавляю его в список 2
#
# my_list2 = ' '.join(my_list2)
# print(my_list2)


# Задание 3

# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# for inxt in my_list:
#     print('Привет,', inxt.split()[-1].title())


# Задание 4

# price = [57.8, 46.51, 97, 26, 56.51, 98.16, 77.77, 12, 91.77, 27.42, 1.05, 7.99]
# print('ID изначльного списка (price)', id(price))
# price.sort()
# print('ID отсортированного списка (price)', id(price))
#
# for pr in price:
#     r = int(pr)
#     k = (pr - int(pr)) * 100
#     print(f'{r} руб {k:02.0f} коп', end=', ')
#
# price2 = price[::-1]
# print(end='\n\n')
# print('Новый списк с ценой по убыванию', price2)
# print('ID новго списка (price2)', id(price2))
#
# for pr in price2[::1][:5]:
#     r = int(pr)
#     k = (pr - int(pr)) * 100
#     print(f'{r} руб {k:02.0f} коп', end=', ')