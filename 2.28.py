import math

a = float(input("Введите большее основание трапеции: "))
b = float(input("Введите меньшее основание трапеции: "))
ugol = float(input("Введите угол при большем основании (в градусах): "))

radian = math.radians(ugol)

h = ((a - b) / 2) * math.tan(radian)

S = (a + b) / 2 * h

print(S)
