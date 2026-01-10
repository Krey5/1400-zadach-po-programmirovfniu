import math
circle_area = float(input("Площадь круга: "))
square_area = float(input("Площадь квадрата: "))

circle_radius = math.sqrt(circle_area / math.pi)
square_side = math.sqrt(square_area)

# Круг в квадрате: диаметр круга <= стороне квадрата
if 2 * circle_radius <= square_side:
    print("Круг уместится в квадрате")
else:
    print("Круг не уместится в квадрате")

# Квадрат в круге: диагональ квадрата <= диаметру круга
if square_side * math.sqrt(2) <= 2 * circle_radius:
    print("Квадрат уместится в круге")
else:
    print("Квадрат не уместится в круге")
