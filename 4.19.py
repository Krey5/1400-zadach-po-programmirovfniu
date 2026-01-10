import math
circle_area = float(input("Площадь круга: "))
triangle_area = float(input("Площадь равностороннего треугольника: "))

circle_radius = math.sqrt(circle_area / math.pi)
triangle_side = math.sqrt(4 * triangle_area / math.sqrt(3))

# Круг в треугольнике: радиус вписанной окружности <= радиусу круга
inscribed_radius = triangle_side * math.sqrt(3) / 6
if circle_radius <= inscribed_radius:
    print("Круг уместится в треугольнике")
else:
    print("Круг не уместится в треугольнике")

# Треугольник в круге: радиус описанной окружности >= радиусу круга
circumscribed_radius = triangle_side * math.sqrt(3) / 3
if circumscribed_radius <= circle_radius:
    print("Треугольник уместится в круге")
else:
    print("Треугольник не уместится в круге")
