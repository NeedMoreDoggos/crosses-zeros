from random import choice


# Отдельно прописываю все это безобразие выбора, чтобы не запутатьс окончательно в этом обилии функций.
# Тут алгоритмы выбора


def easy_ai(field):
    """
    Просто бежим по полю. Ищем пустые клетки. Заносим их в список. Потом случайно выбираем одну
    :param field: Текущее игровое поле
    :return: Координаты клетки
    """
    choices = list()

    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == ' ':
                choices += [[i, j]]

    return choice(choices)


def line_score(field, cont):
    """
    Ищем сколько очков у клетки по линиям. Если есть 2 клетки уже одного цвета => 9999, ставить точно надо суда.
    Если есть и 0 и Х, то линия не выигрышная, ее игнорируем. По умолчанию нольэтой линии. Она не интересна.
    :param field:
    :param cont:
    :return:
    """
    x, y = cont
    sum = 0
    counter1 = dict()
    counter2 = dict()

    for i in range(len(field)):
        counter1[field[x][i]] = counter1.setdefault(field[x][i], 0) + 1
        counter2[field[i][y]] = counter2.setdefault(field[i][y], 0) + 1

    if counter1['X'] = 2 or counter1['0'] = 2 or counter2['X'] = 2 or counter2['0'] = 2:
        return 9999


def score(field, cont):
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
                scores += [[i, j], score(field, [i, j])]

    return max(scores, key=lambda x: x[1])[0]



test = [['X', ' ', ' '] for _ in range(3)]
print(easy_ai(test))