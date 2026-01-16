# 7.1
total = 0
for i in range(10):
    num = float(input(f"Введите число {i+1}: "))
    total += num
print("Сумма:", total)



# 7.2
n = int(input("Сколько чисел? "))
total = 0
for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    total += num
print("Сумма:", total)




# 7.3
perimeter = 0
for i in range(12):
    side = float(input(f"Длина стороны {i+1}: "))
    perimeter += side
print("Периметр 12-угольника:", perimeter)




# 7.4
total_mass = 0
while True:
    mass = float(input("Масса предмета (0 для конца): "))
    if mass == 0:
        break
    total_mass += mass
print("Общая масса груза:", total_mass)





# 7.5
total_salary = 0
n = int(input("Сколько сотрудников? "))
for i in range(n):
    salary = float(input(f"Зарплата сотрудника {i+1}: "))
    total_salary += salary
print("Общая сумма выплат:", total_salary)




# 7.6
total_resistance = 0
n = int(input("Сколько элементов? "))
for i in range(n):
    r = float(input(f"Сопротивление элемента {i+1}: "))
    total_resistance += r
print("Общее сопротивление (последовательно):", total_resistance)




# 7.7
total_inverse = 0
n = int(input("Сколько элементов? "))
for i in range(n):
    r = float(input(f"Сопротивление элемента {i+1}: "))
    total_inverse += 1 / r
total_resistance = 1 / total_inverse
print("Общее сопротивление (параллельно):", total_resistance)




# 7.8
total = 0
count = 0
while True:
    num = int(input("Введите число (0 для конца): "))
    if num == 0:
        break
    total += num
    count += 1
print("Сумма:", total)
print("Количество чисел:", count)




# 7.9
sum1 = 0
sum2 = 0
for i in range(4):
    grade1 = int(input(f"Оценка первого ученика по предмету {i+1}: "))
    grade2 = int(input(f"Оценка второго ученика по предмету {i+1}: "))
    sum1 += grade1
    sum2 += grade2
print("Сумма оценок первого:", sum1)
print("Сумма оценок второго:", sum2)




# 7.10
score1 = 0
score2 = 0
for i in range(5):
    s1 = int(input(f"Баллы первого спортсмена в виде {i+1}: "))
    s2 = int(input(f"Баллы второго спортсмена в виде {i+1}: "))
    score1 += s1
    score2 += s2
print("Сумма баллов первого:", score1)
print("Сумма баллов второго:", score2)




# 7.11
product = 1
for i in range(8):
    num = float(input(f"Число {i+1}: "))
    product *= num
print("Произведение:", product)




# 7.12
while True:
    num = int(input("Введите число (0 для конца): "))
    print(num)
    if num == 0:
        break




# 7.13
total = 0
for i in range(10):
    num = float(input(f"Число {i+1}: "))
    total += num * num
print("Сумма квадратов:", total)





# 7.14
n = int(input("Сколько чисел? "))
total = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    total += num * num
print("Сумма квадратов:", total)





# 7.15
total = 0
for i in range(10):
    num = float(input(f"Число {i+1}: "))
    total += num
print("Сумма > 100.78?", total > 100.78)




# 7.16
n = int(input("Сколько чисел? "))
p = int(input("Число p: "))
total = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    total += num
print("Сумма < p?", total < p)




# 7.17
total = 0
for i in range(8):
    num = int(input(f"Число {i+1}: "))
    total += num
print("Сумма четная?", total % 2 == 0)




# 7.18
n = int(input("Сколько чисел? "))
b = int(input("Число b: "))
total = 0
for i in range(n):
    num = int(input(f"Число {i+1}: "))
    total += num
print(f"Сумма кратна {b}?", total % b == 0)




# 7.19
feb_days = 28
total = 0
for day in range(1, feb_days + 1):
    precipitation = float(input(f"Осадки за {day} февраля: "))
    total += precipitation
last_year = float(input("Осадки за прошлый февраль: "))
print("Больше, чем в прошлом году?", total > last_year)




# 7.20
capacity = float(input("Грузоподъемность автомобиля: "))
total = 0
while True:
    mass = float(input("Масса груза (0 для конца): "))
    if mass == 0:
        break
    total += mass
    if total > capacity:
        print("Перегруз!")
        break
print("Общая масса:", total)




# 7.21
score1 = 0
score2 = 0
for i in range(10):
    s1 = int(input(f"Баллы первого в виде {i+1}: "))
    s2 = int(input(f"Баллы второго в виде {i+1}: "))
    score1 += s1
    score2 += s2
if score1 > score2:
    print("Первый спортсмен лучше")
else:
    print("Второй спортсмен лучше")





# 7.22
cost1 = 0
cost2 = 0
for i in range(8):
    c1 = float(input(f"Стоимость предмета {i+1} в наборе 1: "))
    c2 = float(input(f"Стоимость предмета {i+1} в наборе 2: "))
    cost1 += c1
    cost2 += c2
if cost1 < cost2:
    print("Первый набор дешевле")
else:
    print("Второй набор дешевле")




# 7.23
product = 1
for i in range(8):
    num = float(input(f"Число {i+1}: "))
    product *= num
print("Произведение < 10000?", product < 10000)





# 7.24
n = int(input("Сколько чисел? "))
s = float(input("Число s: "))
product = 1
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    product *= num
print("Произведение > s?", product > s)





# 7.25
total = 0
for i in range(10):
    num = float(input(f"Число {i+1}: "))
    total += num
print("Среднее арифметическое:", total / 10)





# 7.26
n = int(input("Сколько чисел? "))
total = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    total += num
print("Среднее арифметическое:", total / n)





# 7.27
total = 0
for i in range(20):
    grade = int(input(f"Оценка ученика {i+1}: "))
    total += grade
print("Средняя оценка по физике:", total / 20)




# 7.28
total = 0
for i in range(10):
    grade = int(input(f"Оценка по предмету {i+1}: "))
    total += grade
print("Средняя оценка:", total / 10)




# 7.29
n = int(input("Сколько учеников? "))
total = 0
for i in range(n):
    grade = int(input(f"Оценка ученика {i+1}: "))
    total += grade
print("Средняя оценка по алгебре:", total / n)




# 7.30
n = int(input("Сколько предметов? "))
total = 0
for i in range(n):
    mass = float(input(f"Масса предмета {i+1}: "))
    total += mass
print("Средняя масса:", total / n)
