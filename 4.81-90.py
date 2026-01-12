# 4.81
import math
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a + b > c and a + c > b and b + c > a:
    sides = sorted([a, b, c])
    cos_max = (sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1])
    if math.isclose(cos_max, 0):
        print("Прямоугольный")
    elif cos_max > 0:
        print("Остроугольный")
    else:
        print("Тупоугольный")
    
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Треугольник не существует")



# 4.82
n = int(input("Возраст (1-99): "))
if 11 <= n <= 14:
    suffix = "лет"
elif n % 10 == 1:
    suffix = "год"
elif 2 <= n % 10 <= 4:
    suffix = "года"
else:
    suffix = "лет"
print(f"мне {n} {suffix}")






# 4.83
k = int(input("Количество грибов: "))
if k % 10 == 1 and k % 100 != 11:
    word = "гриб"
elif 2 <= k % 10 <= 4 and not (12 <= k % 100 <= 14):
    word = "гриба"
else:
    word = "грибов"
print(f"мы нашли {k} {word} в лесу")




# 4.84
n = int(input("Стоимость в копейках (1-9999): "))
rub = n // 100
kop = n % 100
rub_str = ""
kop_str = ""

if rub % 10 == 1 and rub % 100 != 11:
    rub_str = "рубль"
elif 2 <= rub % 10 <= 4 and not (12 <= rub % 100 <= 14):
    rub_str = "рубля"
else:
    rub_str = "рублей"

if kop % 10 == 1 and kop % 100 != 11:
    kop_str = "копейка"
elif 2 <= kop % 10 <= 4 and not (12 <= kop % 100 <= 14):
    kop_str = "копейки"
else:
    kop_str = "копеек"

print(f"{rub} {rub_str} {kop} {kop_str}")





# 4.85
n = int(input("Возраст в месяцах (1-1188): "))
years = n // 12
months = n % 12
year_str = ""
month_str = ""

if years % 10 == 1 and years % 100 != 11:
    year_str = "год"
elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
    year_str = "года"
else:
    year_str = "лет"

if months == 1:
    month_str = "месяц"
elif 2 <= months <= 4:
    month_str = "месяца"
else:
    month_str = "месяцев"

print(f"{years} {year_str} {months} {month_str}")






# 4.86
from datetime import date

birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения: "))
birth_day = int(input("День рождения: "))
today_year = int(input("Текущий год: "))
today_month = int(input("Текущий месяц: "))
today_day = int(input("Текущий день: "))

age = today_year - birth_year
if (today_month, today_day) < (birth_month, birth_day):
    age -= 1
print(f"Возраст: {age} полных лет")





# 4.87
y1 = int(input("Год рождения первого: "))
m1 = int(input("Месяц рождения первого: "))
d1 = int(input("День рождения первого: "))
y2 = int(input("Год рождения второго: "))
m2 = int(input("Месяц рождения второго: "))
d2 = int(input("День рождения второго: "))

if (y1, m1, d1) < (y2, m2, d2):
    print("Первый старше")
else:
    print("Второй старше")




# 4.88
birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения: "))
curr_year = int(input("Текущий год: "))
curr_month = int(input("Текущий месяц: "))

full_years = curr_year - birth_year
full_months = curr_month - birth_month
if full_months < 0:
    full_years -= 1
    full_months += 12
print(f"Возраст: {full_years} лет {full_months} месяцев")





# 4.89
a = int(input("Час прибытия: "))
b = int(input("Минута прибытия: "))
c = int(input("Час отправления: "))
d = int(input("Минута отправления: "))
n = int(input("Час прихода пассажира: "))
m = int(input("Минута прихода пассажира: "))

arrival = a * 60 + b
departure = c * 60 + d
passenger = n * 60 + m

if arrival <= passenger <= departure:
    print("Поезд будет стоять на платформе")
else:
    print("Поезда не будет на платформе")





# 4.90
m = int(input("Месяц: "))
n = int(input("День: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# a) Предыдущий день
if n > 1:
    prev_day = n - 1
    prev_month = m
else:
    prev_month = m - 1
    prev_day = days_in_month[prev_month - 1]
print(f"Предыдущий день: {prev_day}.{prev_month}")

# б) Следующий день
if n < days_in_month[m - 1]:
    next_day = n + 1
    next_month = m
else:
    next_month = m + 1
    next_day = 1
print(f"Следующий день: {next_day}.{next_month}")
