from helpers import get_text_color, input_number, COLOR_OKBLUE, COLOR_GREEN, COLOR_OKCYAN, COLOR_FAIL, COLOR_WARNING
_FORMAT = '| {:10} | {:30} | {:60} | {:35} | {:30} |'

_DEFAULT_STEP = 0.2
_MIN_STEP = 0.1
_MAX_STEP = 1

_MIN_START_X = -10
_MAX_START_X = -2
_DEFAULT_START_X = -3

_MIN_END_X = 2
_MAX_END_X = 20
_DEFAULT_END_X = 3

def init():
    _example = (
        f'     | x * 0.5,    если x < -1\n'
        f'y = <  0      ,    если x >= -1\n'
        f'     | x      ,    если x <= 1\n'
        f'     | 1      ,    если x > 1\n'
    )
    print(
        f'{get_text_color("По заданному графику функции вычислить ее значение", COLOR_WARNING)}\n'
        f'{get_text_color(_example, COLOR_GREEN)}\n'        
    )

    step_x = input_number(
        text=f'Введите шаг: (по умолчанию {_DEFAULT_STEP})', 
        default_value=_DEFAULT_STEP,
        min=_MIN_STEP,
        max=_MAX_STEP
    )

    start_x = input_number(
        text=f'Введите начальное значение x: (по умолчанию {_DEFAULT_START_X})', 
        default_value=_DEFAULT_START_X,
        min=_MIN_START_X,
        max=_MAX_START_X
    )

    end_x = input_number(
        text=f'Введите конечное значение x: (по умолчанию {_DEFAULT_END_X})', 
        default_value=_DEFAULT_END_X,
        min=_MIN_END_X,
        max=_MAX_END_X
    )

    print(_FORMAT.format(*[
        '№',
        'x',
        'Выбор', 
        'Формула', 
        'результат'
    ]))

    x = start_x
    i = 1
    while start_x <= x <= end_x:

        if x < -1:
            select = f'Т.к. x < -1 -> {x} < -1 -> y = x * 0.5'
            formul = f'{x} * 0.5'
            result = x * 0.5
            color = COLOR_OKCYAN
        elif x >= -1:
            select = f'Т.к. x >= -1 -> {x} >= -1 -> y = 0'
            formul = '0'
            result = '0'
            color = COLOR_OKBLUE
        elif x <= 1:
            select = f'Т.к. x <= 1 -> {x} <= 1 -> y = x'
            formul = f'x'
            result = f'{x}'
            color = COLOR_WARNING
        elif x > 1:
            select = f'Т.к. x > 1 -> {x} > 1 -> y = 1'
            formul = f'1'
            result = f'1'
            color = COLOR_GREEN
        else:
            select = ''
            formul = 'Не подходит под условие задачи!'
            result = ''
            color = COLOR_FAIL

        print(get_text_color(_FORMAT.format(*[
            f'{i}',
            f'{x}',
            select, 
            formul, 
            result
        ]), color))

        x += step_x
        i += 1
    
    print(f'Количество вычислений: {get_text_color(str(i - 1), COLOR_GREEN)}')
