from menu import *
from AIs import *
import json

# Ну в чем суть. Я собираю итоговую программу из 3 модулей, который состоят из миллиардов функций.
# Одна -- чтобы править ими. Одна -- чтобы найти их. Одна -- чтоб возвратить и тьмой оплести. В тьмой окутанном проекте.
# Мне просто проще как-то дописывать, когда видишь результат работы. Тут как раз можно в "двоем" поиграть без всего.
# Оно работает. И дописывать так, исходя из того, что у тебя оно работало, если ты что-то сломал,
# то сломал где-то в свежем месте.

    # такой подход к проектированию существует и называется "заплаточной" разработкой,
    #     "костыльным" программированием, а в особо тяжёлых случаях
    #     ректальным программированием (https://habr.com/ru/post/595301)
    #
    # его можно использовать для всякой мелочёвки или для прототипирования – ради скорости –
    #     но настоятельно не рекомендую принимать его для себя в качестве основного
    # главные причины в том, что:
    #     1. по мере нарастания сложности программа становится большим комком
    #        неструктурированного кода, который очень сложно переписать
    #     2. подход становится привычкой, а основным стилем разработки
    #        становится, соответственно, говно-кодинг
    #
    # помните, что каждый раз, когда программист пишет плохой код – Бог убивает котёнка
    #
    # код детально проанализирую и прокомментирую на днях, пока некогда было
    #
    # как комментировать коммиты:
    # https://habr.com/ru/post/416887


def flattening(data):
    """
    Разворачивает поле. Так удобней искать пустые клетки.
    :param data: Список списков.
    :return: Разворачивает все в один список.
    """
    if not data:
        return []
    if isinstance(data[0], list):
        return flattening(data[0]) + flattening(data[1:])
    return [data[0]] + flattening(data[1:])


def changer(field, move, solo=True):
    """
    Заполняет пустую клетку по координатам. Скорее всего, я перепишу ее так, что координаты будут поступать из вне.
    Но я пока не решил это.
    :param field: Игровое поле.
    :param move: Номер хода.
    :param solo: Кол-во игроков.
    :return: NoneType
    """
    if solo and move % 2 == 1:
         coordinates = medium_ai(field)
    else:
        coordinates = [int(digit) - 1 for digit in input('Введите X, Y через пробел => ').split() if digit.isdigit()]

    if len(coordinates) != 2:
        print(f'Должно быть 2 координаты. У вас {coordinates}')
        return changer(field, move, solo)
    if not 0 < coordinates[0] + 1 < 4 or not 0 < coordinates[1] + 1 < 4:
        print(f'Координата X:{coordinates[0] + 1}, Координата Y: {coordinates[1] + 1}. Координаты должны быть от 1 до 3 включительно')
        return changer(field, move, solo)
    if field[coordinates[0]][coordinates[1]] in 'X0':
        print(f'Клеточка уже занята {field[coordinates[0]][coordinates[1]]}')
        return changer(field, move, solo)

    field[coordinates[0]][coordinates[1]] = 'X' if move % 2 == 0 else '0'
    return


def win(kekw, move):
    """
    Проверку на победу. Пока она работает и в таком режиме. Потом будет переписано.
    По сути, это просто проверка условий для if'а.
    :param kekw: Поле игровое.
    :param move: Номер хода.
    :return: True -- есть победа. False -- нет победы.
    """
    field = [[1+3*i, 2+3*i, 3+3*i]for i in range(3)]
    for i in range(3):
        for j in range(3):
            if kekw[i][j] != ' ':
                field[i][j] = kekw[i][j]

    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            return True
        if field[0][i] == field[1][i] == field[2][i]:
            return True
    if field[0][0] == field[1][1] == field[2][2]:
        return True
    if field[2][0] == field[1][1] == field[0][2]:
        return True

    return False


def cz_game(settings):
    """
    Зачаток функции, который будет запускать процесс самой игры. Оно игается, но пока логика работы не до
    конца определена. Я думаю, как суда кидать аргументы из save'а.
    :argument Словарь с настройками.
    :return: NoneType
    """
    move = 0 + settings['choice']
    if settings.get('load', False):
        field = [[' ', ' ', ' '] for i in range(3)]
    else:
        field = settings['load']['field']

    while ' ' in flattening(field):
        changer(field, move, settings['solo'])
        if win(field, move):
            print('Победа!', 'Крестики' if move % 2 == 0 else 'Нолики', 'выиграли!')
            print(*field, sep='\n')
            return
        print(*field, sep='\n')
        move += 1
    else:
        # Последний ход заполниться выше. И сразу же провериться. Else от while'а. Если нет пустых клеток и
        # нет победной ситуации => ничья.
        print('Ничья!')

    return


def start_game():
    settings = prep_game()
    leave = ''

    while leave not in ('выход', 'out'):
        cz_game(settings)
        leave = input('Напишите "выход" или "out", чтобы выйти')

    return


start_game()


