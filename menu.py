import json


def solo():
    players = input('Введите кол-во игроков "Один" или "Два" => ').upper()
    while not players in ('ОДИН', 'ДВА'):
        players = input(f'Введите корректное кол-во игроков. Вы введи {players} Введите заново => ').upper()
    return players == 'ОДИН'


def choice():
    symbol = input('Введите желаемый символ "X" или "0" => ').upper()
    while not symbol in ('X', '0'):
        symbol = input(f'Вы ввели {symbol}. Нужно вветси "X" или "0". Введите заново => ').upper()
    return symbol == '0'


def read_config():
    with open('config.txt', 'r', encoding='utf-8') as fin:
        config = json.loads(fin.read())
    return config


def write_config(new_con):
    with open('config.txt', 'w', encoding='utf-8') as fon:
        fon.write(json.dumps(new_con))


def config():
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
    return input('Введите имя/имена').split()


def load():
    try:
        with open('save.txt', 'r', encoding='utf-8') as fin:
            return json.loads(fin.read())
    except:
        print('Сохранения не найдеы')
        return [[' ', ' ', ' '] for i in range(3)]


def save(field):
    with open('save.txt', 'w', encoding='utf-8') as fot:
        fot.write(json.dumps(field))


