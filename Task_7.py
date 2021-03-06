"""Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True."""


def is_all_upper(text):
    return text == text.upper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print('Тесты пройдены')
