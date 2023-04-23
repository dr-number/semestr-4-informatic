from helpers import get_text_color, input_number, COLOR_GREEN, COLOR_FAIL
import math

_DEFAULT_A = 12.6
_DEFAULT_X = 0.93

def init():
    print(
        f'Вычислить значение {get_text_color("y = f + a", COLOR_GREEN)}, где\n'
        f'     | z  , если z >= 0\n'
        f'y = <  0  , если -1 <= z < 0\n'
        f'     | z^2, если z < -1\n\n'
        f'z = a*Sin(x)\n'
    )

    a = input_number(f'Введите значение а: (по умолчанию {_DEFAULT_A})', _DEFAULT_A)
    x = input_number(f'Введите значение x: (по умолчанию {_DEFAULT_X})', _DEFAULT_X)

    sin_x = math.sin(x) 
    z = a * sin_x
    print(f'{get_text_color("z", COLOR_GREEN)} = a * Sin(x) = {a} * Sin({x}) = {a} * {sin_x} = {z}')
    
    f = None
    if z >= 0:
        f = z
        print(f'Т.к {z} >= 0 => f = {f}')
    elif -1 <= z < 0:
        f = 0
        print(f'Т.к -1 <= {z} < 0 => f = 0')
    elif z < -1:
        f = z*z
        print(f'Т.к {z} < -1 => f = z^2 = {f}')

    if f is None:
        print(
            f'{get_text_color(f"Ошибка Т.к z = {z} не подходит ни под одно условие задачи!", COLOR_FAIL)}'
        )
        return

    print(f'\n{get_text_color(f"f = {f}", COLOR_GREEN)}')
    print(f'\n{get_text_color(f"y ", COLOR_GREEN)} = f + a = {f} + {a} {get_text_color(f"= {f + a}", COLOR_GREEN)}')
