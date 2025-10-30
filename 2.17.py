a = float(input("Введите большее основание: "))
b = float(input("Введите меньшее основание: "))
h = float(input("Введите высоту: "))
side = ((a - b)/2)**2 + h**2
side = side**0.5
P = a + b + 2 * side
print(P)
