from helpers import get_text_color, input_number, is_question, COLOR_GREEN, COLOR_FAIL, COLOR_WARNING
_DEFAULT_STEP = 0.1
_MIN_STEP = 0.1
_MAX_STEP = 1

_MIN_START_X = -10
_MAX_START_X = -2
_DEFAULT_START_X = -2

_MIN_END_X = 2
_MAX_END_X = 20
_DEFAULT_END_X = -2

def init():
    _example = (
        f'     | x * 0.5,    если x < -1\n'
        f'y = <  0      ,    если x >= -1\n'
        f'     | x      ,    если x >= 1\n'
        f'     | 1      ,    если x > 1\n'
    )
    print(
        f'{get_text_color("По заданному графику функции вычислить ее значение", COLOR_WARNING)}\n'
        f'{get_text_color(_example, COLOR_GREEN)}\n'        
    )

    step = input_number(
        text=f'Введите шаг: (по умолчанию {_DEFAULT_STEP})', 
        default=_DEFAULT_STEP,
        min=_MIN_STEP,
        max=_MAX_STEP
    )

    start_x = input_number(
        text=f'Введите начальное значение x: (по умолчанию {_DEFAULT_START_X})', 
        default=_DEFAULT_START_X,
        min=_MIN_START_X,
        max=_MAX_START_X
    )

    end_x = input_number(
        text=f'Введите конечное значение x: (по умолчанию {_DEFAULT_END_X})', 
        default=_DEFAULT_END_X,
        min=_MIN_END_X,
        max=_MAX_END_X
    )
