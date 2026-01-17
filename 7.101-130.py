# 7.101
prev = None
pos = 0
ordered = True
first_violation = None
while True:
    num = float(input("Введите число (10000 для конца): "))
    pos += 1
    if num == 10000:
        break
    if prev is not None and num < prev and ordered:
        ordered = False
        first_violation = pos
    prev = num
if ordered:
    print("Последовательность возрастает")
else:
    print(f"Нарушение упорядоченности на позиции {first_violation}")




# 7.102
prev = None
descending = True
n = int(input("Сколько учеников? "))
for i in range(n):
    height = float(input(f"Рост ученика {i+1}: "))
    if prev is not None and height > prev:
        descending = False
    prev = height
print("Ученики перечислены по убыванию роста?", descending)




# 7.103
prev = None
descending = True
n = int(input("Сколько команд? "))
for i in range(n):
    points = int(input(f"Очки команды {i+1}: "))
    if prev is not None and points > prev:
        descending = False
    prev = points
print("Команды перечислены по убыванию очков?", descending)






# 7.104
first = None
all_equal = True
for i in range(12):
    num = int(input(f"Число {i+1}: "))
    if first is None:
        first = num
    elif num != first:
        all_equal = False
print("Все числа равны?", all_equal)





# 7.105
first = None
all_equal = True
while True:
    num = int(input("Введите число (отрицательное для конца): "))
    if num < 0:
        break
    if first is None:
        first = num
    elif num != first:
        all_equal = False
print("Все числа равны?", all_equal)





# 7.106
total = 0
count = 0
for i in range(16):
    num = float(input(f"Число {i+1}: "))
    if num > 20:
        total += num
        count += 1
print("Среднее чисел > 20:", total / count)






# 7.107
x = int(input("Сколько чисел? "))
n = int(input("Число n: "))
total = 0
count = 0
for i in range(x):
    num = int(input(f"Число {i+1}: "))
    if num > n:
        total += num
        count += 1
print("Среднее чисел > n:", total / count if count > 0 else 0)






# 7.108
m = int(input("Сколько чисел? "))
n = int(input("Число n: "))
total = 0
count = 0
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if num % n == 0:
        total += num
        count += 1
print("Среднее кратных n:", total / count if count > 0 else 0)






# 7.109
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
for i in range(12):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1
print("Среднее четных:", even_sum / even_count if even_count > 0 else 0)
print("Среднее нечетных:", odd_sum / odd_count if odd_count > 0 else 0)






# 7.110
fat_sum = 0
fat_count = 0
other_sum = 0
other_count = 0
n = int(input("Сколько людей? "))
for i in range(n):
    mass = float(input(f"Масса человека {i+1}: "))
    if mass > 100:
        fat_sum += mass
        fat_count += 1
    else:
        other_sum += mass
        other_count += 1
print("Средняя масса полных:", fat_sum / fat_count if fat_count > 0 else 0)
print("Средняя масса остальных:", other_sum / other_count if other_count > 0 else 0)





# 7.111
boys_sum = 0
boys_count = 0
girls_sum = 0
girls_count = 0
n = int(input("Сколько учеников? "))
for i in range(n):
    height = float(input(f"Рост ученика {i+1} (отрицательный для мальчика): "))
    if height < 0:
        boys_sum += abs(height)
        boys_count += 1
    else:
        girls_sum += height
        girls_count += 1
print("Средний рост мальчиков:", boys_sum / boys_count if boys_count > 0 else 0)
print("Средний рост девочек:", girls_sum / girls_count if girls_count > 0 else 0)





# 7.112
total = 0
count = 0
for i in range(15):
    num = float(input(f"Число {i+1}: "))
    if num > 10:
        total += num
        count += 1
if count > 0:
    print("Среднее чисел > 10:", total / count)
else:
    print("Таких чисел нет")





# 7.113
x = int(input("Сколько чисел? "))
n = int(input("Число n: "))
total = 0
count = 0
for i in range(x):
    num = int(input(f"Число {i+1}: "))
    if num > n:
        total += num
        count += 1
if count > 0:
    print("Среднее чисел > n:", total / count)
else:
    print("Таких чисел нет")





# 7.114
total = 0
count = 0
for i in range(14):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        total += num
        count += 1
if count > 0:
    print("Среднее четных:", total / count)
else:
    print("Четных чисел нет")






# 7.115
m = int(input("Сколько чисел? "))
n = int(input("Число n: "))
total = 0
count = 0
for i in range(m):
    num = int(input(f"Число {i+1}: "))
    if num % n == 0:
        total += num
        count += 1
if count > 0:
    print("Среднее кратных n:", total / count)
