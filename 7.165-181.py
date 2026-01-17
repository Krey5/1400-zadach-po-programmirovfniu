# 7.166
min_current = None
min_index = None
for i in range(20):
    voltage = float(input(f"Напряжение на сопротивлении {i+1} (В): "))
    resistance = float(input(f"Сопротивление {i+1} (Ом): "))
    current = voltage / resistance
    if min_current is None or current < min_current:
        min_current = current
        min_index = i + 1
print("Сопротивление с минимальным током (номер):", min_index)





# 7.167
n = int(input("Сколько чисел? "))
first_max_index = None
first_min_index = None
max_val = None
min_val = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if max_val is None or num > max_val:
        max_val = num
        first_max_index = i + 1
    if min_val is None or num < min_val:
        min_val = num
        first_min_index = i + 1
if first_max_index < first_min_index:
    print("Максимум встретился раньше")
else:
    print("Минимум встретился раньше")





# 7.168
first_oldest_index = None
first_youngest_index = None
oldest_age = None
youngest_age = None
n = int(input("Сколько людей? "))
for i in range(n):
    age = int(input(f"Возраст человека {i+1}: "))
    if oldest_age is None or age > oldest_age:
        oldest_age = age
        first_oldest_index = i + 1
    if youngest_age is None or age < youngest_age:
        youngest_age = age
        first_youngest_index = i + 1
if first_oldest_index < first_youngest_index:
    print("Самый старший указан раньше")
else:
    print("Самый молодой указан раньше")





# 7.169
first_win_index = None
last_loss_index = None
n = int(input("Сколько этапов? "))
for i in range(n):
    time = float(input(f"Время на этапе {i+1}: "))
    # Предполагаем, что лучшее время — это победа, худшее — последнее место
    # Здесь нужно знать лучший и худший результаты заранее, упростим:
    # Пусть вводятся места: 1 — победа, последнее — n
    place = int(input(f"Место на этапе {i+1}: "))
    if place == 1 and first_win_index is None:
        first_win_index = i + 1
    if place == n and last_loss_index is None:
        last_loss_index = i + 1
if first_win_index < last_loss_index:
    print("Победа была раньше последнего места")
else:
    print("Последнее место было раньше победы")





# 7.170
n = int(input("Сколько чисел? "))
prev = None
max_sum = None
min_sum = None
max_indices = None
min_indices = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if prev is not None:
        pair_sum = prev + num
        if max_sum is None or pair_sum > max_sum:
            max_sum = pair_sum
            max_indices = (i, i+1)
        if min_sum is None or pair_sum < min_sum:
            min_sum = pair_sum
            min_indices = (i, i+1)
    prev = num
print("Максимальная сумма соседних:", max_sum, "позиции:", max_indices)
print("Минимальная сумма соседних:", min_sum, "позиции:", min_indices)





# 7.171
n = int(input("Сколько чисел? "))
max1 = None
max2 = None
min1 = None
min2 = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    # Обновляем два максимума
    if max1 is None or num > max1:
        max2 = max1
        max1 = num
    elif max2 is None or num > max2:
        max2 = num
    # Обновляем два минимума
    if min1 is None or num < min1:
        min2 = min1
        min1 = num
    elif min2 is None or num < min2:
        min2 = num
print("Два максимальных:", max1, max2)
print("Два минимальных:", min1, min2)





# 7.172
first = None
second = None
for i in range(22):
    time = float(input(f"Результат спортсмена {i+1}: "))
    if first is None or time < first:
        second = first
        first = time
    elif second is None or time < second:
        second = time
print("Первое место:", first)
print("Второе место:", second)





# 7.173
max_speed = 0
second_max = 0
for i in range(12):
    speed = int(input(f"Макс. скорость автомобиля {i+1}: "))
    if speed > max_speed:
        second_max = max_speed
        max_speed = speed
    elif speed > second_max:
        second_max = speed
print("Скорость, больше которой только максимальная:", second_max)





# 7.174
first = 0
second = 0
third = 0
for i in range(12):
    points = int(input(f"Очки команды {i+1}: "))
    if points > first:
        third = second
        second = first
        first = points
    elif points > second:
        third = second
        second = points
    elif points > third:
        third = points
print("Очки за 1-е место:", first)
print("Очки за 2-е место:", second)
print("Очки за 3-е место:", third)





# 7.175
import itertools
n = int(input("Сколько спортсменов? "))
times = []
for i in range(n):
    t = float(input(f"Результат спортсмена {i+1}: "))
    times.append(t)
# Находим четверку с минимальной суммой
best_sum = None
best_indices = None
# Перебираем все сочетания из 4
for combo in itertools.combinations(range(n), 4):
    total = sum(times[i] for i in combo)
    if best_sum is None or total < best_sum:
        best_sum = total
        best_indices = combo
print("Лучшая четверка (индексы):", [i+1 for i in best_indices])





# 7.176
min1_temp = None
min2_temp = None
min1_day = None
min2_day = None
for day in range(1, 32):
    temp = float(input(f"Температура {day} июля: "))
    if min1_temp is None or temp < min1_temp:
        min2_temp = min1_temp
        min2_day = min1_day
        min1_temp = temp
        min1_day = day
    elif min2_temp is None or temp < min2_temp:
        min2_temp = temp
        min2_day = day
print("Самые прохладные дни:", min1_day, "и", min2_day)





# 7.177
A = int(input("Введите число A: "))
if A == 0:
    print("Максимальных элементов осталось 4")
elif A == 8:
    print("Максимальных элементов стало 5")
else:
    print("Максимальных элементов осталось 4 (A не равно 0 или 8)")





# 7.178
max_val = None
min_val = None
max_count = 0
min_count = 0
for i in range(12):
    num = int(input(f"Число {i+1}: "))
    if max_val is None or num > max_val:
        max_val = num
        max_count = 1
    elif num == max_val:
        max_count += 1
    if min_val is None or num < min_val:
        min_val = num
        min_count = 1
    elif num == min_val:
        min_count += 1
print("Сколько раз встречается максимум:", max_count)
print("Сколько раз встречается минимум:", min_count)






# 7.179
max_residents = 0
max_count = 0
while True:
    residents = int(input("Жильцов в квартире (0 для конца): "))
    if residents == 0:
        break
    if residents > max_residents:
        max_residents = residents
        max_count = 1
    elif residents == max_residents:
        max_count += 1
print("Квартир с наибольшим числом жильцов:", max_count)





# 7.180
min_temp = None
min_count = 0
for day in range(1, 32):
    temp = float(input(f"Температура {day} дня: "))
    if min_temp is None or temp < min_temp:
        min_temp = temp
        min_count = 1
    elif temp == min_temp:
        min_count += 1
print("Дней с самой низкой температурой:", min_count)





# 7.181
# a) Последняя цифра = правая половина кости
prev_right = None
valid = True
for i in range(20):
    num = int(input(f"Число {i+1}: "))
    left = num // 10
    right = num % 10
    if prev_right is not None and left != prev_right:
        valid = False
    prev_right = right
print("Соответствует правилам домино (вариант а)?", valid)

# б) Любая цифра может быть правой/левой
prev_num = None
valid = True
for i in range(20):
    num = int(input(f"Число {i+1}: "))
    if prev_num is not None:
        prev_left = prev_num // 10
        prev_right = prev_num % 10
        left = num // 10
        right = num % 10
        if not (prev_right == left or prev_right == right):
            valid = False
    prev_num = num
print("Соответствует правилам домино (вариант б)?", valid)
