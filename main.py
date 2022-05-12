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


def win(kekw, move): # посмотреть это говно на свежую голову

    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            return True
        if field[0][i] == field[1][i] == field[2][i]:
            return True
    if field[0][0] == field[1][1] == field[2][2]:
        return True
    if field[2][0] == field[1][1] == field[0][2]:
        return True
    print(field)
    return False


def cz_game(solo=False, choice=False):
    move = 0 + choice
    field = [[' ', ' ', ' '] for i in range(3)]
    move = 0

    while ' ' in flattening(field):
        changer(field, move, solo)
        if win(field, move):
            print('Победа!', 'X' if move % 2 == 0 else '0', 'выиграли')
            return
        print(*field, sep='\n')
        move += 1
    else:
        print('Ничья!')

    return


cz_game()