"""In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit."""


def is_acceptable_password(password: str) -> bool:
    digits_in_password = False
    for x in password:
        if x.isdigit():
            digits_in_password = True
            break
    return True if len(password) > 6 and digits_in_password else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print('Тесты пройдены')
