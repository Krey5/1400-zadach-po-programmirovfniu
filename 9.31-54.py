# 9.31
for num in range(1, 100000):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(num)



# 9.32
a = int(input("a: "))
b = int(input("b: "))
max_sum = 0
best_num = a
for num in range(a, b+1):
    divisor_sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum > max_sum:
        max_sum = divisor_sum
        best_num = num
print(f"Число с максимальной суммой делителей: {best_num} (сумма {max_sum})")





# 9.33
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

for a in range(1, 50000):
    b = sum_of_divisors(a)
    if b > a:  # Чтобы не повторяться
        if sum_of_divisors(b) == a:
            print(f"Дружественная пара: {a} и {b}")






# 9.34
n = int(input("n (до 100): "))
count = 0
# a) Число способов
for rub10 in range(n//10 + 1):
    for rub5 in range((n - rub10*10)//5 + 1):
        for rub2 in range((n - rub10*10 - rub5*5)//2 + 1):
            rub1 = n - rub10*10 - rub5*5 - rub2*2
            if rub1 >= 0:
                count += 1
print("Число способов:", count)

# б) Все способы
for rub10 in range(n//10 + 1):
    for rub5 in range((n - rub10*10)//5 + 1):
        for rub2 in range((n - rub10*10 - rub5*5)//2 + 1):
            rub1 = n - rub10*10 - rub5*5 - rub2*2
            if rub1 >= 0:
                print(f"10 руб: {rub10}, 5 руб: {rub5}, 2 руб: {rub2}, 1 руб: {rub1}")





# 9.35
n = int(input("n: "))
nominals = [64, 32, 16, 8, 4, 2, 1]
for amount in range(n, n+11):
    print(f"\nСумма {amount}:")
    temp = amount
    for nom in nominals:
        count = temp // nom
        if count > 0:
            print(f"  {nom}: {count}")
            temp -= count * nom






# 9.36
s = int(input("Площадь s: "))
print("Прямоугольники с площадью", s)
# а) Разные
for a in range(1, s+1):
    if s % a == 0:
        b = s // a
        print(f"{a} x {b}")
# б) Совпадающие (без перестановок)
for a in range(1, int(s**0.5) + 1):
    if s % a == 0:
        b = s // a
        if a <= b:
            print(f"{a} x {b}")





# 9.37
v = int(input("Объем v: "))
print("Параллелепипеды с объемом", v)
# а) Разные
for a in range(1, v+1):
    if v % a == 0:
        for b in range(1, v//a + 1):
            if (v // a) % b == 0:
                c = v // a // b
                print(f"{a} x {b} x {c}")
# б) Совпадающие (без перестановок)
for a in range(1, int(v**(1/3)) + 1):
    if v % a == 0:
        for b in range(a, int((v/a)**0.5) + 1):
            if (v // a) % b == 0:
                c = v // a // b
                if b <= c:
                    print(f"{a} x {b} x {c}")






# 9.38
for x in range(1, 31):
    for y in range(x, 31):  # Чтобы не повторять пары
        for k in range(1, 31):
            if x**2 + y**2 == k**2:
                print(f"{x}^2 + {y}^2 = {k}^2")





# 9.39
m = int(input("m: "))
n = int(input("n: "))
total = 0
for i in range(1, m+1):
    total += i**n
print(f"1^{n} + 2^{n} + ... + {m}^{n} = {total}")







# 9.40
n = int(input("n: "))
total = 0
for i in range(1, n+1):
    total += i**i
print(f"1^1 + 2^2 + ... + {n}^{n} = {total}")






# 9.41
n = int(input("n (≤27): "))
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a + b + c == n:
                print(a*100 + b*10 + c)





# 9.43
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Сколько чисел? "))
nums = [int(input(f"Число {i+1}: ")) for i in range(n)]
result = nums[0]
for num in nums[1:]:
    result = gcd(result, num)
print("НОД всех чисел:", result)






# 9.44
weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("Вес v (в граммах): "))
count = 0
# Перебор всех комбинаций
import itertools
for r in range(1, len(weights)+1):
    for combo in itertools.combinations(weights, r):
        if sum(combo) == v:
            count += 1
            print(f"Способ {count}: {combo}")
print(f"Всего способов: {count}")





# 9.45
m = int(input("m: "))
n = int(input("n: "))
for num in range(1, n):
    digit_sum = sum(int(d) for d in str(num))
    if digit_sum ** 2 == m:
        print(num)





# 9.46
num = int(input("Введите натуральное число: "))
while num >= 10:
    digit_sum = sum(int(d) for d in str(num))
    num = digit_sum
print("Цифровой корень:", num)





# 9.47
for bulls in range(1, 10):  # максимум 10 быков
    for cows in range(1, 20):  # максимум 20 коров
        for calves in range(1, 100):  # максимум 200 телят
            if bulls + cows + calves == 100:
                cost = bulls*10 + cows*5 + calves*0.5
                if abs(cost - 100) < 0.01:  # учитываем погрешность
                    print(f"Быков: {bulls}, коров: {cows}, телят: {calves}")







# 9.48
n = int(input("Введите число: "))
temp = n
factors = []
# 1) Каждый простой множитель один раз
divisor = 2
while temp > 1:
    if temp % divisor == 0:
        factors.append(divisor)
        while temp % divisor == 0:
            temp //= divisor
    divisor += 1
print("Простые множители (уникальные):", factors)

# 2) С учетом кратности
temp = n
factors_multi = []
divisor = 2
while temp > 1:
    while temp % divisor == 0:







# 9.49
n = int(input("Введите число: "))
print("Простые делители:", end=' ')
divisor = 2
while divisor <= n:
    if n % divisor == 0:
        # Проверяем, простой ли делитель
        is_prime = True
        for i in range(2, int(divisor**0.5)+1):
            if divisor % i == 0:
                is_prime = False
                break
        if is_prime:
            print(divisor, end=' ')
    divisor += 1
print()
        factors_multi.append(divisor)
        temp //= divisor
    divisor += 1
print("Простые множители (с кратностью):", factors_multi)






# 9.50
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Введите n: "))
print("Числа, взаимно простые с", n, ":", end=' ')
for i in range(1, n):
    if gcd(i, n) == 1:
        print(i, end=' ')
print()






# 9.51
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def task_9_51():
    n = int(input("Введите число n (натуральное): "))
    m = int(input("Введите число m (натуральное): "))
    
    result = []
    for i in range(1, n):
        if gcd(i, m) == 1:
            result.append(i)
    
    if result:
        print(f"Натуральные числа меньшие {n}, взаимно простые с {m}:")
        print(result)
    else:
        print(f"Нет натуральных чисел меньших {n}, взаимно простых с {m}")






# 9.52
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def task_9_52():
    p = int(input("Введите число p: "))
    q = int(input("Введите число q: "))
    
    result = []
    for i in range(1, q + 1):
        if q % i == 0 and gcd(i, p) == 1:
            result.append(i)
    
    if result:
        print(f"Делители числа {q}, взаимно простые с {p}:")
        print(result)
    else:
        print(f"У числа {q} нет делителей, взаимно простых с {p}")





# 9.53
def task_9_53():
    cubes = {}
    found = False
    n = 1
    
    while not found:
        for a in range(1, int(n**(1/3)) + 2):
            for b in range(a + 1, int(n**(1/3)) + 2):
                if a**3 + b**3 == n:
                    if n in cubes:
                        cubes[n].append((a, b))
                        if len(cubes[n]) == 2:
                            print(f"Наименьшее число: {n}")
                            print(f"Представления: {cubes[n][0]} и {cubes[n][1]}")
                            found = True
                    else:
                        cubes[n] = [(a, b)]
        n += 1




# 9.54
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def task_9_54():
    result = []
    for denominator in range(2, 8):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                fraction = numerator / denominator
                if fraction not in result:
                    result.append(fraction)
    
    result.sort()
    print("Несократимые дроби между 0 и 1 с знаменателем ≤ 7:")
    for fraction in result:
        for denominator in range(2, 8):
            for numerator in range(1, denominator):
                if numerator / denominator == fraction and gcd(numerator, denominator) == 1:
                    print(f"{numerator}/{denominator}")
                    break


