from random import choice


# Отдельно прописываю все это безобразие выбора, чтобы не запутаться окончательно в этом обилии функций.
# Тут алгоритмы выбора


def easy_ai(field):
    """
    Просто бежим по полю. Ищем пустые клетки. Заносим их в список. Потом случайно выбираем одну
    :param field: Текущее игровое поле.
    :return: Координаты клетки
    """
    choices = list()

    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == ' ':
                choices += [[i, j]]

    return choice(choices)


def is_diagonal(cont):
    """
    Проверяем, находится ли точка на диагонали.
    :param cont: Координаты точки.
    :return: True -- если лежит. False -- если не лежит.
    """
    x, y = cont
    if x - y == 0:
        return True
    if x + y == 2:
        return True


def diagonal_score(field, cont):
    """
    Находим очки диагоналей. Суть та же, что и в линиях. С.м. ниже
    :param field: Текущее игровое поле.
    :param cont: Координаты точки.
    :return: Кол-во очков.
    """
    x, y = cont
    sum = 0
    counter1 = dict()
    counter2 = dict()

    if x == y:
        for i in range(len(field)):
            counter1[field[i][i]] = counter1.setdefault(field[i][i], 0) + 1
    if x + y == 2:
        for i in range(len(field)):
            counter2[field[0 + i][2 - i]] = counter2.setdefault(field[0 + i][2 - i], 0) + 1

    if counter1.get('0') == 2 or counter2.get('0') == 2:
        return 9999
    if counter1.get('X') == 2 or counter2.get('X') == 2:
        return 4999
    if len(counter1) == 1:
        sum += 10
    if len(counter2) == 1:
        sum += 10
    if len(counter1) == 2:
        sum += 20
    if len(counter2) == 2:
        sum += 20

    return sum





def is_trap(field, cont):
    """
    Очень важная функция, которая предотвращает проблему моей логики. Нужно проверить следующее. Если я вынуждаю
    противника поставить фигуру в только одном месте, не окажется ли так, что закрыв свое поражение, он получит сразу
    2 выигрышных случая? Пример:
    X - 0
    - 0 -    => куда бы не поставил нолик, он проиграл
    X - X
    :param field: Игровое поле.
    :param cont: Координаты икса, который будет поставлен, чтобы предотварить поражение. Хотя мб точно пока не уверен.
    :return:
    """
    pass


def line_score(field, cont):
    """
    Ищем сколько очков у клетки по линиям. Если есть 2 клетки уже одного цвета => 9999, ставить точно надо суда.
    Если есть и 0 и Х, то линия не выигрышная и не проигрывает, ее игнорируем. По умолчанию ноль этой линии.
    Она не интересна. Интересны только пустые линии которые содержат элементы одного типа. На них мы можем как проиграть
    так и выиграть. В зависимости от того, что там может быть поставлено. Проблема пока в том, как оценивать
    все это дело. У каждой клетки есть от 2 до 4 линий. Именно на эти линии она и влияет. Интересующие варианты:
    ['X', ' ', ' '] -- Линия с одним элементом игрока. 1 приоритет.
    [' ', ' ', ' '] -- Пустая линия. 2 приоритет.
    ['0', ' ', ' '] -- Линия с одним элементом врага. 3 приоритет.
    Постановка элемента в линию, со своим элементом, вынудит закрываться опа, чтобы не проиграть. Это => чем просто
    заблокировать ему победу


    :param field: Поле для оценок.
    :param cont: Координаты точки.
    :return: Вес клетки.
    """
    x, y = cont
    sum = 0
    counter1 = dict()
    counter2 = dict()

    for i in range(len(field)):
        counter1[field[x][i]] = counter1.setdefault(field[x][i], 0) + 1
        counter2[field[i][y]] = counter2.setdefault(field[i][y], 0) + 1

    if counter1.get('0') == 2 or counter2.get('0') == 2:
        print('ping 1')
        return 9999
    if counter1.get('X') == 2 or counter2.get('X') == 2:
        print('ping 2')
        return 4999
    if len(counter1) == 1:
        sum += 10
    if len(counter2) == 1:
        sum += 10
    if len(counter1) == 2:
        sum += 20
    if len(counter2) == 2:
        sum += 20

    return sum


def score(field, cont):
    """
    Получаем сумму весов линий клетки.
    :param field: Текущая игровая ситуация.
    :param cont: Коордиаты клетки.
    :return: Сумма веса всех линий.
    """
    sum = 0

    sum += line_score(field, cont)
    if is_diagonal(cont):
        sum += diagonal_score(field, cont)

    return sum


def medium_ai(field):
    """
    Считаем очки каждой свободной клетки. Потом выбираем клетку с наибольшим кол-вом очкой
    :param field: Текущее игровое поле
    :return: Координаты клетки
    """
    scores = list()

    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == ' ':
                scores += [[[i, j], score(field, [i, j])]]

    return max(scores, key=lambda x: x[1])[0]


test = [
    ['0', ' ', ' '],
    [' ', 'X', ' '],
    ['X', ' ', ' ']
]
# print(easy_ai(test))
# print(medium_ai(test))
# print(test[2][0])