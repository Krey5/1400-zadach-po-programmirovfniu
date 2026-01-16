# 7.61
count_short = 0
for i in range(12):
    height = float(input(f"Рост юноши {i+1}: "))
    if height < 165:
        count_short += 1
print("Юношей ниже 165 см:", count_short)




# 7.62
n = int(input("Сколько чисел? "))
p = int(input("Число p: "))
k = int(input("Число k: "))
count_gt_p = 0
count_ends_5 = 0
count_mult_k = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num > p:
        count_gt_p += 1
    if num % 10 == 5:
        count_ends_5 += 1
    if num % k == 0:
        count_mult_k += 1
print("Чисел > p:", count_gt_p)
print("Чисел оканчивается на 5:", count_ends_5)
print(f"Чисел кратно {k}:", count_mult_k)





# 7.63
count_5 = 0
count_2 = 0
n = int(input("Сколько учеников? "))
for i in range(n):
    grade = int(input(f"Оценка по химии ученика {i+1}: "))
    if grade == 5:
        count_5 += 1
    elif grade == 2:
        count_2 += 1
print("Пятерок:", count_5)
print("Двоек:", count_2)




# 7.64
before_1990 = 0
after_2000 = 0
n = int(input("Сколько людей? "))
for i in range(n):
    year = int(input(f"Год рождения человека {i+1}: "))
    if year < 1990:
        before_1990 += 1
    elif year > 2000:
        after_2000 += 1
print("Родились до 1990:", before_1990)
print("Родились после 2000:", after_2000)




# 7.65
count_better = 0
n = int(input("Сколько команд? "))
for i in range(n):
    wins = int(input(f"Побед команды {i+1}: "))
    losses = int(input(f"Поражений команды {i+1}: "))
    if wins > losses:
        count_better += 1
print("Команд с победами > поражений:", count_better)




# 7.66
count_negative = 0
while True:
    num = float(input("Введите число: "))
    if num >= 0:
        break
    count_negative += 1
print("Отрицательных чисел в начале:", count_negative)





# 7.67
count_before_zero = 0
while True:
    num = float(input("Введите число: "))
    if num == 0:
        break
    count_before_zero += 1
print("Чисел до первого нуля:", count_before_zero)





# 7.68
n = int(input("Сколько чисел? "))
first = int(input("Первое число: "))
count_equal = 1
for i in range(1, n):
    num = int(input(f"Число {i+1}: "))
    if num == first:
        count_equal += 1
    else:
        break
print("Одинаковых чисел в начале:", count_equal)





# 7.69
count_5 = 0
for i in range(20):
    grade = int(input(f"Оценка ученика {i+1}: "))
    if grade != 5:
        break
    count_5 += 1
print("Учеников с пятерками:", count_5)




# 7.70
days_no_rain = 0
for day in range(1, 32):
    rain = float(input(f"Осадки за {day} мая: "))
    if rain > 0:
        break
    days_no_rain += 1
print("Дней без осадков с начала мая:", days_no_rain)





# 7.71
count_2 = 0
n = int(input("Сколько студентов? "))
for i in range(n):
    grade1 = int(input(f"Оценка за первый экзамен студента {i+1}: "))
    grade2 = int(input(f"Оценка за второй экзамен студента {i+1}: "))
    if grade1 == 2 or grade2 == 2:
        count_2 += 1
print("Студентов с двойкой:", count_2)





# 7.72
n = int(input("Сколько чисел? "))
pos = 0
neg = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print("Положительных:", pos)
print("Отрицательных:", neg)





# 7.73
m = int(input("Сколько чисел? "))
count_3 = 0
count_7 = 0
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if num % 3 == 0:
        count_3 += 1
    if num % 7 == 0:
        count_7 += 1
print("Кратных 3:", count_3)
print("Кратных 7:", count_7)





# 7.74
n = int(input("Сколько троек? "))
count_valid = 0
for i in range(n):
    a = int(input(f"a тройки {i+1}: "))
    b = int(input(f"b тройки {i+1}: "))
    c = int(input(f"c тройки {i+1}: "))
    if a + b > c and a + c > b and b + c > a:
        count_valid += 1
print("Троек для треугольника:", count_valid)





# 7.75
import math
g = 9.8
n = int(input("Сколько выстрелов? "))
R = float(input("Расстояние до цели R: "))
H = float(input("Высота цели H: "))
P = float(input("Высота цели P: "))
hits = 0
for i in range(n):
    alpha = float(input(f"Угол выстрела {i+1} (радианы): "))
    v0 = float(input(f"Скорость выстрела {i+1}: "))
    t = R / (v0 * math.cos(alpha))
    y = v0 * t * math.sin(alpha) - g * t**2 / 2
    if H <= y <= H + P:
        hits += 1
print("Процент попаданий:", (hits / n) * 100, "%")





# 7.76
team1_penalties = 0
team2_penalties = 0
team1_time = 0
team2_time = 0
for i in range(24):
    team = int(input("Команда (1 или 2): "))
    time = int(input("Время удаления (2, 5, 10): "))
    if team == 1:
        team1_penalties += 1
        team1_time += time
    else:
        team2_penalties += 1
        team2_time += time
print("Команда 1: удалений", team1_penalties, "время", team1_time)
print("Команда 2: удалений", team2_penalties, "время", team2_time)





# 7.77
team1_penalties = 0
team2_penalties = 0
team1_time = 0
team2_time = 0
while True:
    team = int(input("Команда (1, 2 или 0 для конца): "))
    if team == 0:
        break
    time = int(input("Время удаления (2, 5, 10): "))
    if team == 1:
        team1_penalties += 1
        team1_time += time
    else:
        team2_penalties += 1
        team2_time += time
print("Команда 1: удалений", team1_penalties, "время", team1_time)
print("Команда 2: удалений", team2_penalties, "время", team2_time)




# 7.78
grades_5 = 0
grades_4 = 0
grades_3 = 0
grades_2 = 0
n = int(input("Сколько учеников? "))
for i in range(n):
    grade = int(input(f"Оценка ученика {i+1}: "))
    if grade == 5:
        grades_5 += 1
    elif grade == 4:
        grades_4 += 1
    elif grade == 3:
        grades_3 += 1
    elif grade == 2:
        grades_2 += 1
print("Пятерок:", grades_5)
print("Четверок:", grades_4)
print("Троек:", grades_3)
print("Двоек:", grades_2)




# 7.79
wins = 0
draws = 0
losses = 0
n = int(input("Сколько игр? "))
for i in range(n):
    points = int(input(f"Очки за игру {i+1}: "))
    if points == 3:
        wins += 1
    elif points == 1:
        draws += 1
    else:
        losses += 1
print("Побед:", wins)
print("Ничьих:", draws)
print("Поражений:", losses)





# 7.80
wins = 0
draws = 0
losses = 0
for i in range(20):
    scored = int(input(f"Забито в игре {i+1}: "))
    conceded = int(input(f"Пропущено в игре {i+1}: "))
    if scored > conceded:
        print("Выигрыш")
        wins += 1
    elif scored == conceded:
        print("Ничья")
        draws += 1
    else:
        print("Проигрыш")
        losses += 1
print("Итог: побед", wins, "ничьих", draws, "поражений", losses)
