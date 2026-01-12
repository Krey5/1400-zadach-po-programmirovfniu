# 4.91
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




# 4.92
t = float(input("Время с начала часа (минуты): "))
cycle = t % 6  # цикл: 3 зеленый, 1 желтый, 2 красный
if cycle < 3:
    print("Горит зеленый")
elif cycle < 4:
    print("Горит желтый")
else:
    print("Горит красный")





# 4.93
k = int(input("День года (1-365): "))
d = int(input("День недели 1 января (1-7): "))
day_of_week = (k + d - 2) % 7 + 1
if day_of_week == 6:
    print("Суббота")
elif day_of_week == 7:
    print("Воскресенье")
else:
    print("Рабочий день")





# 4.94
k = int(input("k (1-180): "))
# Последовательность 10 11 12 ... 99
pair = (k + 1) // 2
digit_in_pair = 2 - (k % 2) if k % 2 != 0 else 2
number = 9 + pair
digit = number // 10 if digit_in_pair == 1 else number % 10
print(f"{k}-я цифра: {digit}")





# 4.95
n = int(input("n (1-32): "))
seq = "0" + "".join(str(i) for i in range(1, 21))
print(f"{n}-я цифра: {seq[n-1]}")



# 4.96
k = int(input("k (1-252): "))
seq = "".join(str(i) for i in range(50, 251))
print(f"{k}-я цифра: {seq[k-1]}")





# 4.97
k = int(input("k (1-222): "))
seq = "".join(str(i) for i in range(1, 111))
print(f"{k}-я цифра: {seq[k-1]}")


# 4.98
n = int(input("Количество квартир: "))
a = int(input("Начальный номер квартиры: "))
sum_numbers = n * (2*a + n - 1) // 2
if sum_numbers % 2 == 0:
    print("Сумма номеров четная")
else:
    print("Сумма номеров нечетная")
