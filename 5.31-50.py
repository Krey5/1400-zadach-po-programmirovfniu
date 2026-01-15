# 5.31
n = int(input("n: "))
total = sum((n + i) ** 2 for i in range(n + 1))
print(f"Сумма от n^2 до (2n)^2: {total}")




# 5.32
n = int(input("n: "))
total = sum(1 / i for i in range(1, n + 1))
print(f"1 + 1/2 + ... + 1/n = {total}")



# 5.33
total = sum(i / (i + 1) for i in range(2, 11))
print(f"2/3 + 3/4 + ... + 10/11 = {total}")


# 5.34
n = int(input("n: "))
total = sum(i ** 2 for i in range(1, n + 1))
print(f"1^2 + 2^2 + ... + n^2 = {total}")



# 5.35
n = int(input("n (>=2): "))
total = sum(i * (i + 1) for i in range(1, n))
print(f"1×2 + 2×3 + ... + (n-1)×n = {total}")



# 5.36
total = 1
term = 1
for _ in range(8):
    term /= 3
    total += term
print("1 + 1/3 + 1/3^2 + ... + 1/3^8 =", total)



# 5.37
n = int(input("n: "))
total = 0
sign = 1
for i in range(1, n + 1):
    total += sign / i
    sign = -sign
print(f"1 - 1/2 + 1/3 - ... + (-1)^(n+1)/n = {total}")




# 5.38
x = 2
total = 0
power = 1
for denominator in range(1, 12, 2):
    total += x ** power / denominator
    power += 2
print(f"x + x^3/3 + x^5/5 + ... + x^11/11 = {total}")




# 5.39
x = 2
total = 1
sign = -1
for i in range(2, 12):
    term = (i / (i + 1)) * (x ** (i - 1))
    total += sign * term
    sign = -sign
print(f"1 - 2/3 x + 3/4 x^2 - ... + 11/12 x^10 = {total}")



# 5.40
num = int(input("9-значное число: "))
total = 0
for _ in range(9):
    total += num % 10
    num //= 10
print("Сумма цифр:", total)




# 5.41
num = int(input("Число: "))
n = int(input("n (количество последних цифр): "))
product = 1
sum_digits = 0
for _ in range(n):
    digit = num % 10
    product *= digit
    sum_digits += digit
    num //= 10
print("Произведение последних n цифр:", product)
print("Сумма последних n цифр:", sum_digits)




# 5.42
n = 100
distance = 0
total_path = 0
for i in range(1, n + 1):
    step = 1 / i
    if i % 2 == 1:  # движение к дому
        distance += step
    else:           # движение от дома
        distance -= step
    total_path += step
print(f"После {n} этапов: расстояние от дома = {distance} км")
print(f"Общий пройденный путь = {total_path} км")




# 5.43
n = int(input("n: "))
a = [1]  # a0
for k in range(1, n + 1):
    a_k = k * a[k-1] + 1 / k
    a.append(a_k)
print("Последовательность a0..an:", a)




# 5.44
n = int(input("n (>=3): "))
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

# a) n-й член
print(f"{n}-й член Фибоначчи: {fib[n-1]}")

# б) первые n членов
print(f"Первые {n} членов: {fib[:n]}")



# 5.45
fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[-1] + fib[-2])
print("3-й..10-й члены Фибоначчи:", fib[2:10])



# 5.46
num1, den1 = 1, 1
num2, den2 = 2, 1
sequence = [(num1, den1), (num2, den2)]

k = int(input("k: "))
for i in range(2, k):
    num = num1 + num2
    den = den1 + den2
    sequence.append((num, den))
    num1, den1 = num2, den2
    num2, den2 = num, den

print(f"{k}-й член: {sequence[k-1][0]}/{sequence[k-1][1]}")

n = int(input("n: "))
print(f"Первые {n} членов:")
for i in range(n):
    print(f"{sequence[i][0]}/{sequence[i][1]}")


# 5.47
n = int(input("n (>=4): "))
v = [0, 0, 1.5]  # v1, v2, v3
for i in range(4, n + 1):
    v_i = ((i - 1) / (i ** 2 + 1)) * v[-1] - v[-2] + v[-3]
    v.append(v_i)
print(f"v_{n} = {v[n]}")



# 5.48
cells = 1
for hour in range(3, 25, 3):
    cells *= 2
    print(f"Через {hour} часов: {cells} клеток")






# 5.49
deposit = 1000
rate = 0.02
print("Прирост за месяц:")
for month in range(1, 11):
    increase = deposit * rate
    deposit += increase
    print(f"Месяц {month}: +{increase:.2f} руб")

deposit = 1000
print("\nСумма вклада:")
for month in range(3, 13):
    deposit *= 1.02
    if month >= 3:
        print(f"Через {month} месяцев: {deposit:.2f} руб")





# 5.50
distance = 10
print("Пробег по дням:")
for day in range(2, 11):
    distance *= 1.1
    print(f"День {day}: {distance:.2f} км")

distance = 10
total = distance
for day in range(2, 8):
    distance *= 1.1
    total += distance
print(f"\nСуммарный путь за 7 дней: {total:.2f} км")
