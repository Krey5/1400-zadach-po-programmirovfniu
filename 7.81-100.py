# 7.81
wins = 0
draws = 0
losses = 0
for i in range(20):
    result = int(input(f"Результат игры {i+1} (например, 32): "))
    scored = result // 10
    conceded = result % 10
    if scored > conceded:
        wins += 1
    elif scored == conceded:
        draws += 1
    else:
        losses += 1
print("Побед:", wins, "Ничьих:", draws, "Поражений:", losses)





# 7.82
n = int(input("Сколько чисел? "))
prev = None
count_equal = 0
count_zero = 0
count_even = 0
count_ends_5 = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if prev is not None:
        if num == prev:
            count_equal += 1
        if num == 0 and prev == 0:
            count_zero += 1
        if num % 2 == 0 and prev % 2 == 0:
            count_even += 1
        if num % 10 == 5 and prev % 10 == 5:
            count_ends_5 += 1
    prev = num
print("Пар одинаковых:", count_equal)
print("Пар нулей:", count_zero)
print("Пар четных:", count_even)
print("Пар оканчивающихся на 5:", count_ends_5)




# 7.83
has_even = False
n = int(input("Сколько чисел? "))
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        has_even = True
print("Есть четное число?", has_even)




# 7.84
count_pos = 0
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    if num > 0:
        count_pos += 1
print("Положительных не более 5?", count_pos <= 5)




# 7.85
count_le33 = 0
for i in range(15):
    num = float(input(f"Число {i+1}: "))
    if num <= 33.2:
        count_le33 += 1
print(f"Количество ≤33.2 кратно 4?", count_le33 % 4 == 0)




# 7.86
n = int(input("Сколько чисел? "))
count_lt20 = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num < 20:
        count_lt20 += 1
print("Чисел <20 ровно 5?", count_lt20 == 5)




# 7.87
m = int(input("Сколько чисел? "))
count_pos = 0
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if num > 0:
        count_pos += 1
print("Количество положительных кратно 3?", count_pos % 3 == 0)




# 7.88
n = int(input("Сколько чисел? "))
x = int(input("Число x: "))
count_neg = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num < 0:
        count_neg += 1
print(f"Отрицательных больше {x}?", count_neg > x)





# 7.89
m = int(input("Сколько чисел? "))
p = int(input("Число p: "))
count_gt_m = 0
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if num > m:
        count_gt_m += 1
print(f"Количество >{m} кратно {p}?", count_gt_m % p == 0)




# 7.90
has_3 = False
for i in range(12):
    grade = int(input(f"Оценка по предмету {i+1}: "))
    if grade == 3:
        has_3 = True
print("Нет троек?", not has_3)





# 7.91
days_no_rain = 0
for day in range(1, 32):
    rain = float(input(f"Осадки {day} марта: "))
    if rain == 0:
        days_no_rain += 1
print("Осадков не было 10 дней?", days_no_rain >= 10)





# 7.92
has_2 = False
for i in range(28):
    grade = int(input(f"Оценка ученика {i+1}: "))
    if grade == 2:
        has_2 = True
print("Есть двойки?", has_2)





# 7.93
has_power_200 = False
for i in range(30):
    power = int(input(f"Мощность автомобиля {i+1}: "))
    if power > 200:
        has_power_200 = True
print("Есть модель мощнее 200 л.с.?", has_power_200)






# 7.94
n = int(input("Сколько чисел? "))
prev = None
prev2 = None
count_max = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if prev2 is not None and prev is not None:
        if prev > prev2 and prev > num:
            count_max += 1
    prev2, prev = prev, num
print("Строгих локальных максимумов:", count_max)





# 7.95
n = int(input("Сколько чисел? "))
prev = None
sign_changes = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if prev is not None:
        if (prev > 0 and num < 0) or (prev < 0 and num > 0):
            sign_changes += 1
    prev = num
print("Смен знака:", sign_changes)





# 7.96
prev = None
found = False
for i in range(1, 16):
    num = int(input(f"Число {i}: "))
    if prev is not None and num == prev and not found:
        print(f"Первая пара одинаковых: позиции {i-1} и {i}")
        found = True
    prev = num
if not found:
    print("Нет одинаковых соседних чисел")






# 7.97
prev = None
pos = 0
found = False
while True:
    num = int(input("Введите число (-1 для конца): "))
    pos += 1
    if num == -1:
        break
    if prev is not None and num == prev and not found:
        print(f"Первая пара одинаковых: позиции {pos-1} и {pos}")
        found = True
    prev = num
if not found:
    print("Нет одинаковых соседних чисел")






# 7.98
prev = None
found = False
for i in range(1, 21):
    num = int(input(f"Число {i}: "))
    if prev is not None and num % 2 != 0 and prev % 2 != 0 and not found:
        print(f"Первая пара нечетных: позиции {i-1} и {i}")
        found = True
    prev = num
if not found:
    print("Нет соседних нечетных чисел")





# 7.99
prev = None
pos = 0
found = False
while True:
    num = int(input("Введите число (9999 для конца): "))
    pos += 1
    if num == 9999:
        break
    if prev is not None and num % 2 == 0 and prev % 2 == 0 and not found:
        print(f"Первая пара четных: позиции {pos-1} и {pos}")
        found = True
    prev = num
if not found:
    print("Нет соседних четных чисел")






# 7.100
prev = None
ordered = True
first_violation = None
for i in range(1, 16):
    num = float(input(f"Число {i}: "))
    if prev is not None and num < prev and ordered:
        ordered = False
        first_violation = i
    prev = num
if ordered:
    print("Последовательность возрастает")
else:
    print(f"Нарушение упорядоченности на позиции {first_violation}")
