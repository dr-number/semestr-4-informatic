import sys

DEFAULT_PB = 15625
DEFAULT_PFE = 2255
DEFAULT_PF = 121
DEFAULT_PK = 47
DEFAULT_EN = 11858
DEFAULT_VN = 154
DEFAULT_F1 = 1250

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False
        
def input_number(text: str, default_value: float)-> float:
    while True:
        number = input(f'{get_text_color(text, WARNING)} ')
        if number == '':
            return default_value
        elif is_number(number):
            return float(number)
            
        return 0.0


while True:
    print(get_text_color("\nЛарионов гр. 210з. Информатика. Индивидуальное задание № 1. Вариант 14.\n", WARNING))
    print(
        f'Вычислить уровень расчетной рентабельности по формуле: {get_text_color("Kpp = P/T", GREEN)} где\n'
        f'{get_text_color("P = Pб - Pfe - Pf - Pk", GREEN)};\n'
        f'{get_text_color("T = F1 + En + Vn", GREEN)}\n\n'
        f'{get_text_color("Pб", GREEN)} - балансовая прибыль;\n'
        f'{get_text_color("Pfe", GREEN)} - плата за фонды;\n'
        f'{get_text_color("Pf", GREEN)} - финансируемые платежи;\n'
        f'{get_text_color("Pk", GREEN)} - процент за кредит;\n'
        f'{get_text_color("F1", GREEN)} - средняя стоимость основных фондов;\n'
        f'{get_text_color("En", GREEN)} - нормируемые оборотные средства;\n'
        f'{get_text_color("Vn", GREEN)} - сверхплановые запасы неустановленного оборудования.\n\n'
    )
    
    pb = input_number(f'Введите балансовую прибыль: (по умолчанию {DEFAULT_PB})', DEFAULT_PB)
    pfe = input_number(f'Введите плату за фонды: (по умолчанию {DEFAULT_PFE})', DEFAULT_PFE)
    pf = input_number(f'Введите финансируемые платежи: (по умолчанию {DEFAULT_PF})', DEFAULT_PF)
    pk = input_number(f'Введите процент за кредит: (по умолчанию {DEFAULT_PK})', DEFAULT_PK)
    
    f1 = input_number(f'Введите среднюю стоимость основных фондов: (по умолчанию {DEFAULT_F1})', DEFAULT_F1)
    en = input_number(f'Введите нормируемые оборотные средства: (по умолчанию {DEFAULT_EN})', DEFAULT_EN)
    vn = input_number(f'Введите сверхплановые запасы неустановленного оборудования: (по умолчанию {DEFAULT_VN})', DEFAULT_VN)
    
    print(
        f'\n{get_text_color("Исходные данные:", WARNING)}\n'
        f'{get_text_color("Pб", GREEN)} - балансовая прибыль = {get_text_color(pb, GREEN)};\n'
        f'{get_text_color("Pfe", GREEN)} - плата за фонды = {get_text_color(pfe, GREEN)};\n'
        f'{get_text_color("Pf", GREEN)} - финансируемые платежи = {get_text_color(pf, GREEN)};\n'
        f'{get_text_color("Pk", GREEN)} - процент за кредит = {get_text_color(pk, GREEN)};\n'
        f'{get_text_color("F1", GREEN)} - средняя стоимость основных фондов = {get_text_color(f1, GREEN)};\n'
        f'{get_text_color("En", GREEN)} - нормируемые оборотные средства = {get_text_color(en, GREEN)};\n'
        f'{get_text_color("Vn", GREEN)} - сверхплановые запасы неустановленного оборудования = {get_text_color(vn, GREEN)}.\n\n'
    )
    
    t = f1 + en + vn
    p = pb - pfe - pf - pk
    
    print(
        f'{get_text_color("T = F1 + En + Vn", GREEN)}\n'
        f'T = {f1} + {en} + {vn}\n'
        f'{get_text_color(f"T = {t}", GREEN)}\n'
    )
    
    print(
        f'{get_text_color("P = Pб - Pfe - Pf - Pk", GREEN)}\n'
        f'P = {pb} - {pfe} - {pf} - {pk}\n'
        f'{get_text_color(f"P = {p}", GREEN)}\n\n'
    )
    
    if t == 0:
        print(f'{get_text_color("Ошибка Т.к T = 0 дальнейшие вычисления невозможны!", FAIL)}')
        continue
    
    print(
        f'{get_text_color("Итоговый результат вычислений:", GREEN)}\n'
        'Kpp = P / T\n'
        f'Kpp = {p} / {t}\n'
        f'Kpp = {get_text_color(p/t, GREEN)}\n\n'
    )

    if input('Для выхода введите \'0\'\nДля продолжения нажмите любую другую клавишу...\n') == '0':
        break
    