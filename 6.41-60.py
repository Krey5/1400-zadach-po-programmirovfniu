# 6.41
n = input("Введите число: ")
max_digit = max(n)
min_digit = min(n)
print("Максимальная цифра:", max_digit)
print("Минимальная цифра:", min_digit)



# 6.42
n = input("Введите число: ")
digits = [int(d) for d in n]
max_digit = max(digits)
min_digit = min(digits)
print("Максимальная цифра:", max_digit)
print("Минимальная цифра:", min_digit)
print("На сколько максимум больше минимума:", max_digit - min_digit)
print("Сумма максимальной и минимальной цифры:", max_digit + min_digit)



# 6.43
n = input("Введите число: ")
digits = [int(d) for d in n]
a = int(input("Введите число a: "))
if (max(digits) + min(digits)) % a == 0:
    print("Сумма макс и мин цифр кратна a")
else:
    print("Сумма макс и мин цифр не кратна a")



# 6.44
n = input("Введите число: ")
digits = [int(d) for d in n]
diff = max(digits) - min(digits)
if diff % 2 == 0:
    print("Разность макс и мин цифр четная")
else:
    print("Разность макс и мин цифр нечетная")





# 6.45
n = input("Введите число с разными цифрами: ")
digits = [int(d) for d in n]
max_digit = max(digits)
min_digit = min(digits)

# Номер от конца (справа)
index_max_end = len(n) - n.index(str(max_digit))
index_min_end = len(n) - n.index(str(min_digit))

# Номер от начала (слева)
index_max_start = n.index(str(max_digit)) + 1
index_min_start = n.index(str(min_digit)) + 1

print("Номер макс цифры от конца:", index_max_end, "от начала:", index_max_start)
print("Номер мин цифры от конца:", index_min_end, "от начала:", index_min_start)






# 6.46
n = input("Введите число с разными цифрами: ")
digits = [int(d) for d in n]
max_digit = max(digits)
min_digit = min(digits)

# Номера от конца
index_max_end = len(n) - n.index(str(max_digit))
index_min_end = len(n) - n.index(str(min_digit))

# Номера от начала
index_max_start = n.index(str(max_digit)) + 1
index_min_start = n.index(str(min_digit)) + 1

print("Номер макс от конца:", index_max_end, "от начала:", index_max_start)
print("Номер мин от конца:", index_min_end, "от начала:", index_min_start)






# 6.47
n = input("Введите число с разными цифрами: ")
digits = [int(d) for d in n]
max_digit = max(digits)
min_digit = min(digits)

index_max = n.index(str(max_digit))
index_min = n.index(str(min_digit))

if index_max < index_min:
    print("Максимальная цифра левее")
else:
    print("Минимальная цифра левее")






# 6.48
n = input("Введите число: ")
digits = [int(d) for d in n]
odd_digits = [d for d in digits if d % 2 != 0]
max_odd = max(odd_digits) if odd_digits else "нет нечетных"
print("Максимальная нечетная цифра:", max_odd)

min_digit = min(digits)
index_min = n.index(str(min_digit)) + 1
print("Номер минимальной цифры (слева направо):", index_min)






# 6.49
n = input("Введите число: ")
digits = [int(d) for d in n]
sum_digits = sum(digits)
prod_digits = 1
for d in digits:
    prod_digits *= d

# a
print("Сумма цифр > 10:", sum_digits > 10)
# б
print("Произведение цифр < 50:", prod_digits < 50)
# в
print("Количество цифр четное:", len(n) % 2 == 0)
# г
print("Число четырехзначное:", len(n) == 4)
# д
print("Первая цифра ≤ 6:", int(n[0]) <= 6)
# е
print("Начинается и заканчивается одной цифрой:", n[0] == n[-1])
# ж
print("Первая цифра больше последней:", int(n[0]) > int(n[-1]))





# 6.50
n = input("Введите число: ")
digits = [int(d) for d in n]
sum_digits = sum(digits)
prod_digits = 1
for d in digits:
    prod_digits *= d

a = int(input("Введите a: "))
b = int(input("Введите b: "))
k = int(input("Введите k (количество цифр для проверки): "))
m = int(input("Введите m: "))

print("Сумма цифр < a:", sum_digits < a)
print("Произведение цифр > b:", prod_digits > b)
print("Число k-значное:", len(n) == k)
print("Первая цифра > m:", int(n[0]) > m)






# 6.51
n = input("Введите число: ")
digits = [int(d) for d in n]
sum_digits = sum(digits)
prod_digits = 1
for d in digits:
    prod_digits *= d

k = int(input("Введите k: "))
b = int(input("Введите b: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))
a = int(input("Введите a: "))
b_div = int(input("Введите b для делимости: "))
m = int(input("Введите m: "))
n_div = int(input("Введите n для делимости: "))

# a
print("Сумма цифр > k и число четное:", sum_digits > k and int(n) % 2 == 0)
# б
print("Количество цифр четное и число ≤ b:", len(n) % 2 == 0 and int(n) <= b)
# в
print("Начинается с", x, "и заканчивается на", y, ":", n[0] == str(x) and n[-1] == str(y))
# г
print("Произведение цифр < a и число делится на b:", prod_digits < a and int(n) % b_div == 0)
# д
print("Сумма цифр > m и число делится на n:", sum_digits > m and int(n) % n_div == 0)






# 6.52
n = input("Введите число: ")
print("Есть цифра 3:", '3' in n)
print("Есть цифры 2 и 5:", '2' in n and '5' in n)





# 6.53
n = input("Введите число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
k = int(input("Введите k: "))

print("Есть цифра a:", a in n)
print("Нет цифры b:", b not in n)
print("Цифра a встречается > k раз:", n.count(a) > k)
print("Есть цифры a и b:", a in n and b in n)





# 6.54
n = input("Введите число: ")
count0 = n.count('0')
count9 = n.count('9')
if count0 > count9:
    print("Чаще встречается 0")
elif count9 > count0:
    print("Чаще встречается 9")
else:
    print("0 и 9 встречаются одинаково")







# 6.55
n = input("Введите число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
count_a = n.count(a)
count_b = n.count(b)
print("Цифра a встречается реже, чем b:", count_a < count_b)






# 6.56
n = input("Введите число: ")
index2 = n.find('2')
index5 = n.find('5')
if index2 != -1 and index5 != -1:
    if index2 < index5:
        print("Цифра 2 левее")
    else:
        print("Цифра 5 левее")
else:
    print("Одной из цифр нет")





# 6.57
n = input("Введите число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
index_a = n.rfind(a)
index_b = n.rfind(b)
if index_a != -1 and index_b != -1:
    if index_a > index_b:
        print("Цифра a правее")
    else:
        print("Цифра b правее")
else:
    print("Одной из цифр нет")





# 6.58
n = input("Введите число: ")
max_digit = max(n)
count_max = n.count(max_digit)
print("Максимальная цифра", max_digit, "встречается", count_max, "раз")





# 6.59
n = input("Введите число: ")
min_digit = min(n)
count_min = n.count(min_digit)
print("Минимальная цифра", min_digit, "встречается", count_min, "раз")





# 6.60
n = input("Введите число с разными цифрами: ")
digits = sorted(set(int(d) for d in n))
print("Две максимальные цифры:", digits[-1], digits[-2])
print("Две минимальные цифры:", digits[0], digits[1])
