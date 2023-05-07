from helpers import get_text_color, input_number, COLOR_GREEN, COLOR_FAIL, COLOR_WARNING
import math

_DEFAULT_A = 12.6
_DEFAULT_X = 0.93

def init():
    _example = (
        '     | z  , если z >= 0\n'
        'y = <  0  , если -1 <= z < 0\n'
        '     | z^2, если z < -1\n\n'
        'z = a*Sin(x)\n'
    )
    print(
        f'Вычислить значение {get_text_color("y = f + a", COLOR_GREEN)}, где\n'
        f'{get_text_color(_example, COLOR_GREEN)}'
    )

    a = input_number(f'Введите значение а: (по умолчанию {_DEFAULT_A})', _DEFAULT_A)
    x = input_number(f'Введите значение x: (по умолчанию {_DEFAULT_X})', _DEFAULT_X)

    print(
        f'\n{get_text_color("Исходные данные:", COLOR_WARNING)}\n'
        f'{get_text_color("a", COLOR_GREEN)} = {get_text_color(a, COLOR_GREEN)}\n'
        f'{get_text_color("x", COLOR_GREEN)} = {get_text_color(x, COLOR_GREEN)}\n'
    )
    

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

    print(f'{get_text_color(f"f = {f}", COLOR_GREEN)}\n')
    print(f'{get_text_color("Итоговый результат вычислений:", COLOR_GREEN)}\n')
    print(f'{get_text_color(f"y ", COLOR_GREEN)} = f + a = {f} + {a} {get_text_color(f"= {f + a}", COLOR_GREEN)}')
