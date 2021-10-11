"""Дана строка и нужно найти ее первое слово.

Это упрощенная версия миссии First Word , которую можно решить позднее.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет."""

def first_word(text):
    text= text.split(' ')
    return str(text[0])


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!") 