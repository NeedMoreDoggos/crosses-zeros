import json


def solo():
    """
    Сколько игроков.
    :return: Один -- True. Два -- False.
    """
    players = input('Введите кол-во игроков "Один" или "Два" => ').upper()
    while not players in ('ОДИН', 'ДВА'):
        players = input(f'Введите корректное кол-во игроков. Вы введи {players} Введите заново => ').upper()
    return players == 'ОДИН'


def choice():
    """
    Выбор 0 или Х будет играть 1 игрок.
    :return: True --  0. False -- Х.
    """
    symbol = input('Введите желаемый символ "X" или "0" => ').upper()
    while not symbol in ('X', '0'):
        symbol = input(f'Вы ввели {symbol}. Нужно вветси "X" или "0". Введите заново => ').upper()
    return symbol == '0'


def read_config():
    """
    Читаем конфиг. Его немного перепишу под задачу. Я в начале попробу через json сделать. Мне кажется, с ним будет
    сильно удобнее. Потом переделаю если что.
    :return: Словарик конфигурации
    """
    with open('config.txt', 'r', encoding='utf-8') as fin:
        config = json.loads(fin.read())
    return config


def write_config(new_con):
    """
    Записываем изменения.
    :param new_con: Изменения, который произошли.
    :return: NoneType
    """
    with open('config.txt', 'w', encoding='utf-8') as fon:
        fon.write(json.dumps(new_con))


def config():
    """
    Загрузка настроек и состояний. Тоже подделаю под задачи.
    :return: NoneType
    """
    try:
        return read_config()
    except:
        conf = {
            'duo_score': dict(),
            'solo_score': dict(),
            'first_run': True
        }
        write_config(conf)
        return conf


def players():
    """
    Ввод имен игроков.
    :return: 1/2 имени
    """
    return input('Введите имя/имена').split()


def load(name1, name2):
    """
    Зачатки загрузки. Сделаю просто словарик с картежами именами игроков и полем.
    :return: Игровое поле.
    """
    try:
        with open('save.txt', 'r', encoding='utf-8') as fin:
            return json.loads(fin.read())[(name1, name2)]
    except:
        print('Сохранения не найдеы')
        return {(name1, name2): [[' ', ' ', ' '] for i in range(3)]}


def save(name1, name2, field):
    """
    Сохраняем текущее безобразие.
    :param field: Текущее поле.
    :return: NoneType
    """
    for_save = load(name1, name2)
    for_save[(name1, name2)] = field
    with open('save.txt', 'w', encoding='utf-8') as fot:
        fot.write(json.dumps(for_save))


def prep_game():
    pass
