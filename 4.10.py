km = float(input("Расстояние в км: "))
feet = float(input("Расстояние в футах: "))

km_to_m = km * 1000
feet_to_m = feet * 0.3048

if km_to_m < feet_to_m:
    print("Расстояние в км меньше")
else:
    print("Расстояние в футах меньше")
