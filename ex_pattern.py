import sys

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
    print(get_text_color("\nЛарионов гр. 210з. Информатика. Индивидуальное задание № 2. Вариант 14.\n", WARNING))

    if input('Для выхода введите \'0\'\nДля продолжения нажмите любую другую клавишу...\n') == '0':
        break
    