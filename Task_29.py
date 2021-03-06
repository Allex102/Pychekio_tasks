"""Шахматы известны по всему миру, и практически всем людям знакомы их основные правила игры. В игре используется набор фигур,
 которые могут ходить по игровому полю различными способами, что обеспечивает огромное количество различных игровых комбинаций
 (к примеру, количество возможных шахматных партий оценивается Шенноном в 10^118). В этой задаче мы будем исследовать правила игры пешками.

Шахматы - это стратегическая игра двух игроков, которая разыгрывается на игровой доске с клетками,
расположенными в восьми рядах (называемых горизонталями и обозначаемых цифрами от 1 до 8)
и в восьми колонках (называемых вертикалями и обозначаемых буквами от a до h). Каждая клетка доски идентифицируется уникальной парой координат,
 состоящей из буквы и цифры (например, "a1", "h8", "d6"). В этой задаче мы будем иметь дело только с пешками. Пешка может бить пешку противника,
  которая находится перед ней в соседней клетке по диагонали справа или слева, переходя в эту клетку.
  У белых пешек клетки перед ними имеют номер горизонтали на единицу больше.

Сама по себе пешка является слабой фигурой, но мы можем использовать до восьми пешек для построения оборонительной стены.
Стратегия оборонительной стены основывается на защите друг друга. Пешка защищена, если её клетка находится по ударом другой своей пешки.
 На игровом поле находятся только белые пешки. Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.

Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек."""


def safe_pawns(pawns: set) -> int:
    pawn_indexes = set()
    count = 0
    for x in pawns:
        row = int(x[1]) - 1
        col = ord(x[0]) - 97
        pawn_indexes.add((row, col))
    for row, col in pawn_indexes:
        is_safe = ((row - 1, col - 1) in pawn_indexes) or ((row - 1, col + 1) in pawn_indexes)
        if is_safe:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print('Тесты пройдены')
