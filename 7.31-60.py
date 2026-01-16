# 7.31
total = 0
count = 0
while True:
    num = int(input("Введите число (отрицательное для конца): "))
    if num < 0:
        break
    total += num
    count += 1
print("Среднее арифметическое:", total / count if count > 0 else 0)




# 7.32
total1 = 0
total2 = 0
for i in range(20):
    age = float(input(f"Возраст ученика {i+1} класса 1: "))
    total1 += age
for i in range(20):
    age = float(input(f"Возраст ученика {i+1} класса 2: "))
    total2 += age
print("Средний возраст в классе 1:", total1 / 20)
print("Средний возраст в классе 2:", total2 / 20)




# 7.33
jan_days = 31
mar_days = 31
jan_total = 0
mar_total = 0
for day in range(1, jan_days + 1):
    precipitation = float(input(f"Осадки {day} января: "))
    jan_total += precipitation
for day in range(1, mar_days + 1):
    precipitation = float(input(f"Осадки {day} марта: "))
    mar_total += precipitation
print("Среднее за январь:", jan_total / jan_days)
print("Среднее за март:", mar_total / mar_days)





# 7.34
n = int(input("Сколько учеников в каждом классе? "))
total1 = 0
total2 = 0
for i in range(n):
    height = float(input(f"Рост ученика {i+1} класса 1: "))
    total1 += height
for i in range(n):
    height = float(input(f"Рост ученика {i+1} класса 2: "))
    total2 += height
print("Средний рост в классе 1:", total1 / n)
print("Средний рост в классе 2:", total2 / n)





# 7.35
n = int(input("Сколько учеников в каждом классе? "))
total1 = 0
total2 = 0
for i in range(n):
    grade = int(input(f"Оценка ученика {i+1} класса 1: "))
    total1 += grade
for i in range(n):
    grade = int(input(f"Оценка ученика {i+1} класса 2: "))
    total2 += grade
print("Средняя оценка в классе 1:", total1 / n)
print("Средняя оценка в классе 2:", total2 / n)





# 7.36
total_wheat = 0
total_area = 0
for i in range(10):
    area = float(input(f"Площадь района {i+1} (га): "))
    yield_per_ha = float(input(f"Урожайность района {i+1} (ц/га): "))
    total_wheat += area * yield_per_ha
    total_area += area
print("Собрано пшеницы в области (ц):", total_wheat)
print("Средняя урожайность (ц/га):", total_wheat / total_area)




# 7.37
total_population = 0
total_area = 0
for i in range(12):
    population = float(input(f"Население района {i+1} (тыс. чел): "))
    area = float(input(f"Площадь района {i+1} (км²): "))
    total_population += population
    total_area += area
print("Средняя плотность населения (тыс. чел/км²):", total_population / total_area)





# 7.38
total_area = 0
for i in range(12):
    population = float(input(f"Население района {i+1} (тыс. чел): "))
    density = float(input(f"Плотность района {i+1} (тыс. чел/км²): "))
    total_area += population / density
print("Общая площадь области (км²):", total_area)






# 7.39
n = int(input("Сколько чисел? "))
# a
abs_sum = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    abs_sum += abs(num)
print("Сумма модулей:", abs_sum)

# б
abs_product = 1
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    abs_product *= abs(num)
print("Произведение модулей:", abs_product)

# в
nums = []
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    nums.append(num)
for i in range(n - 1):
    print("Сумма соседних:", nums[i] + nums[i+1])

# г
sign_sum = 0
sign = 1
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    sign_sum += sign * num
    sign *= -1
print("Знакопеременная сумма:", sign_sum)




# 7.40
total = 0
for i in range(12):
    num = float(input(f"Число {i+1}: "))
    if num > 10.75:
        total += num
print("Сумма чисел > 10.75:", total)





# 7.41
n = int(input("Сколько чисел? "))
p = float(input("Число p: "))
total = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if num > p:
        total += num
print("Сумма чисел > p:", total)





# 7.42
total = 0
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    if num % 2 == 0:
        total += num
print("Сумма четных чисел:", total)





# 7.43
total = 0
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    if num % 10 == 0:
        total += num
print("Сумма чисел, оканчивающихся на 0:", total)





# 7.44
total = 0
for i in range(20):
    num = int(input(f"Число {i+1}: "))
    if (i + 1) % 2 == 0:  # четные позиции (2, 4, ...)
        total += num
