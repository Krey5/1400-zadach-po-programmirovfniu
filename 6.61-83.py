# 6.61
n = input("Введите число с разными цифрами: ")
digits = [(int(d), i) for i, d in enumerate(n)]
sorted_digits = sorted(digits, key=lambda x: x[0], reverse=True)

max1, max2 = sorted_digits[0], sorted_digits[1]
min1, min2 = sorted_digits[-1], sorted_digits[-2]

print("Максимальные цифры и их номера от начала:", max1[1]+1, max2[1]+1)
print("Минимальные цифры и их номера от начала:", min1[1]+1, min2[1]+1)







# 6.62
n = input("Введите число: ")
# a
print("Число наоборот:", n[::-1])
# б
print("С двойками в начале и конце:", '2' + n + '2')
# в
a = input("Введите цифру для удаления: ")
print("Без цифры", a + ":", n.replace(a, ''))
# г
if len(n) >= 2:
    new_n = n[-1] + n[1:-1] + n[0]
    print("После перестановки первой и последней цифр:", new_n)
# д
print("Дублирование числа:", n + n)






# 6.63
n = input("Введите число: ")
if n == n[::-1]:
    print("Число палиндром")
else:
    print("Число не палиндром")






# 6.64
n = int(input("Введите сумму: "))
nominals = [64, 32, 16, 8, 4, 2, 1]
for nom in nominals:
    count = n // nom
    if count > 0:
        print(f"Купюр по {nom}: {count}")
        n -= count * nom







# 6.65
a = int(input("Введите a: "))
b = int(input("Введите b: "))
while b != 0:
    a, b = b, a % b
print("НОД:", a)






# 6.66
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print("НОД трёх чисел:", gcd(gcd(a, b), c))






# 6.67
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
print("НОК:", lcm(a, b))






# 6.68
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))
d = gcd(a, b)
print(f"Сокращённая дробь: {a//d}/{b//d}")






# 6.69
a, b = 425, 131
while a > 0 and b > 0:
    if a >= b:
        count = a // b
        print(f"Квадратов {b}x{b}: {count}")
        a %= b
    else:
        count = b // a
        print(f"Квадратов {a}x{a}: {count}")
        b %= a






# 6.70
a = int(input("Введите a: "))
b = int(input("Введите b: "))
while a > 0 and b > 0:
    if a >= b:
        count = a // b
        print(f"Квадратов {b}x{b}: {count}")
        a %= b
    else:
        count = b // a
        print(f"Квадратов {a}x{a}: {count}")
        b %= a





# 6.71
n = int(input("Введите число: "))
a, b = 1, 1
while b < n:
    a, b = b, a + b
if b == n or n == 1:
    print("Число является членом последовательности Фибоначчи")
else:
    print("Не является")





# 6.72
n = int(input("Введите число: "))
f = int(input("Первый член прогрессии: "))
s = int(input("Шаг прогрессии: "))
if (n - f) % s == 0 and (n - f) // s >= 0:
    print("Число является членом арифметической прогрессии")
else:
    print("Не является")





# 6.73
m = int(input("Введите число: "))
g = int(input("Первый член прогрессии: "))
z = int(input("Знаменатель прогрессии: "))
if z == 0:
    print("Не геометрическая прогрессия")
else:
    temp = m
    while temp % z == 0:
        temp //= z
    if temp == g and m >= g:
        print("Число является членом геометрической прогрессии")
    else:
        print("Не является")





# 6.74
n = int(input("Введите число: "))
# a
temp = n
while temp % 3 == 0:
    temp //= 3
print("Степень 3:", temp == 1)
# б
temp = n
while temp % 5 == 0:
    temp //= 5
print("Степень 5:", temp == 1)







# 6.75
# a
def f(x):
    return x**4 + 2*x**3 - x - 1

a, b = 0, 1
while b - a > 0.001:
    mid = (a + b) / 2
    if f(mid) == 0:
        break
    elif f(a) * f(mid) < 0:
        b = mid
    else:
        a = mid
print("Корень (а):", (a + b) / 2)

# б
def g(x):
    return x**3 - 0.2*x**2 - 0.2*x - 1.2

a, b = 1, 1.5
while b - a > 0.001:
    mid = (a + b) / 2
    if g(mid) == 0:
        break
    elif g(a) * g(mid) < 0:
        b = mid
    else:
        a = mid
print("Корень (б):", (a + b) / 2)







# 6.76
a = int(input("Ширина лужайки: "))
b = int(input("Длина лужайки: "))
print("Примерный ответ (упрощённо):", a * b - 1)





# 6.77
n = input("Введите число: ")
# a
if len(set(n)) == 1:
    print("Все цифры одинаковые")
else:
    print("Не все цифры одинаковые")
# б
has_pair = any(n[i] == n[i+1] for i in range(len(n)-1))
print("Есть две одинаковые цифры подряд:", has_pair)




# 6.78
n = input("Введите число: ")
rev = n[::-1]
sorted_rev = ''.join(sorted(rev))
print("Цифры справа налево упорядочены по возрастанию:", rev == sorted_rev)





# 6.79
n = input("Введите число: ")
rev = n[::-1]
sorted_rev = ''.join(sorted(rev))
# Проверка на неубывание: отсортированная версия должна быть равна оригиналу
print("Цифры справа налево упорядочены по неубыванию:", rev == sorted_rev)





# 6.80
n = input("Введите число: ")
sorted_n = ''.join(sorted(n))
print("Цифры слева направо упорядочены по возрастанию:", n == sorted_n)




# 6.81
n = input("Введите число: ")
# Проверка строгого возрастания
inc = all(int(n[i]) < int(n[i+1]) for i in range(len(n)-1))
print("Цифры образуют строго возрастающую последовательность:", inc)




# 6.82
n = input("Введите число: ")
# Проверка неубывания
non_dec = all(int(n[i]) <= int(n[i+1]) for i in range(len(n)-1))
print("Цифры упорядочены по неубыванию:", non_dec)




# 6.83
n = input("Введите число: ")
digits = [int(d) for d in n]
inc = all(digits[i] < digits[i+1] for i in range(len(digits)-1))
dec = all(digits[i] > digits[i+1] for i in range(len(digits)-1))
print("Монотонно возрастает или убывает:", inc or dec)
