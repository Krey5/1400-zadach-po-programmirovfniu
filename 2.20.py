import math

e = float(input("Введите значение e: "))
f = float(input("Введите значение f: "))
g = float(input("Введите значение g: "))
h = float(input("Введите значение h: "))

a = math.sqrt(e - 3/f) + g

b = math.sin(e) + math.cos(h)**2

c = (33 * g) / (e * f - 3)

print(a)
print(b)
print(c)
