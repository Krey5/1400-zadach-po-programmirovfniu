# 4.61
import math
a = float(input("a (не 0): "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Два корня: {x1}, {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Один корень: {x}")
else:
    print("Действительных корней нет")


# 4.62
a = float(input("Сторона a первого прямоугольника: "))
b = float(input("Сторона b первого прямоугольника: "))
c = float(input("Сторона c второго прямоугольника: "))
d = float(input("Сторона d второго прямоугольника: "))

if (a < c and b < d) or (a < d and b < c):
    print("Прямоугольник a×b можно поместить в прямоугольник c×d")
else:
    print("Прямоугольник a×b нельзя поместить в прямоугольник c×d")


# 4.63
a = float(input("Ширина конверта (мм): "))
b = float(input("Высота конверта (мм): "))
c = float(input("Ширина открытки (мм): "))
d = float(input("Высота открытки (мм): "))

if (c + 2 <= a) and (d + 2 <= b):
    print("Открытка помещается в конверт")
else:
    print("Открытка не помещается в конверт")



# 4.64
a = float(input("Ширина форточки (см): "))
b = float(input("Высота форточки (см): "))
d = float(input("Диаметр головы (см): "))

if (d + 2 <= a) and (d + 2 <= b):
    print("Вася сможет высунуть голову в форточку")
else:
    print("Вася не сможет высунуть голову в форточку")



# 4.65
a = float(input("Ребро кирпича a: "))
b = float(input("Ребро кирпича b: "))
c = float(input("Ребро кирпича c: "))
x = float(input("Сторона отверстия x: "))
y = float(input("Сторона отверстия y: "))

# Проверяем, можно ли просунуть кирпич так, чтобы два ребра были параллельны сторонам отверстия
def brick_fits(a, b, c, x, y):
    return ((a <= x and b <= y) or
            (a <= y and b <= x) or
            (a <= x and c <= y) or
            (a <= y and c <= x) or
            (b <= x and c <= y) or
            (b <= y and c <= x))

if brick_fits(a, b, c, x, y):
    print("Кирпич пройдет в отверстие")
else:
    print("Кирпич не пройдет в отверстие")



# 4.66
a1 = float(input("Размер чемодана a1: "))
a2 = float(input("Размер чемодана a2: "))
a3 = float(input("Размер чемодана a3: "))
b1 = float(input("Размер коробки b1: "))
b2 = float(input("Размер коробки b2: "))
b3 = float(input("Размер коробки b3: "))

# Сортируем размеры, чтобы сравнивать минимальные и максимальные стороны
chemodan = sorted([a1, a2, a3])
korobka = sorted([b1, b2, b3])

if korobka[0] <= chemodan[0] and korobka[1] <= chemodan[1] and korobka[2] <= chemodan[2]:
    print("Коробка помещается в чемодан, можно сэкономить")
else:
    print("Коробка не помещается в чемодан")



# 4.67
num = int(input("Шестизначное число: "))
if 100000 <= num <= 999999:
    part1 = num // 1000
    part2 = num % 1000
    sum1 = part1 // 100 + (part1 // 10) % 10 + part1 % 10
    sum2 = part2 // 100 + (part2 // 10) % 10 + part2 % 10
    if sum1 == sum2:
        print("Число счастливое")
    else:
        print("Число не счастливое")
else:
    print("Число не шестизначное")




# 4.68
year = int(input("Год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")



# 4.70
k = int(input("День года (1-365): "))
day_of_week = (k + 0) % 7  # 1 января — понедельник (0)
if day_of_week in (5, 6):  # суббота, воскресенье
    print("Выходной день")
else:
    print("Рабочий день")
