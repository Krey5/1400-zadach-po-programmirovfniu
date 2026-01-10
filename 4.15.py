a = float(input("a (не 0): "))
b = float(input("b: "))
c = float(input("c: "))

D = b ** 2 - 4 * a * c

if D >= 0:
    print("Уравнение имеет вещественные корни")
else:
    print("Уравнение не имеет вещественных корней")
