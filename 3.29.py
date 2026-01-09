n = int(input("Натуральное число (>9): "))
units = n % 10
tens = (n // 10) % 10
print("Единицы:", units, "Десятки:", tens)
