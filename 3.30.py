n = int(input("Натуральное число (>99): "))
tens = (n // 10) % 10
hundreds = n // 100
print("Десятки:", tens, "Сотни:", hundreds)
