from menu import *
import json

# я бы с раздела помощи начал
# заодно сам себе в голове уложил: что я хочу пользователю вывести, а что от него получить и в каком виде

# используй чёртовы комментарии! описывай, что делаешь!
def flattening(data):
    if not data:
        return []
    if isinstance(data[0], list):
        return flattening(data[0]) + flattening(data[1:])
    return [data[0]] + flattening(data[1:])

# используй чёртовы комментарии! описывай, что делаешь!
def changer(field, move, solo=False):
    # такие длинные строки не приветствуются, их неудобно читать
    # в чём проблема написать нормальный if not solo ?
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

# используй чёртовы комментарии! описывай, что делаешь!
def win(kekw, move):
    # нафига мы map(), all() lambda-функции проходили?...
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

# используй чёртовы комментарии! описывай, что делаешь!
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
        # а последний ход разве прям никогда не может быть выигрышным?
        print('Ничья!')

    return

# используй чёртовы комментарии! описывай, что делаешь!
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

# используй чёртовы комментарии! описывай, что делаешь!
with open('json_test.txt', 'w', encoding='utf-8') as fin:
    fin.write(json.dumps(dicti, indent=4))

with open('json_test.txt', 'r', encoding='utf-8') as fon:
    print(str(fon))
    dicti2 = json.loads(fon.read())

print(dicti2)

save([[' ', ' ', ' '] for i in range(3)])
print(solo())
print(config())


# за такие commit messages – грохну весь проект, будешь с нуля писать!
# пошутить можно в коде в комментах, но не в коммитах!
# и это тебе любой тимлид скажет – на случай, если думаешь, что я якобы к ерунде придираюсь
