# 4.131
a1 = float(input("Первое число первой тройки: "))
a2 = float(input("Второе число первой тройки: "))
a3 = float(input("Третье число первой тройки: "))
b1 = float(input("Первое число второй тройки: "))
b2 = float(input("Второе число второй тройки: "))
b3 = float(input("Третье число второй тройки: "))

def middle_of_three(x, y, z):
    if (y <= x <= z) or (z <= x <= y):
        return x
    elif (x <= y <= z) or (z <= y <= x):
        return y
    else:
        return z

middle1 = middle_of_three(a1, a2, a3)
middle2 = middle_of_three(b1, b2, b3)
average_middles = (middle1 + middle2) / 2
print("Среднее арифметическое средних чисел каждой тройки:", average_middles)




# 4.132
x = float(input("x (не 0): "))
y = float(input("y (не 0): "))

if x > 0 and y > 0:
    quarter = 1
elif x < 0 and y > 0:
    quarter = 2
elif x < 0 and y < 0:
    quarter = 3
else:
    quarter = 4
print("Номер четверти:", quarter)




# 4.133
day_num = int(input("Номер дня недели (1-7): "))
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(days[day_num - 1])



# 4.134
month_num = int(input("Номер месяца (1-12): "))
months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
print(months[month_num - 1])




# 4.135
month_num = int(input("Номер месяца (1-12): "))
if month_num in (12, 1, 2):
    season = "зима"
elif month_num in (3, 4, 5):
    season = "весна"
elif month_num in (6, 7, 8):
    season = "лето"
else:
    season = "осень"
print("Время года:", season)



# 4.136
month_num = int(input("Номер месяца (1-12): "))
is_leap = input("Год високосный? (да/нет): ").strip().lower() == "да"

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leap:
    days_in_month[1] = 29
print("Количество дней:", days_in_month[month_num - 1])



# 4.137
month_num = int(input("Номер месяца (1-12): "))
if month_num == 2:
    days = 28
elif month_num in (4, 6, 9, 11):
    days = 30
else:
    days = 31
print("Количество дней:", days)



# 4.138
m = int(input("Номер масти (1-4): "))
suits = {1: "пики", 2: "трефы", 3: "бубны", 4: "червы"}
print(suits[m])



# 4.139
k = int(input("Номер карты (6-14): "))
ranks = {6: "шестерка", 7: "семерка", 8: "восьмерка", 9: "девятка", 10: "десятка",
         11: "валет", 12: "дама", 13: "король", 14: "туз"}
print(ranks[k])



# 4.140
m = int(input("Номер масти (1-4): "))
k = int(input("Номер достоинства (6-14): "))

suits = {1: "пик", 2: "треф", 3: "бубен", 4: "червей"}
ranks = {6: "Шестерка", 7: "Семерка", 8: "Восьмерка", 9: "Девятка", 10: "Десятка",
         11: "Валет", 12: "Дама", 13: "Король", 14: "Туз"}

print(f"{ranks[k]} {suits[m]}")



# 4.141
k = int(input("День года (1-365): "))
d = int(input("День недели 1 января (1-7): "))
day_of_week = (k + d - 2) % 7
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(days[day_of_week])



# 4.142
n = int(input("Количество месяцев с 2010 года: "))
month_num = (n % 12) + 1
months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
print(months[month_num - 1])



# 4.143
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





# 4.144
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

g = int(input("Год: "))
m = int(input("Месяц: "))
n = int(input("День: "))
days_in_month = [31, 28 + is_leap(g), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# a) Предыдущий день
if n > 1:
    prev_day = n - 1
    prev_month = m
    prev_year = g
else:
    prev_month = m - 1
    if prev_month == 0:
        prev_month = 12
        prev_year = g - 1
    else:
        prev_year = g
    prev_day = days_in_month[prev_month - 1]
print(f"Предыдущий день: {prev_day}.{prev_month}.{prev_year}")

# б) Следующий день
if n < days_in_month[m - 1]:
    next_day = n + 1
    next_month = m
    next_year = g
else:
    next_month = m + 1
    if next_month == 13:
        next_month = 1
        next_year = g + 1
    else:
        next_year = g
    next_day = 1
print(f"Следующий день: {next_day}.{next_month}.{next_year}")
