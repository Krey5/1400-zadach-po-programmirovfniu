# 5.81
# a)
for num in range(100, 1000):
    square = num ** 2
    if square % 1000 == num:
        print(num)

# б)
for num in range(100, 1000):
    if num % 7 == 0:
        digit_sum = num // 100 + (num // 10) % 10 + num % 10
        if digit_sum % 7 == 0:
            print(num)





# 5.82
# a)
for num in range(10, 100):
    d1 = num // 10
    d2 = num % 10
    if (d1 ** 2 + d2 ** 2) % 13 == 0:
        print(num)

# б)
for num in range(10, 100):
    d1 = num // 10
    d2 = num % 10
    digit_sum = d1 + d2
    if digit_sum + digit_sum ** 2 == num:
        print(num)




# 5.83
total = sum(i for i in range(1, 50) if i % 2 == 1)
print("Сумма положительных нечетных чисел < 50:", total)





# 5.84
total = sum(num for num in range(100, 1000) if num % 2 == 0)
print("Сумма четных трехзначных чисел:", total)




# 5.85
a = int(input("a: "))
b = int(input("b: "))
total = sum(num for num in range(a, b + 1) if num > 0 and num % 4 == 0)
print("Сумма положительных чисел, кратных 4:", total)





# 5.86
total = sum(num for num in range(31, 100) 
            if num % 3 == 0 and num % 10 in (2, 4, 8))
print("Сумма чисел (30..99), кратных 3 и оканчивающихся на 2,4,8:", total)





# 5.87
count = 0
for num in range(100, 501):
    digit_sum = num // 100 + (num // 10) % 10 + num % 10
    if digit_sum == 15:
        count += 1
print("Количество чисел (100..500) с суммой цифр 15:", count)





# 5.88
s = int(input("s (0 < s <= 27): "))
count = 0
for num in range(100, 1000):
    digit_sum = num // 100 + (num // 10) % 10 + num % 10
    if digit_sum == s:
        count += 1
print("Количество трехзначных чисел с суммой цифр", s, ":", count)





# 5.89
count = 0
for num in range(100, 1000):
    if num % 7 == 0:
        digit_sum = num // 100 + (num // 10) % 10 + num % 10
        if digit_sum % 7 == 0:
            count += 1
print("Количество трехзначных чисел, кратных 7 и с суммой цифр кратной 7:", count)





# 5.90
n = int(input("n: "))
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
total = sum(fib[:n])
if total % 2 == 0:
    print(f"Сумма первых {n} чисел Фибоначчи четная")
else:
    print(f"Сумма первых {n} чисел Фибоначчи нечетная")




    # 5.91
num = int(input("Натуральное число: "))

# a) Все делители
print("Делители:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()

# б) Сумма делителей
div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
print("Сумма делителей:", div_sum)

# в) Сумма четных делителей
even_div_sum = sum(i for i in range(2, num + 1, 2) if num % i == 0)
print("Сумма четных делителей:", even_div_sum)

# г) Количество делителей
div_count = sum(1 for i in range(1, num + 1) if num % i == 0)
print("Количество делителей:", div_count)

# д) Количество нечетных делителей
odd_div_count = sum(1 for i in range(1, num + 1, 2) if num % i == 0)
print("Количество нечетных делителей:", odd_div_count)

# е) Количество делителей и сколько из них четных
even_count = sum(1 for i in range(2, num + 1, 2) if num % i == 0)
print(f"Всего делителей: {div_count}, из них четных: {even_count}")

# ж) Количество делителей > d
d = int(input("d: "))
count_greater = sum(1 for i in range(1, num + 1) if num % i == 0 and i > d)
print(f"Делителей > {d}: {count_greater}")





# 5.92
num = int(input("Натуральное число > 1: "))
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Число простое")
else:
    print("Число не простое")




# 5.93
num = int(input("Натуральное число: "))
div_sum = sum(i for i in range(1, num) if num % i == 0)
if div_sum == num:
    print("Число совершенное")
else:
    print("Число не совершенное")





# 5.94
n = int(input("n: "))
i = 1
while i ** 2 <= n:
    print(i, end=" ")
    i += 1
