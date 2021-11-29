"""Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой."""


def date_time(time: str) -> str:
    time = time.replace('.', ' ')
    time = time.replace(':', ' ')
    time = time.split(' ')
    if time[0][0] == '0':
        time[0] = time[0][1]
    day = time[0]
    month = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
             '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    year = time[2] + ' year'
    if time[3][0] == '0':
        time[3] = time[3][1]
    if time[3] == '1':
        hour = time[3] + ' hour'
    else:
        hour = time[3] + ' hours'
    if time[4][0] == '0':
        time[4] = time[4][1]
    if time[4] == '1':
        minute = time[4] + ' minute'
    else:
        minute = time[4] + ' minutes'
    return f'{day} {month[time[1]]} {year} {hour} {minute}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print('Тесты пройдены')
