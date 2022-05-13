import json


def solo():
    players = input('Введите кол-во игроков "Один" или "Два" => ')
    while not players in ('Один', 'Два'):
        players = input(f'Введите корректное кол-во игроков. Вы введи {players} Введите заново => ')
    return players == 'Один'


def choice():
    symbol = input('Введите желаемый символ "X" или "0" => ')
    while not symbol in ('X', '0'):
        symbol = input(f'Вы ввели {symbol}. Нужно вветси "X" или "0". Введите заново => ')
    return symbol == '0'


def read_config():
    with open('config.txt', 'r', encoding='utf-8') as fin:
        config = json.loads(fin.read())
    return config


def players():
    return input('Введите имя/имена').split()


def load():
    try:
        with open('save.txt', 'r', encoding='utf-8') as fin:
            field = json.loads(fin.read())
            return field
    except:
        print('Сохранения не найдеы')
        return [[' ', ' ', ' '] for i in range(3)]


def save(field):
    with open('save.txt', 'w', encoding='utf-8') as fot:
        fot.write(json.dumps(field))