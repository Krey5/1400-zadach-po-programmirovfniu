volume1 = float(input("Объем первого тела: "))
mass1 = float(input("Масса первого тела: "))
volume2 = float(input("Объем второго тела: "))
mass2 = float(input("Масса второго тела: "))

density1 = mass1 / volume1
density2 = mass2 / volume2

if density1 > density2:
    print("Плотность первого материала больше")
else:
    print("Плотность второго материала больше")
