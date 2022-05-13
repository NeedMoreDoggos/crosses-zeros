from menu import *
import json


def flattening(data):
    if not data:
        return []
    if isinstance(data[0], list):
        return flattening(data[0]) + flattening(data[1:])
    return [data[0]] + flattening(data[1:])


def changer(field, move, solo=False):
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


def win(kekw, move): # посмотреть это говно на свежую голову, это какой-то пиздец
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
    move = 0 + choice
    field = [[' ', ' ', ' '] for i in range(3)]
    move = 0
    player1, player2 = players(), 'AI' * solo

    while ' ' in flattening(field):
        changer(field, move, solo)
        if win(field, move):
            print('Победа!', 'Крестики' if move % 2 == 0 else 'Нолики', 'выиграли!')
            print(*field, sep='\n')
            return
        print(*field, sep='\n')
        move += 1
    else:
        print('Ничья!')

    return


def game():
    while restart():
        cz_game(solo())


# cz_game()
# print(solo())

dicti = {
    'a': 1,
    'b': 2,
    'c': 3
}


with open('json_test.txt', 'w', encoding='utf-8') as fin:
    fin.write(json.dumps(dicti, indent=4))

with open('json_test.txt', 'r', encoding='utf-8') as fon:
    print(str(fon))
    dicti2 = json.loads(fon.read())

print(dicti2)

save([[' ', ' ', ' '] for i in range(3)])
print(solo())
print(config())