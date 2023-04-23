from helpers import get_text_color, COLOR_WARNING, COLOR_FAIL
import ex_1, ex_2

_EX_1 = '1'
_EX_2 = '2'

def main():
    while True:
        print(
            "\nЛарионов гр. 210з. Информатика. Индивидуальное задание № 1. Вариант 14.\n"
            "Какую задачу выполнить: \n"
            f"{get_text_color(f'{_EX_1}) Вычислить уровень расчетной рентабельности', COLOR_WARNING)}"
        )
        select = input('Для выхода введите \'0\'\n')

        if select == _EX_1:
            ex_1.init()
        elif select == _EX_2:
            ex_2.init()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()
