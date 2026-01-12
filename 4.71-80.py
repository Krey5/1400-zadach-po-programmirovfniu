# 4.71
import math
g = 9.8
alpha = float(input("Угол α (радианы): "))
v0 = float(input("Начальная скорость v0: "))
P = float(input("Высота цели P: "))
R = float(input("Расстояние R: "))
H = float(input("Высота цели H: "))

# Время полета до цели по горизонтали
t = R / (v0 * math.cos(alpha))
# Высота снаряда в этот момент
y = v0 * t * math.sin(alpha) - g * t**2 / 2

if H <= y <= H + P:
    print("Снаряд поразит цель")
else:
    print("Снаряд не поразит цель")



# 4.72
x1 = float(input("x левого нижнего угла первого: "))
y1 = float(input("y левого нижнего угла первого: "))
w1 = float(input("Ширина первого: "))
h1 = float(input("Высота первого: "))
x2 = float(input("x левого нижнего угла второго: "))
y2 = float(input("y левого нижнего угла второго: "))
w2 = float(input("Ширина второго: "))
h2 = float(input("Высота второго: "))

# Проверка принадлежности всех точек первого прямоугольника второму
if x1 >= x2 and y1 >= y2 and x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2:
    print("Первый прямоугольник полностью внутри второго")
else:
    print("Первый прямоугольник не полностью внутри второго")

# Проверка принадлежности одного прямоугольника другому
if (x1 >= x2 and y1 >= y2 and x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2) or \
   (x2 >= x1 and y2 >= y1 and x2 + w2 <= x1 + w1 and y2 + h2 <= y1 + h1):
    print("Один прямоугольник полностью внутри другого")
else:
    print("Нет полного вложения")

# Проверка пересечения
if (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2):
    print("Прямоугольники пересекаются")
else:
    print("Прямоугольники не пересекаются")



# 4.73
a2 = int(input("Десятки двузначного: "))
a1 = int(input("Единицы двузначного: "))
b = int(input("Однозначное число: "))

# Вычитание: (a2 a1) - b, результат двузначный
if a1 >= b:
    diff_units = a1 - b
    diff_tens = a2
else:
    diff_units = a1 + 10 - b
    diff_tens = a2 - 1

print("Цифры разности (десятки, единицы):", diff_tens, diff_units)



# 4.74
a2 = int(input("Десятки первого: "))
a1 = int(input("Единицы первого: "))
b2 = int(input("Десятки второго: "))
b1 = int(input("Единицы второго: "))

# Вычитание: (a2 a1) - (b2 b1), результат двузначный
if a1 >= b1:
    diff_units = a1 - b1
    borrow = 0
else:
    diff_units = a1 + 10 - b1
    borrow = 1

diff_tens = a2 - b2 - borrow

print("Цифры разности (десятки, единицы):", diff_tens, diff_units)



# 4.75
a3 = int(input("Сотни трехзначного: "))
a2 = int(input("Десятки трехзначного: "))
a1 = int(input("Единицы трехзначного: "))
b2 = int(input("Десятки двузначного: "))
b1 = int(input("Единицы двузначного: "))

# Вычитание: (a3 a2 a1) - (b2 b1), результат трехзначный
if a1 >= b1:
    diff_units = a1 - b1
    borrow1 = 0
else:
    diff_units = a1 + 10 - b1
    borrow1 = 1

temp_tens = a2 - borrow1
if temp_tens >= b2:
    diff_tens = temp_tens - b2
    borrow2 = 0
else:
    diff_tens = temp_tens + 10 - b2
    borrow2 = 1

diff_hundreds = a3 - borrow2

print("Цифры разности (сотни, десятки, единицы):", diff_hundreds, diff_tens, diff_units)





# 4.76
a = int(input("a (вертикаль): "))
b = int(input("b (горизонталь): "))
c = int(input("c (вертикаль цели): "))
d = int(input("d (горизонталь цели): "))

# a) Ладья
if a == c or b == d:
    print("Ладья угрожает полю")
else:
    print("Ладья не угрожает полю")

# б) Слон
if abs(a - c) == abs(b - d):
    print("Слон угрожает полю")
else:
    print("Слон не угрожает полю")

# в) Король
if abs(a - c) <= 1 and abs(b - d) <= 1:
    print("Король может попасть на поле за один ход")
else:
    print("Король не может попасть на поле за один ход")

# г) Ферзь
if a == c or b == d or abs(a - c) == abs(b - d):
    print("Ферзь угрожает полю")
else:
    print("Ферзь не угрожает полю")

# д) Белая пешка
if a == c and d - b == 1:
    print("Белая пешка может сделать обычный ход")
elif abs(a - c) == 1 and d - b == 1:
    print("Белая пешка может взять фигуру")
else:
    print("Белая пешка не может сделать ход")

# е) Черная пешка
if a == c and b - d == 1:
    print("Черная пешка может сделать обычный ход")
elif abs(a - c) == 1 and b - d == 1:
    print("Черная пешка может взять фигуру")
else:
    print("Черная пешка не может сделать ход")

# ж) Конь
if (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2):
    print("Конь угрожает полю")
else:
    print("Конь не угрожает полю")




# 4.77
a = int(input("a (вертикаль белой): "))
b = int(input("b (горизонталь белой): "))
c = int(input("c (вертикаль черной): "))
d = int(input("d (горизонталь черной): "))
e = int(input("e (вертикаль цели): "))
f = int(input("f (горизонталь цели): "))

# Проверка, может ли белая фигура пойти на (e, f) без попадания под удар черной
def under_attack(x1, y1, x2, y2, piece):
    if piece == "ладья":
        return x1 == x2 or y1 == y2
    elif piece == "слон":
        return abs(x1 - x2) == abs(y1 - y2)
    elif piece == "ферзь":
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    elif piece == "конь":
        return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
    elif piece == "король":
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    return False

# Пример для комбинации "ладья и ладья"
white_piece = "ладья"
black_piece = "ладья"

# Может ли белая фигура пойти на (e, f)?
if under_attack(a, b, e, f, white_piece):
    # Оказалась ли бы она под ударом черной фигуры?
    if under_attack(c, d, e, f, black_piece):
        print("Белая фигура попадет под удар")
    else:
        print("Белая фигура может пойти безопасно")
else:
    print("Белая фигура не может пойти на это поле")




# 4.78
a = int(input("a (вертикаль): "))
b = int(input("b (горизонталь): "))
c = int(input("c (вертикаль цели): "))
d = int(input("d (горизонталь цели): "))

if (a + b) % 2 == (c + d) % 2:
    print("Поля одного цвета")
else:
    print("Поля разных цветов")




# 4.79
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")





# 4.80
import math
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a + b > c and a + c > b and b + c > a:
    sides = sorted([a, b, c])
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не прямоугольный")
else:
    print("Треугольник не существует")
