from import_number import import_number
from export_number import export_number



def hi_command():
    print("Приветствую!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    return [last_name, first_name, phone_number]


def deistvie():
    print("Что будем делать:\n\
    1 - импорт;\n\
    2 - экспорт;\n.")
    ch = input("Введите цифру: ")
    if ch == '1':
        import_number(input_data())
    elif ch == '2':
        data = export_number()
        print(data)