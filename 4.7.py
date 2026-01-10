import math
x = float(input("Введите x: "))

if math.sin(x) < 0:
    k = x ** 2
else:
    k = abs(x)

if k < x:
    f = k * x
else:
    f = k + x

print("f =", f)
