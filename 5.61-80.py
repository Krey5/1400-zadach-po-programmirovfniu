# 5.61
x = int(input("x: "))
y = int(input("y: "))

# Способ 1: сложение x раз по y
product1 = 0
for _ in range(abs(x)):
    product1 += y
if x < 0:
    product1 = -product1

# Способ 2: сложение y раз по x
product2 = 0
for _ in range(abs(y)):
    product2 += x
if y < 0:
    product2 = -product2

print(f"Способ 1: {x} * {y} = {product1}")
print(f"Способ 2: {x} * {y} = {product2}")




# 5.62
a = float(input("a: "))
n = int(input("n: "))
result = 1
for _ in range(abs(n)):
    result *= a
if n < 0:
    result = 1 / result
print(f"{a}^{n} = {result}")




# 5.63
result = 20 ** 2
for i in range(19, 0, -1):
    result = (abs(result - i ** 2) / 2) ** 2
print("Результат выражения:", result)




# 5.64
num = int(input("Семизначное число: "))
reversed_num = 0
for _ in range(7):
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print("Число справа налево:", reversed_num)



# 5.65
n = int(input("n: "))
square = 0
odd = 1
for _ in range(n):
    square += odd
    odd += 2
print(f"{n}^2 = {square}")




# 5.66
total = 0
odd = 1
for i in range(1, 13):
    total += odd
    odd += 2
print("Сумма 1^2 + 2^2 + ... + 12^2 =", total)




# 5.67
n = int(input("n: "))
# Для n^3 сумма n последовательных нечетных чисел
start = n * (n - 1) + 1
total = 0
for _ in range(n):
    total += start
    start += 2
print(f"{n}^3 = {total}")




# 5.68
n = int(input("n (1 < n <= 10): "))
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print(f"1! + 2! + ... + {n}! = {total}")




# 5.69
n = int(input("n (1 < n <= 10): "))
total = 1
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += 1 / factorial
print(f"1 + 1/1! + 1/2! + ... + 1/{n}! = {total}")




# 5.70
x = float(input("x: "))
n = int(input("n (1 < n <= 10): "))
total = 1
factorial = 1
power = 1
for i in range(1, n + 1):
    factorial *= i
    power *= x
    total += power / factorial
print(f"1 + x/1! + x^2/2! + ... + x^{n}/{n}! = {total}")




# 5.71
import math
result = 0
for i in range(50, 0, -1):
    result = math.sqrt(i + result)
print("√(1 + √(2 + ... + √(50))) ≈", result)



# 5.72
import math
n = int(input("n: "))

# a)
sum_a = 0
partial = 0
for i in range(1, n + 1):
    partial += math.sin(i)
    sum_a += 1 / partial
print("a) Сумма =", sum_a)

# б)
result = math.sqrt(2)
for _ in range(1, n):
    result = math.sqrt(2 + result)
print("б) Результат =", result)

# в)
sum_c = 0
for i in range(1, n + 1):
    sum_c += math.cos(i)
print("в) Сумма cos =", sum_c)

# г)
sum_d = 0
for i in range(1, 2 * n + 1):
    sum_d += math.sin(i)
print("г) Сумма sin =", sum_d)

# д)
result = math.sqrt(3 * n)
for i in range(n - 1, 0, -1):
    result = math.sqrt(3 * i + result)
print("д) Результат =", result)




# 5.73
import math
length = 4.5
wall_distance = 3
slide_step = 0.2
distance = wall_distance
while distance <= length:
    angle = math.degrees(math.acos(distance / length))
    print(f"При расстоянии {distance:.1f} м: угол {angle:.2f}°")
    distance += slide_step



# 5.74
# Способ 1: с условным оператором
print("Способ 1:")
for num in range(10, 101):
    if num % 2 == 1:
        print(num, end=" ")
print()

# Способ 2: без условного оператора
print("Способ 2:")
for num in range(11, 101, 2):
    print(num, end=" ")




# 5.75
for num in range(100, 201):
    if num % 3 == 0:
        print(num)


# 5.76
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
for num in range(a, b + 1):
    if num % c == 0:
        print(num)




# 5.78
for num in range(100, 1000):
    if num % 47 == 43 and num % 43 == 45:
        print(num)






# 5.79
for num in range(1000, 10000):
    if num % 133 == 125 and num % 134 == 111:
        print(num)





# 5.80
n = int(input("n: "))
for num in range(10, 100):
    if num % n == 0 or n in (num // 10, num % 10):
        print(num)
