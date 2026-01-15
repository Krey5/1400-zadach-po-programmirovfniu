# 5.1
for _ in range(9):
    print("20", end=" ")


# 5.2
number = int(input("Введите число: "))
count = int(input("Сколько раз вывести: "))
for _ in range(count):
    print(number, end=" ")




# 5.3
# a)
for i in range(20, 36):
    print(i)

# б)
a = int(input("a (<=50): "))
for i in range(a, 51):
    print(i ** 2)

# в)
b = int(input("b (>10): "))
for i in range(10, b + 1):
    print(i ** 3)

# г)
a = int(input("a: "))
b = int(input("b (>a): "))
for i in range(a, b + 1):
    print(i)




# 5.4
# a)
for i in range(10, 26):
    print(i, i + 0.4)

# б)
for i in range(25, 36):
    print(i, i + 0.5, i - 0.2)





# 5.5
# a)
for i in range(21, 9, -1):
    print(i, i - 1.8)

# б)
for i in range(45, 24, -1):
    print(i, i - 0.5, i - 0.8)





# 5.6
# a)
for i in range(21, 36):
    print(i, i - 0.6)

# б)
for i in range(16, 25):
    print(i, i - 0.5, i + 0.8)





# 5.7
price = 20.4
for i in range(2, 21):
    print(f"{i} шт: {price * i:.2f} руб")






# 5.8
print("Фунты    Кг")
for pounds in range(1, 11):
    kg = pounds * 0.453
    print(f"{pounds}        {kg:.3f}")





# 5.9
for inches in range(10, 23):
    cm = inches * 2.54
    print(f"{inches} дюймов = {cm:.2f} см")





# 5.10
rate = float(input("Курс доллара: "))
for dollars in range(1, 21):
    rubles = dollars * rate
    print(f"{dollars} USD = {rubles:.2f} RUB")





# 5.11
import math
R = 6350
for h in range(1, 11):
    distance = math.sqrt((R + h) ** 2 - R ** 2)
    print(f"Высота {h} км: {distance:.2f} км до горизонта")





# 5.12
import math
p0 = 1.29
z = 1.25e-4
print("Высота (м)   Плотность (кг/м³)")
for h in range(0, 1001, 100):
    p = p0 * math.exp(-h * z)
    print(f"{h}           {p:.4f}")




# 5.13
for i in range(1, 10):
    print(f"{i} × 7 = {i * 7}")




# 5.14
for i in range(1, 10):
    print(f"9 × {i} = {9 * i}")





# 5.15
n = int(input("n (1-9): "))
for i in range(1, 10):
    print(f"{i} × {n} = {i * n}")




# 5.16
import math
for i in range(2, 16):
    print(math.sin(i))




# 5.17
for x in range(4, 29):
    t = x + 3
    y = 3 * t ** 2 + 4.87 * t - 3
    print(f"x={x}, y={y}")




# 5.18
for a in range(2, 18):
    t = 3 * a
    z = 4.3 * t ** 2 - 8 * t + 13
    print(f"a={a}, z={z}")




# 5.19
import math
x = 0.1
while x <= 1.5:
    print(math.sin(x))
    x += 0.1




# 5.20
import math
x = 0.1
while x <= 0.9:
    print(math.sqrt(x))
    x += 0.1




# 5.21
price_per_kg = float(input("Стоимость 1 кг сыра: "))
for grams in range(50, 1001, 50):
    cost = (grams / 1000) * price_per_kg
    print(f"{grams} г = {cost:.2f} руб")




# 5.22
price_per_kg = float(input("Стоимость 1 кг конфет: "))
for grams in range(100, 2001, 100):
    cost = (grams / 1000) * price_per_kg
    print(f"{grams} г = {cost:.2f} руб")




# 5.23
x = 2.1
while x <= 2.8:
    print(x)
    x += 0.1




# 5.24
x = 3.2
while x <= 3.9:
    print(x)
    x += 0.1




# 5.25
x = 2.2
while x <= 4.2:
    print(x)
    x += 0.2




# 5.26
x = 4.4
while x <= 6.4:
    print(x)
    x += 0.2





# 5.27
# a)
total = sum(range(200, 601))
print("Сумма от 200 до 600:", total)

# б)
a = int(input("a (<=400): "))
total = sum(range(a, 401))
print("Сумма:", total)

# в)
b = int(input("b (>= -15): "))
total = sum(range(-15, b + 1))
print("Сумма:", total)

# г)
a = int(input("a: "))
b = int(input("b (>=a): "))
total = sum(range(a, b + 1))
print("Сумма:", total)





# 5.28
# a)
product = 1
for i in range(7, 15):
    product *= i
print("Произведение от 7 до 14:", product)

# б)
a = int(input("a (1..15): "))
product = 1
for i in range(a, 16):
    product *= i
print("Произведение:", product)

# в)
b = int(input("b (1..10): "))
product = 1
for i in range(1, b + 1):
    product *= i
print("Произведение:", product)

# г)
a = int(input("a: "))
b = int(input("b (>=a): "))
product = 1
for i in range(a, b + 1):
    product *= i
print("Произведение:", product)





# 5.29
# a)
numbers = list(range(1, 751))
average = sum(numbers) / len(numbers)
print("Среднее арифметическое 1..750:", average)

# б)
b = int(input("b (>=150): "))
numbers = list(range(150, b + 1))
average = sum(numbers) / len(numbers)
print("Среднее арифметическое:", average)

# в)
a = int(input("a (<=200): "))
numbers = list(range(a, 201))
average = sum(numbers) / len(numbers)
print("Среднее арифметическое:", average)

# г)
a = int(input("a: "))
b = int(input("b (>=a): "))
numbers = list(range(a, b + 1))
average = sum(numbers) / len(numbers)
print("Среднее арифметическое:", average)





# 5.30
# a)
total = sum(i ** 3 for i in range(25, 41))
print("Сумма кубов 25..40:", total)

# б)
a = int(input("a (0..50): "))
total = sum(i ** 2 for i in range(a, 51))
print("Сумма квадратов:", total)

# в)
n = int(input("n (1..100): "))
total = sum(i ** 2 for i in range(1, n + 1))
print("Сумма квадратов 1..n:", total)

# г)
a = int(input("a: "))
b = int(input("b (>=a): "))
total = sum(i ** 2 for i in range(a, b + 1))
print("Сумма квадратов:", total)
