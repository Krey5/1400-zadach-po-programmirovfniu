n = int(input("Натуральное число (>999): "))
hundreds = (n // 100) % 10
thousands = n // 1000
print("Сотни:", hundreds, "Тысячи:", thousands)
