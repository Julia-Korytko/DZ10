"""
МОДУЛЬ 2
"""
# Задание: переписать код используя как минимум 1 функцию

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
#
# day = input('Ввведите день рождения Пушкина?')
# while day != '6':
#     print("Не верно")
#     day = input('Ввведите день рождения Пушкина?')
# print('Верно')

def question_bornday(ask_bornday, date):
    bornday = input(ask_bornday)
    while bornday != date:
        print("Не верно")
        bornday = input(ask_bornday)


question_bornday('Ввведите год рождения А.С.Пушкина:', '1799')
question_bornday('Ввведите день рождения Пушкина?', '6 июня') # Веести день рождения в формате день месяц

print('Верно')
