n = int(input("Прошло месяцев (с 1990): "))
month = (n + 1) % 12
if month == 0:
    month = 12
print(month)
