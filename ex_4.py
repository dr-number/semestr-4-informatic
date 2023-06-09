from helpers import get_text_color, input_number, COLOR_GREEN, COLOR_FAIL, COLOR_WARNING
import math

_DEFAULT_A = 6.3
_DEFAULT_B = 5.9

def init():
    _example = (
        '     | 0.5 * t, если t > 2.4\n'
        's = <\n'
        '     | t + 2.4, если t <= 2.4,  где\n'
        't = ln(max(a, b))\n'
    )
    print(
        f'Вычислить значение {get_text_color("s", COLOR_GREEN)}, где\n'
        f'{get_text_color(_example, COLOR_GREEN)}'
    )

    a = input_number(f'Введите значение а: (по умолчанию {_DEFAULT_A})', _DEFAULT_A)
    b = input_number(f'Введите значение b: (по умолчанию {_DEFAULT_B})', _DEFAULT_B)

    print(
        f'\n{get_text_color("Исходные данные:", COLOR_WARNING)}\n'
        f'{get_text_color("a", COLOR_GREEN)} = {get_text_color(a, COLOR_GREEN)}\n'
        f'{get_text_color("b", COLOR_GREEN)} = {get_text_color(b, COLOR_GREEN)}\n'
    )

    _max = max(a, b)
    if _max == 0:
        print(get_text_color(f"Ошибка Т.к max({a}, {b}) равен 0!", COLOR_FAIL))
        return

    t = math.log(_max)
    print(f'{get_text_color("t", COLOR_GREEN)} = ln(max(a, b)) = ln(max({a}, {b})) = ln({_max}) = {t}')

    s = None
    if t > 2.4:
        s = 0.5 * t
        print(f'Т.к {t} > 2.4 => s = 0.5 * t = 0.5 * {t} = {s}')
    elif t <= 2.4:
        s = t + 2.4
        print(f'Т.к {t} <= 2.4 => s = t + 2.4 = {t} + 2.4 = {s}')

    if s is None:
        print(get_text_color(f"Ошибка Т.к t = {t} не подходит ни под одно условие задачи!", COLOR_FAIL))
        return

    print(get_text_color("\nИтоговый результат вычислений:", COLOR_GREEN))
    print(f'{get_text_color(f"s ", COLOR_GREEN)} = {get_text_color(s, COLOR_GREEN)}')
