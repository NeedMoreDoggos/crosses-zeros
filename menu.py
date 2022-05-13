def solo():
    players = input('Введите кол-во игроков "Один" или "Два"')
    while not players in ('Один', 'Два'):
        players = input(f'Введите корректное кол-во игроков. Вы введи {players}')
    if players == 'Два':
        return False
    return True


def read_config():
    with open('config.txt', 'r', encoding='utf-8') as fin:


def players():
    return input('Введите имя/имена').split()