else:
    print("Таких чисел нет")






# 7.116
car_sum = 0
car_count = 0
moto_sum = 0
moto_count = 0
while True:
    price = float(input("Стоимость транспорта (0 для конца): "))
    if price == 0:
        break
    if price > 5000:
        car_sum += price
        car_count += 1
    else:
        moto_sum += price
        moto_count += 1
car_avg = car_sum / car_count if car_count > 0 else 0
moto_avg = moto_sum / moto_count if moto_count > 0 else 0
print("Средняя стоимость авто > средней стоимости мото в 3 раза?", car_avg > moto_avg * 3)






# 7.117
boys_sum = 0
boys_count = 0
girls_sum = 0
girls_count = 0
n = int(input("Сколько учеников? "))
for i in range(n):
    height = float(input(f"Рост ученика {i+1} (отрицательный для мальчика): "))
    if height < 0:
        boys_sum += abs(height)
        boys_count += 1
    else:
        girls_sum += height
        girls_count += 1
boys_avg = boys_sum / boys_count if boys_count > 0 else 0
girls_avg = girls_sum / girls_count if girls_count > 0 else 0
print("Средний рост мальчиков > среднего роста девочек на 10 см?", boys_avg - girls_avg > 10)






# 7.118
n = int(input("Сколько чисел? "))
first_index = None
last_index = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num == 10:
        last_index = i + 1
        if first_index is None:
            first_index = i + 1
print("Номер последнего 10:", last_index)
print("Номер первого 10:", first_index)





# 7.119
n = int(input("Сколько чисел? "))
last_index = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num > 100:
        last_index = i + 1
print("Номер последнего числа > 100:", last_index)






# 7.120
n = int(input("Сколько чисел? "))
last_index = None
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num == 25:
        last_index = i + 1
if last_index:
    print("Номер последнего 25:", last_index)
else:
    print("Число 25 не найдено")






# 7.121
k = int(input("Сколько чисел? "))
last_index = None
for i in range(k):
    num = int(input(f"Число {i+1}: "))
    if num < 0:
        last_index = i + 1
print("Номер последнего отрицательного:", last_index)






# 7.123
positions = 1
for i in range(15):
    height = float(input(f"Рост ученика {i+1} (по убыванию): "))
    new_height = float(input("Рост нового ученика: "))
    if new_height < height:
        positions += 1
print("Новый ученик займет место:", positions)






# 7.124
place = 1
for i in range(20):
    points = int(input(f"Очки команды {i+1} (по убыванию): "))
    N = int(input("Очки искомой команды: "))
    if points > N:
        place += 1
print("Команда заняла место:", place)






# 7.125
total = 0
n = float(input("Число n: "))
for i in range(15):
    y = float(input(f"Число y{i+1}: "))
    if y < n:
        total += y
print("Сумма чисел < n:", total)

# б) Найти два числа, между которыми лежит n
prev = None
for i in range(15):
    y = float(input(f"Число y{i+1}: "))
    if prev is not None and prev < n < y:
        print(f"n между {prev} (позиция {i}) и {y} (позиция {i+1})")
    prev = y





# 7.126
first_neg_index = None
for i in range(15):
    num = float(input(f"Число {i+1}: "))
    if num < 0 and first_neg_index is None:
        first_neg_index = i + 1
if first_neg_index:
    print("Первый отрицательный на позиции:", first_neg_index)
else:
    print("Отрицательных нет")






# 7.127
first_666_index = None
while True:
    num = int(input("Введите число (100 для конца): "))
    if num == 100:
        break
    if num == 666 and first_666_index is None:
        first_666_index = pos
print("Первый 666 на позиции:", first_666_index if first_666_index else "не найден")






# 7.128
first_ends_7_index = None
for i in range(12):
    num = int(input(f"Число {i+1}: "))
    if num % 10 == 7 and first_ends_7_index is None:
        first_ends_7_index = i + 1
if first_ends_7_index:
    print("Первое число, оканчивающееся на 7, на позиции:", first_ends_7_index)
else:
    print("Таких чисел нет")





# 7.129
first_mult_7_index = None
while True:
    num = int(input("Введите число (-1 для конца): "))
    if num == -1:
        break
    if num % 7 == 0 and first_mult_7_index is None:
        first_mult_7_index = pos
print("Первое кратное 7 на позиции:", first_mult_7_index if first_mult_7_index else "не найдено")






# 7.130
prev = None
repeat_count = 0
for i in range(20):
    num = int(input(f"Число {i+1}: "))
    if num == prev:
        repeat_count += 1
    prev = num
print("Количество повторений:", repeat_count)
