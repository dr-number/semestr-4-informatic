from helpers import get_text_color, input_number, is_question, COLOR_GREEN, COLOR_FAIL, COLOR_WARNING
class Point:
    x: float
    y: float
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
    def get_info(self):
        return f'({self.x}; {self.y})'

    def change(self, prefix: str):
        self.x = input_number(f"{prefix}. Введите координату х:")
        self.y = input_number(f"{prefix}. Введите координату y:")
        
class Sqare:
    point_start: Point
    point_end: Point
    def __init__(self, point_start: Point, point_end: Point):
        self.point_start = point_start
        self.point_end = point_end

    def get_info(self):
        return (
            f'start: {self.point_start.get_info()}\n'
            f'end:   {self.point_end.get_info()}\n'
        )
    
    def change(self):
        self.point_start.change("Начальная точка")
        self.point_end.change("Конечная точка")

_DEFAULT_COORDINATES_SQUARE = Sqare(
    point_start=Point(x=-1, y=1),
    point_end=Point(x=1, y=-1)
)
def init():
    _default_square = _DEFAULT_COORDINATES_SQUARE
    print(
        f'{get_text_color("Определить, лежит ли точка с координатами (x,y) внутри квадрата", COLOR_WARNING)}\n'
        f'Исходный квадрат:\n{get_text_color(_default_square.get_info(), COLOR_GREEN)}\n'
    )

    if is_question("Хотите изменить исходный квадрат?"):
        _default_square.change()

    point = Point()
    point.change("Точка внутри квадрата")

    print(
        f'{get_text_color("Исходные данные", COLOR_WARNING)}\n\n'
        f'Квадрат:\n{get_text_color(_default_square.get_info(), COLOR_GREEN)}'
        f'Точка: {get_text_color(point.get_info(), COLOR_WARNING)}\n'
    )
