from helpers import get_text_color, COLOR_GREEN, COLOR_FAIL
import math
import cmath

def init():
    print(
        f'Вычислить значение {get_text_color("F = y + 5.6", COLOR_GREEN)}, где\n'
        f'     | √-1              , если x >= 1\n'
        f'y = <\n'
        f'     | Cos(e^x - 1)^e^x , если x < 1\n\n'
        f'x = Sin^2(a) + Cos(a)^2;    a = π/5\n'
    )

    a = math.pi/5
    sin_a = math.sin(a)
    cos_a = math.cos(a)
    sin_pow_a = sin_a * sin_a
    cos_pow_a = cos_a * cos_a
    x = sin_pow_a + cos_pow_a

    print(
        f'{get_text_color("a =", COLOR_GREEN)} π/5 = {math.pi}/5 = {get_text_color(a, COLOR_GREEN)}\n'
        f'{get_text_color("x =", COLOR_GREEN)} Sin^2(a) + Cos(a)^2 = Sin^2({a}) + Cos({a})^2 = {sin_pow_a} + {cos_pow_a} = {get_text_color(x, COLOR_GREEN)}\n'
    )

    y = None
    if x >= 1:
        y = cmath.sqrt(-1)
        print(f'Т.к {x} >= 1 => y = √-1 = {get_text_color(y, COLOR_GREEN)}')
    elif x < 1:
        ex = math.exp(x)
        y = math.cos(ex - 1)^ex
        print(f'Т.к {x} < 1 => y = Cos(e^x - 1)^e^x = Cos(e^{x} - 1)^e^{x} = {get_text_color(y, COLOR_GREEN)}')

    if y is None:
        print(
            f'{get_text_color(f"Ошибка Т.к x = {x} не подходит ни под одно условие задачи!", COLOR_FAIL)}'
        )
        return

    f = y + 5.6
    print(
        f'{get_text_color("F =", COLOR_GREEN)} y+5.6 = {y}+5.6 = {get_text_color(f, COLOR_GREEN)}\n'
    )
    