print("Сумма на четных позициях:", total)





# 7.45
total = 0
for i in range(15):
    num = float(input(f"Число {i+1}: "))
    if (i + 1) % 2 != 0:  # нечетные позиции (1, 3, ...)
        total -= num
print("Сумма с минусом на нечетных позициях:", total)





# 7.46
n = int(input("Сколько чисел? "))
numbers = []
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    numbers.append(num)
print("a) a1 + an =", numbers[0] + numbers[-1])
print("б) a2 - a(n-1) =", numbers[1] - numbers[-2])





# 7.47
total = 0
while True:
    price = float(input("Стоимость товара (0 для конца): "))
    if price == 0:
        break
    if price > 1000:
        total += price
print("Общая стоимость товаров дороже 1000 руб:", total)





# 7.48
total_pages = 0
while True:
    pages = int(input("Число страниц (0 для конца): "))
    if pages == 0:
        break
    if pages > 16:
        total_pages += pages
print("Общее число страниц в журналах:", total_pages)




# 7.49
days = 30  # например, апрель
total = 0
for day in range(1, days + 1):
    precipitation = float(input(f"Осадки за {day} число: "))
    if day % 2 == 0:  # четные числа
        total += precipitation
print("Осадков по четным числам:", total)




# 7.50
total = 0
for grade in range(1, 12):
    students = int(input(f"Учеников в {grade} классе: "))
    if grade % 2 != 0:  # 1, 3, 5, ...
        total += students
print("Учеников в нечетных классах:", total)




# 7.51
total = 0
while True:
    num = int(input("Введите число: "))
    if num % 2 == 0:
        break
    total += num
print("Сумма нечетных чисел в начале:", total)




# 7.52
sum_gt20 = 0
sum_lt50 = 0
for i in range(14):
    num = int(input(f"Число {i+1}: "))
    if num > 20:
        sum_gt20 += num
    if num < 50:
        sum_lt50 += num
print("Сумма >20 превышает 100?", sum_gt20 > 100)
print("Сумма <50 четная?", sum_lt50 % 2 == 0)




# 7.53
n = int(input("Сколько чисел? "))
sum_lt25 = 0
sum_le20 = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if num < 25.5:
        sum_lt25 += num
    if num <= 20:
        sum_le20 += num
print("Сумма <25.5 не превышает 50?", sum_lt25 <= 50)
print("Сумма ≤20 кратна 3?", sum_le20 % 3 == 0)




# 7.54
n = int(input("Сколько чисел? "))
p = float(input("Число p: "))
total = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if num > 20.5:
        total += num
print("Сумма >20.5 < p?", total < p)





# 7.55
n = int(input("Сколько чисел? "))
m = int(input("Число m: "))
q = int(input("Число q: "))
total = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num <= m:
        total += num
print("Сумма ≤ m > q?", total > q)





# 7.56
n = int(input("Сколько чисел? "))
m = int(input("Число m: "))
p = int(input("Число p: "))
total = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    if num <= m:
        total += num
print(f"Сумма ≤ {m} кратна {p}?", total % p == 0)





# 7.57
days = 28  # февраль
even_sum = 0
odd_sum = 0
for day in range(1, days + 1):
    precip = float(input(f"Осадки за {day} февраля: "))
    if day % 2 == 0:
        even_sum += precip
    else:
        odd_sum += precip
print("По четным числам выпало больше?", even_sum > odd_sum)





# 7.58
even_side = 0
odd_side = 0
house = 1
while True:
    residents = int(input(f"Жильцов в доме {house} (0 для конца): "))
    if residents == 0:
        break
    if house % 2 == 0:
        even_side += residents
    else:
        odd_side += residents
    house += 1
if even_side > odd_side:
    print("Больше жителей на четной стороне")
else:
    print("Больше жителей на нечетной стороне")




# 7.59
count_5 = 0
n = int(input("Сколько учеников? "))
for i in range(n):
    grade = int(input(f"Оценка ученика {i+1}: "))
    if grade == 5:
        count_5 += 1
print("Пятерок:", count_5)





# 7.60
days = 30
count_below_zero = 0
for day in range(1, days + 1):
    temp = float(input(f"Температура {day} дня: "))
    if temp < 0:
        count_below_zero += 1
print("Дней с температурой ниже 0:", count_below_zero)
