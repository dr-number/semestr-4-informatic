from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

_DEFAULT_PB = 15625
_DEFAULT_PFE = 2255
_DEFAULT_PF = 121
_DEFAULT_PK = 47
_DEFAULT_EN = 11858
_DEFAULT_VN = 154
_DEFAULT_F1 = 1250
_MIN_VALUE = 1
_MAX_VALUE = 9999999999

def init():
    print(
        f'Вычислить уровень расчетной рентабельности по формуле: {get_text_color("Kpp = P/T", COLOR_GREEN)} где\n'
        f'{get_text_color("P = Pб - Pfe - Pf - Pk", COLOR_GREEN)};\n'
        f'{get_text_color("T = F1 + En + Vn", COLOR_GREEN)}\n\n'
        f'{get_text_color("Pб", COLOR_GREEN)} - балансовая прибыль;\n'
        f'{get_text_color("Pfe", COLOR_GREEN)} - плата за фонды;\n'
        f'{get_text_color("Pf", COLOR_GREEN)} - финансируемые платежи;\n'
        f'{get_text_color("Pk", COLOR_GREEN)} - процент за кредит;\n'
        f'{get_text_color("F1", COLOR_GREEN)} - средняя стоимость основных фондов;\n'
        f'{get_text_color("En", COLOR_GREEN)} - нормируемые оборотные средства;\n'
        f'{get_text_color("Vn", COLOR_GREEN)} - сверхплановые запасы неустановленного оборудования.\n\n'
    )
    
    pb = input_number(
        text=f'Введите балансовую прибыль [Pб]: (по умолчанию {_DEFAULT_PB})', 
        default_value=_DEFAULT_PB,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    pfe = input_number(
        text=f'Введите плату за фонды [Pfe]: (по умолчанию {_DEFAULT_PFE})', 
        default_value=_DEFAULT_PFE,
    )
    pf = input_number(
        text=f'Введите финансируемые платежи [Pf]: (по умолчанию {_DEFAULT_PF})', 
        default_value=_DEFAULT_PF,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    pk = input_number(
        text=f'Введите процент за кредит [Pk]: (по умолчанию {_DEFAULT_PK})', 
        default_value=_DEFAULT_PK,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    
    f1 = input_number(
        text=f'Введите среднюю стоимость основных фондов [F1]: (по умолчанию {_DEFAULT_F1})', 
        default_value=_DEFAULT_F1,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    en = input_number(
        text=f'Введите нормируемые оборотные средства [En]: (по умолчанию {_DEFAULT_EN})', 
        default_value=_DEFAULT_EN,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    vn = input_number(
        text=f'Введите сверхплановые запасы неустановленного оборудования [Vn]: (по умолчанию {_DEFAULT_VN})',
        default_value=_DEFAULT_VN,
        min=_MIN_VALUE,
        max=_MAX_VALUE
    )
    
    print(
        f'\n{get_text_color("Исходные данные:", COLOR_WARNING)}\n'
        f'{get_text_color("Pб", COLOR_GREEN)} - балансовая прибыль = {get_text_color(pb, COLOR_GREEN)};\n'
        f'{get_text_color("Pfe", COLOR_GREEN)} - плата за фонды = {get_text_color(pfe, COLOR_GREEN)};\n'
        f'{get_text_color("Pf", COLOR_GREEN)} - финансируемые платежи = {get_text_color(pf, COLOR_GREEN)};\n'
        f'{get_text_color("Pk", COLOR_GREEN)} - процент за кредит = {get_text_color(pk, COLOR_GREEN)};\n'
        f'{get_text_color("F1", COLOR_GREEN)} - средняя стоимость основных фондов = {get_text_color(f1, COLOR_GREEN)};\n'
        f'{get_text_color("En", COLOR_GREEN)} - нормируемые оборотные средства = {get_text_color(en, COLOR_GREEN)};\n'
        f'{get_text_color("Vn", COLOR_GREEN)} - сверхплановые запасы неустановленного оборудования = {get_text_color(vn, COLOR_GREEN)}.\n\n'
    )
    
    t = f1 + en + vn
    p = pb - pfe - pf - pk
    
    print(
        f'{get_text_color("T = F1 + En + Vn", COLOR_GREEN)}\n'
        f'T = {f1} + {en} + {vn}\n'
        f'{get_text_color(f"T = {t}", COLOR_GREEN)}\n'
    )
    
    print(
        f'{get_text_color("P = Pб - Pfe - Pf - Pk", COLOR_GREEN)}\n'
        f'P = {pb} - {pfe} - {pf} - {pk}\n'
        f'{get_text_color(f"P = {p}", COLOR_GREEN)}\n\n'
    )
    
    if t == 0:
        print(
            f'{get_text_color("Ошибка Т.к T = 0 дальнейшие вычисления невозможны!", COLOR_FAIL)}'
        )
        return
    
    print(
        f'{get_text_color("Итоговый результат вычислений:", COLOR_GREEN)}\n'
        'Kpp = P / T\n'
        f'Kpp = {p} / {t}\n'
        f'Kpp = {get_text_color(p/t, COLOR_GREEN)}\n\n'
    )
    