import math

def square(side):
    """Вычисляет площадь квадрата и округляет результат вверх, если необходимо."""
    area = side * side
    return math.ceil(area)  # Округляем вверх
print(square(3))
print(3*3)
print(square(1.1))
print(1.1*1.1)