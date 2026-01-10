birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения: "))
current_year = int(input("Текущий год: "))
current_month = int(input("Текущий месяц: "))

age = current_year - birth_year
if current_month < birth_month:
    age -= 1
print("Возраст:", age, "лет")
