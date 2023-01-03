def choose_mode():
    print('Добро пожаловать в калькулятор!')
    print('Выберите действие')
    print('1 - Посчитать пример')
    print('2 - Посчитать уравнение')
    print('3 - Упростить уравнение')
    print('4 - Показать историю вычислений')
    choice = int(input())
    return choice


def user_input():
    choice = input('Введите выражение: ')
    return choice

def error_message(choice):
    if choice != 1 or choice != 2 or choice != 3:
        print('Нет такого действия')

def print_ans(example, ans):
    print(f'{example} = {ans}')

def print_x(ans):
    print(f'x = {ans}')

def print_history(history):
    print(history)