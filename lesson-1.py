# Задание 1. Расчет времени

# secunds = input('Введите колочество секунд:')
# secunds = int(secunds)
# minutes = secunds // 60
# hour = secunds // 3600
# day = secunds // 86400
#
# if secunds < 60:
#     print(secunds, 'сек.')
# elif minutes < 60:
#     print(minutes, 'мин.', secunds % 60, 'сек.')
# elif hour < 24:
#     print(hour, 'ч.', minutes % 60, 'мин.', secunds % 60, 'сек.')
# else:
#     print(day, 'дн.', hour % 24, 'ч.', minutes % 60, 'мин.', secunds % 60, 'сек.')


# Задание 2.

# my_list = list(range(1, 1000, 2))
# indx = 0
#
# while indx < len(my_list):
#     my_list[indx] = my_list[indx] ** 3
#     indx += 1
#
# final_sum = 0
# for num in my_list:
#     num += 17
#     check_sum = 0
#     for check_num in str(num):
#         check_sum += int(check_num)
#     if check_sum % 7 == 0:
#         final_sum += num
# print(final_sum)


# Задание 3.

# declination = list(range(1, 101))
#
# print(declination)
# for inxt in declination:
#     if 10 < inxt < 15: # исключение
#         print(f'{inxt} процентов')
#     elif inxt % 10 == 1:
#         print(f'{inxt} процент')
#     elif 1 < inxt % 10 < 5:
#         print(f'{inxt} процента')
#     else:
#         print(f'{inxt} процентов')