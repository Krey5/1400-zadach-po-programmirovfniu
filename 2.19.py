import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))

x = (2/(a**2 + 25) + b) / ((b + (a + b)/2)**0.5)
y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)

print(x)
print(y)
