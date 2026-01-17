# 8.1
n = int(input("Введите число n: "))
i = 1
while i * i <= n:
    print(i * i)
    i += 1




# 8.2
n = int(input("Введите число n: "))
# Способ 1: с условием
i = 1
while i * i <= n:
    i += 1
print("Первое число, квадрат которого > n:", i)

# Способ 2: без явного условия (математически)
import math
result = math.isqrt(n) + 1
print("Результат (без цикла с условием):", result)





# 8.3
a = float(input("Введите a (0 < a ≤ 1): "))
znam = 1
value = 1.0
while value >= a:
    print(value)
    znam += 1
    value = 1 / znam





# 8.4
a = float(input("Введите a (0 < a ≤ 1): "))
znam = 1
while 1 / znam >= a:
    znam += 1
print("Первое число меньше a:", 1 / znam)





# 8.5
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 2
value = 1 + 1/n
while value >= a:
    print(value)
    n += 1
    value = 1 + 1/n




# 8.6
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 2
while True:
    value = 1 + 1/n
    if value >= a:
        print(value)
    else:
        break
    n += 1




# 8.7
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 2
while 1 + 1/n >= a:
    n += 1
print("Первое число меньше a:", 1 + 1/n)




# 8.8
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 2
while 1 + 1/n >= a:
    print("n =", n)
    n += 1





# 8.9
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 2
while 1 + 1/n >= a:
    n += 1
print("Наименьшее n:", n)





# 8.10
a = float(input("Введите a: "))
n = 1
value = 1.0
while value < a:
    print(value)
    n += 1
    value = 1 + 1/n





# 8.11
n = float(input("Введите число n: "))
sum_seq = 1 + 0.5 + 1/3
k = 3
while sum_seq <= n:
    k += 1
    sum_seq += 1/k
print("Первое число > n:", sum_seq)





# 8.12
a = float(input("Введите a: "))
sum_seq = 0
n = 1
while sum_seq <= a:
    sum_seq += 1/n
    if sum_seq > a:
        print("n =", n)
    n += 1





# 8.13
a = float(input("Введите a: "))
sum_seq = 0
n = 1
while sum_seq <= a:
    sum_seq += 1/n
    n += 1
print("Наименьшее n, при котором сумма > a:", n-1)





# 8.14
a = float(input("Введите a (0 < a ≤ 1): "))
# Способ 1
znam = 1
while 1/znam >= a:
    znam += 1
print("Первое число меньше a:", 1/znam)

# Способ 2
import math
znam = math.ceil(1/a)
print("Результат (другой способ):", 1/znam)




# 8.15
m = float(input("Введите m (0.52 ≤ m ≤ 33.7): "))
x = 1
while x <= 100:
    y = (x*x + 100) / (x + 200)
    if y < m:
        print(y)
    x += 1





# 8.16
m = float(input("Введите m (0.5 < m < 1): "))
n = 1
value = n / (n + 1)
while value < m:
    print(value)
    n += 1
    value = n / (n + 1)





# 8.17
num1, den1 = 1, 1  # 1/1
num2, den2 = 2, 1  # 2/1
while True:
    num3 = num1 + num2
    den3 = den1 + den2
    value = num3 / den3
    prev_value = num2 / den2
    if abs(value - prev_value) <= 0.001:
        print("Первый член, отличающийся от предыдущего не более чем на 0.001:", value)
        break
    num1, den1 = num2, den2
    num2, den3 = num3, den3





# 8.18
a = float(input("Введите a (>0): "))
x = float(input("Введите x (>0): "))
eps = float(input("Введите ε (>0): "))
y_prev = a
y_curr = 0.5 * (y_prev + x / (y_prev - 1))
while abs(y_curr**2 - y_prev**2) >= eps:
    y_prev = y_curr
    y_curr = 0.5 * (y_prev + x / (y_prev - 1))
print("y_n =", y_curr)





# 8.19
# a) Сумма чисел Фибоначчи, не превосходящих 1000
a, b = 1, 1
total = 0
while a <= 1000:
    total += a
    a, b = b, a + b
print("Сумма чисел Фибоначчи ≤ 1000:", total)

# б) Первое число Фибоначчи, большее n
n = int(input("Введите n (>1): "))
a, b = 1, 1
while a <= n:
    a, b = b, a + b
print("Первое число Фибоначчи > n:", a)
