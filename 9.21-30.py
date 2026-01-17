# 9.21
for num in range(1, 301):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    if divisors == 5:
        print(num)





# 9.22
for num in range(200, 501):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    if divisors == 6:
        print(num)





# 9.23
a = int(input("a: "))
b = int(input("b: "))
k = int(input("k: "))
for num in range(a, b+1):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    if divisors == k:
        print(num)






# 9.24
a = int(input("a: "))
b = int(input("b: "))
max_divisors = 0
best_numbers = []
for num in range(a, b+1):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    if divisors > max_divisors:
        max_divisors = divisors
        best_numbers = [num]
    elif divisors == max_divisors:
        best_numbers.append(num)

print("Числа с максимальным количеством делителей:", best_numbers)
print("а) Максимальное из них:", max(best_numbers))
print("б) Минимальное из них:", min(best_numbers))






# 9.25
for num in range(100, 1000):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)





# 9.26
count = 0
num = 2
while count < 100:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1





# 9.27
for num in range(50, 71):
    divisor_sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisor_sum += i
    print(f"Число {num}: сумма делителей {divisor_sum}")





# 9.28
for num in range(100, 301):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == 50:
        print(num)





# 9.29
for num in range(300, 601):
    divisor_sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum % 10 == 0:
        print(num)





# 9.30
for num in range(100, 1000):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(num)
        break  # Первое совершенное число
