"""Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки."""


def beginning_zeros(number):
    count = 0
    for x in number:
        if x == '0':
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print('Тесты пройдены')