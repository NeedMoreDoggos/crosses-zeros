from random import choice


# Отдельно прописываю все это безобразие выбора, чтобы не запутатьс окончательно в этом обилии функций.
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

    if counter1['X'] = 2 or counter1['0'] = 2 or counter2['X'] = 2 or counter2['0'] = 2:
        return 9999


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
                scores += [[i, j], score(field, [i, j])]

    return max(scores, key=lambda x: x[1])[0]



test = [['X', ' ', ' '] for _ in range(3)]
print(easy_ai(test))