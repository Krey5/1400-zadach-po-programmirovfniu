import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = (x + (2 + y)/(x**2)) / (y + 1/((x**2 + 10)**0.5))
q = 7.25 * math.sin(x) - abs(y)

print(z)
print(q)
