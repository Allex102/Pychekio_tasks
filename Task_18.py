"""Давайте научим наших роботов отличать слова от чисел.

Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв.
 Вам нужно проверить есть ли в исходной строке три слова подряд . Для примера, в строке "start 5 one two three 7 end" есть три слова подряд."""


def checkio(words: str) -> bool:
    words = words.split()
    counter = 0
    for x in words:
        if x.isalpha():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print('Тесты пройдены')
