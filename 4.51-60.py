# 4.51
num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if hundreds == 6 or tens == 6 or units == 6:
    print("Цифра 6 входит в число")
else:
    print("Цифра 6 не входит в число")

n = int(input("Введите цифру n: "))
if hundreds == n or tens == n or units == n:
    print(f"Цифра {n} входит в число")
else:
    print(f"Цифра {n} не входит в число")


# 4.52
num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if 6 in (hundreds, tens, units):
    print("Цифра 6 входит в число")
else:
    print("Цифра 6 не входит в число")



# 4.53
num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if 4 in (hundreds, tens, units) or 7 in (hundreds, tens, units):
    print("В число входит цифра 4 или 7")
else:
    print("В число не входят цифры 4 и 7")

if 3 in (hundreds, tens, units) or 6 in (hundreds, tens, units) or 9 in (hundreds, tens, units):
    print("В число входит цифра 3, 6 или 9")
else:
    print("В число не входят цифры 3, 6, 9")



# 4.54
num = int(input("Четырехзначное число: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

if d1 == 4 or d2 == 4 or d3 == 4 or d4 == 4:
    print("Цифра 4 входит в число")
else:
    print("Цифра 4 не входит в число")

b = int(input("Введите цифру b: "))
if b in (d1, d2, d3, d4):
    print(f"Цифра {b} входит в число")
else:
    print(f"Цифра {b} не входит в число")



# 4.55
num = int(input("Четырехзначное число: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

if 2 in (d1, d2, d3, d4) or 7 in (d1, d2, d3, d4):
    print("В число входит цифра 2 или 7")
else:
    print("В число не входят цифры 2 и 7")

if 3 in (d1, d2, d3, d4) or 6 in (d1, d2, d3, d4) or 9 in (d1, d2, d3, d4):
    print("В число входит цифра 3, 6 или 9")
else:
    print("В число не входят цифры 3, 6, 9")


# 4.56
num = int(input("Четырехзначное число: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

if d1 == d4 and d2 == d3:
    print("Запись числа симметрична")
else:
    print("Запись числа не симметрична")



# 4.57
a = int(input("Неотрицательное число a: "))
b = int(input("Положительное число b: "))
c = int(input("Число c: "))
d = int(input("Число d: "))

remainder = a % b
if remainder == c or remainder == d:
    print("Остаток равен c или d")
else:
    print("Остаток не равен ни c, ни d")




# 4.58
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == b or b == c or a == c:
    print("Есть хотя бы одна пара равных чисел")
else:
    print("Все числа различны")



# 4.59
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник не равносторонний")

if a == b or b == c or a == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник не равнобедренный")


# 4.60
h1 = float(input("Рост первого: "))
h2 = float(input("Рост второго: "))
h3 = float(input("Рост третьего: "))

if h1 == h2 == h3:
    print("Рост всех трех человек одинаковый")
else:
    print("Рост не одинаковый")
