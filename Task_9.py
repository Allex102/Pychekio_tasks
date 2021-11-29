"""У вас есть число и нужно определить какая цифра из этого числа является наибольшей."""


def max_digit(number):
    return int(max(list(str(number))))


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print('Тесты пройдены')
