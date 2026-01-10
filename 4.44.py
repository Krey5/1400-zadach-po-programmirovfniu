x = float(input("Введите x: "))
y = float(input("Введите y: "))

if (x >= 0 and y >= 0) or (x <= -1 and y <= -1):
    print("Точка попадает в область I или III")
else:
    print("Точка не попадает в область I или III")
