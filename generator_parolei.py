from random import *

def questions():
    DIGITS = '0123456789'
    LOW_L = 'abcdefghijklmnopqrstuvwxyz'
    UP_L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOL = '!#$%&*+-=?@^_'
    password = ''

    quant_password = input('\nСколько паролей Вам нужно сгенерировать?(цифра): ')
    len_password = input('Какой длины пароль(и) Вам нужно?(цифра не менее 4): ')
    need_digit = input('Включать ли в пароль цифры?("да" или "нет"): ')
    need_up_l = input('Включать ли в пароль ПРОПИСНЫЕ буквы?("да" или "нет"): ')
    need_low_l = input('Включать ли в пароль строчные буквы?("да" или "нет"): ')
    need_symbol = input('Включать ли в пароль символы "!#$%&*+-=?@^_" ?("да" или "нет"): ')
    need_except = input('Нужно ли ИСКЛЮЧИТЬ неоднозначные символы "il1Lo0O"?("да" или "нет"): ')

    if not quant_password.isdigit() or not len_password.isdigit() or int(len_password) < 4 or int(
            quant_password) < 1:  # защита от дураков на цифры
        print('Где-то вы ошиблись с ответом. Вам нужно к ним вернуться.')
        questions()

    check_answer = [need_digit, need_up_l, need_low_l, need_symbol, need_except]
    for check in check_answer:  # защита от дураков на да/нет
        if check.lower() not in ['да', 'нет', 'lf', 'ytn']:
            print('Где-то вы ошиблись с ответом. Вам нужно к ним вернуться.')
            questions()

    for _ in range(int(quant_password)):

        c = 0
        for i in range(4):  # сколько частей пароля должно быть
            if check_answer[i].lower() in ['да', 'lf']:
                c += 1

        n = (int(len_password) // c)  # сколько символов нужно
        t = (int(len_password) % c)  # есть ли хвост, если число символов нечётное

        if need_except == 'да' or need_except == 'lf':  # убираем неоднозначные символы
            DIGITS = '23456789'
            LOW_L = 'abcdefghjkmnpqrstuvwxyz'
            UP_L = 'ABCDEFGHJKMNPQRSTUVWXYZ'

        if need_digit == 'да' or need_digit == 'lf':  # добавляю в пароль цифры
            for i in range(n):
                password += choice(DIGITS)

        if need_up_l == 'да' or need_up_l == 'lf':  # добавляю в пароль большие буквы
            for i in range(n):
                password += choice(UP_L)

        if need_low_l == 'да' or need_low_l == 'lf':  # добавляю в пароль маленькие буквы
            for i in range(n):
                password += choice(LOW_L)

        if need_symbol == 'да' or need_symbol == 'lf':  # добавляю в пароль маленькие буквы
            for i in range(n):
                password += choice(SYMBOL)

        if t > 0:  # получаем нужное количество символов по хвосту
            for i in range(t):
                if need_digit == 'да' or need_digit == 'lf':
                    password += choice(DIGITS)
                elif need_up_l == 'да' or need_up_l == 'lf':
                    password += choice(UP_L)
                elif need_low_l == 'да' or need_low_l == 'lf':
                    password += choice(LOW_L)
                elif need_symbol == 'да' or need_symbol == 'lf':
                    password += choice(SYMBOL)

        l_pass = ' '.join(password).split()
        shuffle(l_pass)
        print('-' * int(len_password))
        print(''.join(l_pass), sep='\n')
        password = ''


agree = input(
    'Здравствуйте! Я - Генератор Паролей.\n \nДля корректной генерации паролей по Вашим предпочтениям, ответьте на несколько вопросов.\n'
    'Если согласны, напишите "ДА: ')
if agree.lower() in ('да', 'lf'):
    print('\nОтвечайте на вопросы корректно, иначе придётся отвечать на них повторно.')
    questions()
else:
    print('\nКогда передумаете - Добро пожаловать в Генератор Паролей!\nВсего Вам доброго!')