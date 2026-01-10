a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

maximum = a if a > b else b
minimum = a if a < b else b

print("Максимум:", maximum)
print("Минимум:", minimum)
