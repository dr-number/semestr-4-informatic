from helpers import get_text_color, COLOR_WARNING
import ex_1

_EX_1 = '1'
_EX_2 = '2'

while True:
    print(
        "\nЛарионов гр. 210з. Информатика.\n"
        "Какую задачу выполнить: \n"
        f"{get_text_color(f'{_EX_1}) Вычислить уровень расчетной рентабельности', COLOR_WARNING)}"
    )
    select = input('Для выхода введите \'0\'\n')

    if select == _EX_1:
        ex_1.init()
    elif select == '0':
        break
