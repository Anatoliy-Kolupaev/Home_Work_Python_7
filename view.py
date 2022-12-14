
def choice_mode():
    """Выбор работы с телфенной книгой"""
    print('Если хотите записать новый контакт нажмите - 1')
    print('Если хотите найти контакт нажмите - 2')
    print('Если хотите посмотреть весь список контактов - 3')
    print('Если хотите удалить контакт - 4')
    return int(input('Что делаем?: '))


def get_name():
    """Получает Фамилию для поиска"""
    print()
    return input('Введите фамилию: ').lower()


def print_result(result):
    """Выводит найденный контакт"""
    print()
    print(result.capitalize())


def get_new_contact():
    """Получает данные нового контакта"""
    name = input('Введите фамилию: ')
    tel = input('Введите № телефона: ')
    print(f'Котакт создан: {name.capitalize()} тел. {tel}')
    return (f'{name}//{tel}')


def continue_work_book():
    """Продолжать работу или нет?"""
    print()
    return input('Желаете продалжить работу с телефонной книгой?: ').lower()


def delit_contact():
    """Ввод фамилии для удаления"""
    return input('Введите фамилию контакта который хотите удалить: ')
