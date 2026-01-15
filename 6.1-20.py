# 6.1
a = int(input("a (>b): "))
b = int(input("b: "))

# a) Целочисленное деление
quotient = 0
temp = a
while temp >= b:
    temp -= b
    quotient += 1
print(f"{a} // {b} = {quotient}")

# б) Остаток
remainder = a
while remainder >= b:
    remainder -= b
print(f"{a} % {b} = {remainder}")




# 6.2
n = int(input("n: "))
i = 1
while i <= n:
    print(i)
    i += 1




# 6.3
num = 11
while num <= 100:
    print(num)
    num += 2




# 6.4
num = 191
while num % 17 != 0:
    num += 1
print("Минимальное число >190, кратное 17:", num)





# 6.5
num = 5000
while num % 139 != 0:
    num -= 1
print("Максимальное число <=5000, кратное 139:", num)





# 6.6
fact = int(input("Факториал числа: "))
n = 1
product = 1
while product < fact:
    n += 1
    product *= n
if product == fact:
    print(f"Число: {n}")
else:
    print("Не является факториалом целого числа")




# 6.7
n = int(input("n: "))
i = 1
while i ** 2 <= n:
    print(i)
    i += 1





# 6.8
n = int(input("n: "))
i = 1
while i ** 2 <= n:
    i += 1
print(f"Первое натуральное число, квадрат которого > {n}: {i}")





# 6.9
while True:
    num = int(input("Введите четное число: "))
    if num % 2 == 0:
        break
    print("Ошибка: число нечетное")
print("Спасибо!")





# 6.10
password = 1234
while True:
    attempt = int(input("Введите пароль: "))
    if attempt == password:
        print("Добро пожаловать!")
        break
    print("Неверный пароль")





# 6.11
for _ in range(10):
    num = int(input("Введите число: "))
    if num == 0:
        break





# 6.12
while True:
    num = int(input("Введите число: "))
    print("Вы ввели число:", num)
    if num == 0:
        break





# 6.13
# a) С предусловием
i = 10
while i <= 30:
    print(i)
    i += 1

# б) С постусловием (эмулируем)
i = 10
while True:
    print(i)
    i += 1
    if i > 30:
        break





# 6.14
i = 100
while i >= 80:
    print(i)
    i -= 1




# 6.15
for n in range(21, 152, 10):
    print(2 * n)





# 6.16
n = 2
while n <= 12:
    print(n)
    n += 0.5





# 6.17
x = 1.0
while x <= 13.5:
    print(x)
    x += 0.5




# 6.18
import math
a = int(input("a: "))
b = int(input("b (<a): "))

# a) С предусловием
i = a
while i >= b:
    print(math.sqrt(i))
    i -= 1

# б) С постусловием
i = a
while True:
    print(math.sqrt(i))
    i -= 1
    if i < b:
        break





# 6.19
num = int(input("Натуральное число: "))
while num > 0:
    print(num % 10)
    num //= 10






# 6.20
num = int(input("Натуральное число: "))
temp = num
digit_sum = 0
digit_count = 0
digit_product = 1
first_digit = 0
last_digit = num % 10

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    digit_count += 1
    digit_product *= digit
    if temp == num:
        first_digit = digit
    temp //= 10

print("Сумма цифр:", digit_sum)
print("Количество цифр:", digit_count)
print("Произведение цифр:", digit_product)
print("Среднее арифметическое:", digit_sum / digit_count)
print("Сумма квадратов цифр:", sum(int(d)**2 for d in str(num)))
print("Сумма кубов цифр:", sum(int(d)**3 for d in str(num)))
print("Первая цифра:", first_digit)
print("Сумма первой и последней цифры:", first_digit + last_digit)
