import logger


def check_name(base, name):
    """Ищет имя и тел в справочнике"""
    if name in base:
        return f'{name} тел: {base[name]}'
    else:
        return 'Такой Фамилии нет в телефонной книге'


def check_name_for_del(str1, name):
    if name in str1:
        str1.pop(name)
    else:
        print()
        print('Такого контакта нет')
    str1 = list(str1.items())
    for i in str1:
        logger.create_book(i[0], i[1])
