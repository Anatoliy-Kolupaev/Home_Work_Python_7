
def read_mode_phone_book():
    """Преобразует справочник в словарь"""
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        str1 = data.read().lower().split()
        return dict(map(lambda x: tuple(x.split('//')), str1))


def write_new_contact(result):
    """Запись в телефонный справочник"""
    with open('phone_book.txt', 'a', encoding='utf-8') as data:
        data.write(f'\n{str(result)}')


def read_phone_book():
    """Чтение телефонного справочника"""
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        res = data.read()
    return res.replace('//', ' тел. ')


def clear_book():
    """Отчищает файл справочника"""
    with open('phone_book.txt', 'r+', encoding='utf-8') as data:
        data.truncate()


def create_book(n1, n2):
    """Перезаписывает справочник"""
    with open('phone_book.txt', 'a', encoding='utf-8') as data:
        data.write(f'{str(n1.capitalize())}//{str(n2)}\n')
