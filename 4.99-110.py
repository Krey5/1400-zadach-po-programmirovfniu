# 4.99
a = float(input("Первое число: "))
b = float(input("Второе число: "))

# a) Два неполных условных оператора
max_num = a
if b > max_num:
    max_num = b
print("Максимум (два оператора):", max_num)

# б) Один неполный условный оператор
max_num = a
if b > a:
    max_num = b
print("Максимум (один оператор):", max_num)



# 4.100
a = float(input("Первое число: "))
b = float(input("Второе число: "))

# a) Два неполных условных оператора
max_num = a
min_num = a
if b > max_num:
    max_num = b
if b < min_num:
    min_num = b
print("Максимум:", max_num, "Минимум:", min_num)

# б) Один неполный условный оператор
max_num = a
min_num = a
if b > a:
    max_num = b
else:
    min_num = b
print("Максимум:", max_num, "Минимум:", min_num)



# 4.101
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

# a) Наибольшее
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("Наибольшее:", max_num)

# б) Наименьшее
min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
print("Наименьшее:", min_num)




# 4.102
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
d = float(input("Четвертое число: "))

# a) Наибольшее
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
if d > max_num:
    max_num = d
print("Наибольшее:", max_num)

# б) Наименьшее
min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d
print("Наименьшее:", min_num)




# 4.103
x = float(input("Число: "))
abs_x = x if x >= 0 else -x
print("Абсолютная величина:", abs_x)




# 4.104
a = float(input("Первое число: "))
b = float(input("Второе число: "))

abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b

# a) Полусумма абсолютных величин
half_sum = (abs_a + abs_b) / 2
print("Полусумма абсолютных величин:", half_sum)

# б) Квадратный корень из произведения абсолютных величин
import math
sqrt_product = math.sqrt(abs_a * abs_b)
print("Корень из произведения абсолютных величин:", sqrt_product)



# 4.105
a = float(input("Первое число: "))
b = float(input("Второе число: "))
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b

if abs_a > abs_b:
    a /= 2
print("Первое число после изменения:", a)





# 4.106
import math
a = float(input("Первое число: "))
b = float(input("Второе число: "))

if math.sqrt(b) < a:
    b *= 5
print("Второе число после изменения:", b)




# 4.107
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)




# 4.108
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

if a >= 0:
    a **= 2
if b >= 0:
    b **= 2
if c >= 0:
    c **= 2

print("Измененные числа:", a, b, c)



# 4.109
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

if 1.6 <= a <= 3.8:
    print(a)
if 1.6 <= b <= 3.8:
    print(b)
if 1.6 <= c <= 3.8:
    print(c)




# 4.110
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
d = float(input("Четвертое число: "))

count = 0
if a < 0: count += 1
if b < 0: count += 1
if c < 0: count += 1
if d < 0: count += 1
print("Количество отрицательных:", count)




