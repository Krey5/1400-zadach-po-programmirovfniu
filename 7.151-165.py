# 7.151
m = int(input("Сколько чисел? "))
min_len = None
current_len = 0
for i in range(m):
    num = int(input(f"Число {i+1} (0 или 1): "))
    if num == 0:
        current_len += 1
    else:
        if current_len > 0:
            if min_len is None or current_len < min_len:
                min_len = current_len
        current_len = 0
# Проверяем последний отрезок
if current_len > 0:
    if min_len is None or current_len < min_len:
        min_len = current_len
if min_len is not None:
    print("Наименьшая длина отрезка из нулей:", min_len)
else:
    print("Нулей нет")






# 7.152
n = float(input("Введите число n: "))
closest_num = None
closest_index = None
min_diff = None
for i in range(1, 16):
    y = float(input(f"Число y{i}: "))
    diff = abs(y - n)
    if min_diff is None or diff < min_diff:
        min_diff = diff
        closest_num = y
        closest_index = i
print(f"Ближайшее число: {closest_num} (позиция {closest_index})")






# 7.153
max_even = None
for i in range(14):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        if max_even is None or num > max_even:
            max_even = num
if max_even is not None:
    print("Максимальное четное число:", max_even)
else:
    print("Четных чисел нет")





# 7.154
prev = None
max_repeat = 1
current_repeat = 1
while True:
    num = int(input("Введите число (0 для конца): "))
    if num == 0:
        break
    if num == prev:
        current_repeat += 1
        if current_repeat > max_repeat:
            max_repeat = current_repeat
    else:
        current_repeat = 1
    prev = num
print("Наибольшее количество подряд идущих одинаковых:", max_repeat)






# 7.155
prev = None
max_len = 1
current_len = 1
while True:
    num = int(input("Введите число (0 для конца): "))
    if num == 0:
        break
    if prev is not None and num > prev:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1
    prev = num
print("Наибольшая длина возрастающего фрагмента:", max_len)






# 7.156
def solve_with_reinput():
    numbers = []
    while True:
        num = int(input("Введите число (0 для конца): "))
        if num == 0:
            break
        numbers.append(num)
    
    max_len = 1
    current_len = 1
    for i in range(1, len(numbers)):
        if (numbers[i] > numbers[i-1]) or (numbers[i] < numbers[i-1]):
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1
    print("Наибольшая длина монотонного фрагмента:", max_len)

solve_with_reinput()





# 7.157
n = int(input("Сколько чисел? "))
max_index = None
min_index = None
max_val = None
min_val = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if max_val is None or num >= max_val:  # для последнего максимума
        max_val = num
        max_index = i + 1
    if min_val is None or num < min_val:  # для первого минимума
        min_val = num
        min_index = i + 1
print("Номер последнего максимума:", max_index)
print("Номер первого минимума:", min_index)





# 7.158
m = int(input("Сколько чисел? "))
max_index = None
min_index = None
max_val = None
min_val = None
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if max_val is None or num >= max_val:  # последний максимум
        max_val = num
        max_index = i + 1
    if min_val is None or num >= min_val:  # последний минимум (>= для последнего)
        min_val = num
        min_index = i + 1
print("Номер последнего максимума:", max_index)
print("Номер последнего минимума:", min_index)




# 7.159
max_residents = 0
max_flat = None
flat = 1
while True:
    residents = int(input(f"Жильцов в квартире {flat} (0 для конца): "))
    if residents == 0:
        break
    if residents >= max_residents:  # для квартиры с максимальным номером
        max_residents = residents
        max_flat = flat
    flat += 1
print("Квартира с наибольшим числом жильцов:", max_flat)





# 7.160
best_time = None
best_index = None
index = 1
while True:
    time = float(input("Время спортсмена (0 для конца): "))
    if time == 0:
        break
    if best_time is None or time < best_time:  # для первого лучшего
        best_time = time
        best_index = index
    index += 1
print("Лыжник с лучшим результатом стартовал по порядку:", best_index)






# 7.161
min_points = None
min_index = None
n = int(input("Сколько команд? "))
for i in range(n):
    points = int(input(f"Очки команды {i+1}: "))
    if min_points is None or points < min_points:  # для первой с минимальным
        min_points = points
        min_index = i + 1
print("Команда с наименьшим количеством очков (номер):", min_index)





# 7.162
max_precip = 0
max_day = None
for day in range(1, 32):
    precip = float(input(f"Осадки за {day} число: "))
    if precip >= max_precip:  # для последнего дня с максимумом
        max_precip = precip
        max_day = day
print("Самое большое количество осадков выпало числа:", max_day)





# 7.163
n = int(input("Сколько покупателей? "))
t = []
for i in range(n):
    ti = float(input(f"Время обслуживания покупателя {i+1}: "))
    t.append(ti)

c = []
total_wait = 0
for i in range(n):
    c.append(total_wait)
    total_wait += t[i]

min_service_time = min(t)
last_min_index = None
for i in range(n):
    if t[i] == min_service_time:
        last_min_index = i + 1

print("Время ожидания каждого покупателя:", c)
print("Покупатель с самым малым временем обслуживания (последний):", last_min_index)






# 7.164
n = int(input("Сколько пар? "))
max_avg = None
max_avg_index = None
min_geom = None
min_geom_index = None
import math
for i in range(n):
    a = float(input(f"a пары {i+1}: "))
    b = float(input(f"b пары {i+1}: "))
    avg = (a + b) / 2
    geom = math.sqrt(a * b)
    if max_avg is None or avg >= max_avg:  # для последней
        max_avg = avg
        max_avg_index = i + 1
    if min_geom is None or geom < min_geom:  # для первой
        min_geom = geom
        min_geom_index = i + 1
print("Пара с максимальным средним арифметическим (последняя):", max_avg_index)
print("Пара с минимальным средним геометрическим (первая):", min_geom_index)





# 7.165
max_speed = 0
max_index = None
for i in range(25):
    distance = float(input(f"Расстояние автомобиля {i+1} (км): "))
    time = float(input(f"Время автомобиля {i+1} (часы): "))
    speed = distance / time
    if speed > max_speed:
        max_speed = speed
        max_index = i + 1
print("Автомобиль с максимальной средней скоростью (номер):", max_index)
