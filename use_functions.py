"""
МОДУЛЬ 3
"""
# Программа "Личный счет"
# Описание работы программы:
# Пользователь запускает программу у него на счету 0
# Программа предлагает следующие варианты действий
# 1. пополнить счет
# 2. покупка
# 3. история покупок
# 4. выход

invoice_amount = 0
purchase_history = []

while True:
    print('1. ПОПОЛНЕНИЕ СЧЕТА')
    print('2. ПОКУПКА')
    print('3. ИСТОРИЯ ПОКУПОК')
    print('4. ВЫХОД')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        refil = int(input("Пополните ваш счет, введя сумму: "))
        invoice_amount += refil
    elif choice == '2':
        refil = int(input("Введите сумму покупки: "))
        if refil >invoice_amount:
            print("К сожалению, у вас недостаточно денег")
        else:
            invoice_amount -= refil
            purchase_name = str(input("Введите название покупки: "))
            purchase_history.append((purchase_name, refil))

    elif choice == '3':
        print(purchase_history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
