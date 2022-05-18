from menu import *
import json

# Ну в чем суть. Я собираю итоговую программу из 3 модулей, который состоят из миллиардов функций.
# Одна -- чтобы править ими. Одна -- чтобы найти их. Одна -- чтоб возвратить и тьмой оплести. В тьмой окутанном проекте.
# Мне просто проще как-то дописывать, когда видишь результат работы. Тут как раз можно в "двоем" поиграть без всего.
# Оно работает. И дописывать так, исходя из того, что у тебя оно работало, если ты что-то сломал,
# то сломал где-то в свежем месте.


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


def changer(field, move, solo=False):
    """
    Заполняет пустую клетку по координатам. Скорее всего, я перепишу ее так, что координаты будут поступать из вне.
    Но я пока не решил это.
    :param field: Игровое поле.
    :param move: Номер хода.
    :param solo: Кол-во игроков.
    :return: NoneType
    """
    coordinates = [int(digit) - 1 for digit in input('Введите X, Y через пробел => ').split() if digit.isdigit()] if not solo else AI(field, )

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


def cz_game(solo=False, choice=False):
    """
    Зачаток функции, который будет запускать процесс самой игры. Оно игается, но пока логика работы не до
    конца определена. Я думаю, как суда кидать аргументы из save'а.
    :param solo: Режим.
    :param choice: Х или 0.
    :return: NoneType
    """
    move = 0 + choice
    field = [[' ', ' ', ' '] for i in range(3)]
    move = 0
    player1, player2 = players(), 'AI' * solo #думаю о том, как лучше вводить имена

    while ' ' in flattening(field):
        changer(field, move, solo)
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



# cz_game()
# print(solo())

dicti = {
    'a': 1,
    'b': 2,
    'c': 3
}

# Тестовые записи. Тут нет ничего интересно. Просто подсказки для самого себя о том, как это работает.
with open('json_test.txt', 'w', encoding='utf-8') as fin:
    fin.write(json.dumps(dicti, indent=4))

with open('json_test.txt', 'r', encoding='utf-8') as fon:
    print(str(fon))
    dicti2 = json.loads(fon.read())

print(dicti2)

save([[' ', ' ', ' '] for i in range(3)])
print(solo())
print(config())

