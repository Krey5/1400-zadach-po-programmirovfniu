# 6.21
n = int(input("n (>9): "))
while n >= 100:
    n //= 10
second_digit = n % 10
print("Вторая цифра:", second_digit)





# 6.22
n = int(input("n (>99): "))
while n >= 1000:
    n //= 10
third_digit = n % 10
print("Третья цифра:", third_digit)





# 6.23
num = int(input("Число: "))
m = int(input("m: "))
sum_last = 0
for _ in range(m):
    if num == 0:
        break
    sum_last += num % 10
    num //= 10
print("Сумма последних m цифр:", sum_last)





# 6.24
num = int(input("Число: "))
sign = 1
sum_a = 0
sum_b = 0
while num > 0:
    digit = num % 10
    sum_a += sign * digit
    sum_b += digit * sign
    sign = -sign
    num //= 10
print("Сумма a):", sum_a)
print("Сумма б):", sum_b)





# 6.25
n = int(input("Натуральное число: "))
divisor = 2
while n % divisor != 0:
    divisor += 1
print("Наименьший делитель >1:", divisor)




# 6.26
# a) Без условия
for i in range(13, 100, 13):
    print(i)

# б) С условием
num = 13
while num < 100:
    print(num)
    num += 13




# 6.27
count = 0
num = 100
while count < 15:
    if num % 19 == 0:
        print(num)
        count += 1
    num += 1





# 6.28
count = 0
num = 500
while count < 20:
    if num % 13 == 0 or num % 17 == 0:
        print(num)
        count += 1
    num += 1





# 6.29
count = 0
num = 100
while count < 10:
    if num % 10 == 7 and num % 9 == 0:
        print(num)
        count += 1
    num += 1






# 6.30
a = int(input("a: "))
b = int(input("b: "))

# a) Целочисленное деление
quotient = 0
temp = abs(b)
while temp >= abs(a):
    temp -= abs(a)
    quotient += 1
if (a < 0) != (b < 0):
    quotient = -quotient
print(f"{b} // {a} = {quotient}")

# б) Остаток
remainder = abs(b)
while remainder >= abs(a):
    remainder -= abs(a)
if b < 0:
    remainder = -remainder
print(f"{b} % {a} = {remainder}")
