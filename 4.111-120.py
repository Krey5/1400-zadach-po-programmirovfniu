# 4.111
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
d = int(input("Четвертое число: "))

count = 0
if a % 2 == 0: count += 1
if b % 2 == 0: count += 1
if c % 2 == 0: count += 1
if d % 2 == 0: count += 1
print("Количество четных:", count)


# 4.112
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

sum_pos = 0
if a > 0: sum_pos += a
if b > 0: sum_pos += b
if c > 0: sum_pos += c
print("Сумма положительных:", sum_pos)



# 4.113
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
d = float(input("Четвертое число: "))

total = 0
if a > 5: total += a
if b > 5: total += b
if c > 5: total += c
if d > 5: total += d
print("Сумма чисел >5:", total)




# 4.114
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
d = int(input("Четвертое число: "))

total = 0
if a % 3 == 0: total += a
if b % 3 == 0: total += b
if c % 3 == 0: total += c
if d % 3 == 0: total += d
print("Сумма кратных 3:", total)



# 4.115
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
d = int(input("Четвертое число: "))
e = int(input("Пятое число: "))
f = int(input("Шестое число: "))

total = 0
if a > 0: total += a
if b > 0: total += b
if c > 0: total += c
if d > 0: total += d
if e > 0: total += e
if f > 0: total += f
print("Сумма положительных:", total)



# 4.116
x = float(input("Введите x: "))

if x < -1:
    y = -1
elif x > -1:
    y = x
else:
    y = 1
print("y =", y)


# 4.117
a = float(input("Введите a: "))

if a > 0:
    z = 1
elif a == 0:
    z = 0
else:
    z = -1
print("z =", z)


# 4.118
x = float(input("Введите x: "))

if x <= 0:
    f = 0
elif x <= 1:
    f = x
else:
    f = x ** 2
print("f(x) =", f)



# 4.119
y = float(input("Введите y: "))

if y > 2:
    f = 2
elif y > 0:
    f = 0
else:
    f = -3 * y
print("f(y) =", f)


# 4.120
x = float(input("Введите x: "))

# a) График a: треугольник от (-1,0) до (0,1) до (1,0)
if -1 <= x <= 0:
    y = x + 1
elif 0 <= x <= 1:
    y = -x + 1
else:
    y = 0
print("y (а) =", y)

# б) График б: V-образный от (-1,0) до (0,-1) до (1,0)
if -1 <= x <= 0:
    y = -x - 1
elif 0 <= x <= 1:
    y = x - 1
else:
    y = 0
print("y (б) =", y)

# в) График в: ступенька
if x < -1:
    y = -1
elif -1 <= x < 0:
    y = 0
elif 0 <= x < 1:
    y = 1
else:
    y = 0
print("y (в) =", y)
