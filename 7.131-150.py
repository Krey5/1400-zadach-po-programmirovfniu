# 7.132
unique_count = 0
prev = None
for i in range(30):
    num = int(input(f"Число {i+1}: "))
    if num != prev:
        unique_count += 1
    prev = num
print("Количество различных чисел:", unique_count)




# 7.133
prev = None
repeat_count = 0
while True:
    num = float(input("Введите число (1000 для конца): "))
    if num == 1000:
        break
    if num == prev:
        repeat_count += 1
    prev = num
print("Количество одинаковых подряд идущих чисел:", repeat_count)





# 7.134
prev = None
unique_count = 0
while True:
    num = float(input("Введите число (0 для конца): "))
    if num == 0:
        break
    if num != prev:
        unique_count += 1
    prev = num
print("Количество различных чисел:", unique_count)





# 7.135
n = int(input("Сколько чисел? "))
max_num = None
min_num = None
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
print("Максимум:", max_num)
print("Минимум:", min_num)




# 7.136
best_time = None
while True:
    time = float(input("Время спортсмена (0 для конца): "))
    if time == 0:
        break
    if best_time is None or time < best_time:
        best_time = time
    print("Лучший результат сейчас:", best_time)





# 7.137
max_distance = 0
while True:
    distance = float(input("Расстояние до города (0 для конца): "))
    if distance == 0:
        break
    if distance > max_distance:
        max_distance = distance
print("Самое удаленное расстояние:", max_distance)






# 7.138
max_temp = None
days = 30
for day in range(1, days + 1):
    temp = float(input(f"Температура {day} дня: "))
    if max_temp is None or temp > max_temp:
        max_temp = temp
print("Максимальная температура месяца:", max_temp)






# 7.139
max_speed = 0
for i in range(20):
    speed = int(input(f"Макс. скорость автомобиля {i+1}: "))
    if speed > max_speed:
        max_speed = speed
print("Самая высокая скорость:", max_speed)






# 7.140
import math
min_radius = None
while True:
    area = float(input("Площадь круга (0 для конца): "))
    if area == 0:
        break
    radius = math.sqrt(area / math.pi)
    if min_radius is None or radius < min_radius:
        min_radius = radius
print("Самый маленький радиус:", min_radius)





# 7.141
import math
max_diagonal = 0
while True:
    area = float(input("Площадь квадрата (0 для конца): "))
    if area == 0:
        break
    side = math.sqrt(area)
    diagonal = side * math.sqrt(2)
    if diagonal > max_diagonal:
        max_diagonal = diagonal
print("Самая длинная диагональ:", max_diagonal)





# 7.142
max_density = 0
for i in range(20):
    mass = float(input(f"Масса тела {i+1} (кг): "))
    volume = float(input(f"Объем тела {i+1} (см³): "))
    density = mass / (volume / 1000000)  # переводим в кг/м³
    if density > max_density:
        max_density = density
print("Максимальная плотность (кг/м³):", max_density)




# 7.143
min_density = None
for i in range(16):
    population = float(input(f"Население государства {i+1} (млн): "))
    area = float(input(f"Площадь государства {i+1} (тыс. км²): "))
    density = population / area  # млн чел / тыс. км² = тыс. чел/км²
    if min_density is None or density < min_density:
        min_density = density
print("Минимальная плотность населения:", min_density, "тыс. чел/км²")





# 7.144
n = int(input("Сколько пар? "))
max_sum = None
min_product = None
for i in range(n):
    a = float(input(f"a пары {i+1}: "))
    b = float(input(f"b пары {i+1}: "))
    pair_sum = a + b
    pair_product = a * b
    if max_sum is None or pair_sum > max_sum:
        max_sum = pair_sum
    if min_product is None or pair_product < min_product:
        min_product = pair_product
print("Максимальная сумма в паре:", max_sum)
print("Минимальное произведение в паре:", min_product)




# 7.145
n = int(input("Сколько судей? "))
scores = []
for i in range(n):
    score = float(input(f"Оценка судьи {i+1}: "))
    scores.append(score)
scores.sort()
trimmed = scores[1:-1]
average = sum(trimmed) / len(trimmed)
print("Итоговая оценка:", average)





# 7.146
max_height = None
min_height = None
while True:
    height = float(input("Рост человека (0 для конца): "))
    if height == 0:
        break
    if max_height is None or height > max_height:
        max_height = height
    if min_height is None or height < min_height:
        min_height = height
if max_height is not None and min_height is not None:
    print("Разница между самым высоким и самым низким:", max_height - min_height)




# 7.147
max_students = 0
min_students = None
for i in range(20):
    students = int(input(f"Учеников в классе {i+1}: "))
    if students > max_students:
        max_students = students
    if min_students is None or students < min_students:
        min_students = students
print("Разница между самым большим и самым маленьким классом:", max_students - min_students)






# 7.148
n = int(input("Сколько чисел? "))
max_num = None
min_num = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
if max_num is not None and min_num is not None:
    print("Максимум превышает минимум не более чем на 25?", max_num - min_num <= 25)





    # 7.149
max_mass = 0
min_mass = None
while True:
    mass = float(input("Масса человека (0 для конца): "))
    if mass == 0:
        break
    if mass > max_mass:
        max_mass = mass
    if min_mass is None or mass < min_mass:
        min_mass = mass
if min_mass is not None and min_mass > 0:
    print("Масса самого тяжелого > массы самого легкого в 2 раза?", max_mass / min_mass > 2)








    # 7.150
n = int(input("Сколько чисел? "))
max_len = 0
current_len = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 0
print("Наибольшая длина отрезка из четных чисел:", max_len)
