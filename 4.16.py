import math
a = float(input("a (не 0): "))
b = float(input("b: "))
c = float(input("c: "))

D = b ** 2 - 4 * a * c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Корни:", x1, x2)
else:
    print("Вещественных корней нет")
