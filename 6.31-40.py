# 6.31
deposit = 1000
month = 0
increase = 0
while increase <= 30:
    month += 1
    increase = deposit * 0.02
    deposit += increase
print(f"На {month}-м месяце увеличение превысит 30 руб.")

deposit = 1000
month = 0
while deposit <= 1200:
    month += 1
    deposit *= 1.02
print(f"Через {month} месяцев вклад превысит 1200 руб.")




# 6.32
distance = 10
day = 1
while distance <= 20:
    day += 1
    distance *= 1.1
print(f"На {day}-й день пробег >20 км")

distance = 10
total = distance
day = 1
while total <= 100:
    day += 1
    distance *= 1.1
    total += distance
print(f"На {day}-й день суммарный пробег >100 км")




# 6.33
area = 100
yield_per_ha = 20
year = 1
while yield_per_ha <= 22:
    year += 1
    yield_per_ha *= 1.02
print(f"В {year}-м году урожайность >22 ц/га")

area = 100
year = 1
while area <= 120:
    year += 1
    area *= 1.05
print(f"В {year}-м году площадь >120 га")

area = 100
yield_per_ha = 20
total = 0
year = 1
while total <= 800:
    total += area * yield_per_ha
    year += 1
    area *= 1.05
    yield_per_ha *= 1.02
print(f"В {year}-м году общий урожай >800 ц")





# 6.34
m = int(input("m: "))
n = int(input("n: "))
limit = m * n
multiple_m = m
multiple_n = n
while multiple_m <= limit or multiple_n <= limit:
    if multiple_m < multiple_n:
        print(multiple_m)
        multiple_m += m
    elif multiple_n < multiple_m:
        print(multiple_n)
        multiple_n += n
    else:
        print(multiple_m)
        multiple_m += m
        multiple_n += n






# 6.35
num = int(input("Число: "))
temp = num

# a) Количество цифр 3
count_3 = 0
# б) Сколько раз встречается последняя цифра
last_digit = num % 10
count_last = 0
# в) Количество четных цифр
count_even = 0
# г) Сумма цифр >5
sum_gt5 = 0
# д) Произведение цифр >7
product_gt7 = 1
has_gt7 = False
# е) Сколько раз встречаются цифры 0 и 5
count_0_5 = 0

while temp > 0:
    digit = temp % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_gt5 += digit
    if digit > 7:
        product_gt7 *= digit
        has_gt7 = True
    if digit == 0 or digit == 5:
        count_0_5 += 1
    temp //= 10

if not has_gt7:
    product_gt7 = 0

print("Цифр 3:", count_3)
print(f"Цифра {last_digit} встречается:", count_last, "раз")
print("Четных цифр:", count_even)
print("Сумма цифр >5:", sum_gt5)
print("Произведение цифр >7:", product_gt7)
print("Цифр 0 и 5:", count_0_5)





# 6.36
num = int(input("Число: "))
a = int(input("a (0-8): "))
x = int(input("x: "))
y = int(input("y: "))

temp = num
count_a = 0
sum_gt_a = 0
sum_even = 0
count_xy = 0

while temp > 0:
    digit = temp % 10
    if digit == a:
        count_a += 1
    if digit > a:
        sum_gt_a += digit
    if digit % 2 == 0:
        sum_even += digit
    if digit == x or digit == y:
        count_xy += 1
    temp //= 10

print(f"Цифра {a} встречается:", count_a, "раз")
print(f"Сумма цифр >{a}:", sum_gt_a)
print("Сумма четных цифр:", sum_even)
print(f"Цифры {x} и {y} встречаются:", count_xy, "раз")





# 6.37
num = int(input("Число: "))
digit = 8
position = 0
found = False
temp = num

while temp > 0:
    position += 1
    if temp % 10 == digit:
        found = True
        break
    temp //= 10

if found:
    print(f"Цифра {digit} на позиции {position} с конца")
else:
    print("0")





# 6.38
num = int(input("Число: "))
digit = 3
position = 0
last_position = 0
temp = num

while temp > 0:
    position += 1
    if temp % 10 == digit:
        last_position = position
    temp //= 10

print(f"Самая правая цифра {digit} на позиции {last_position} с конца")





# 6.39
num = int(input("Число: "))
# Переворачиваем число для вывода с первой цифры
reversed_num = 0
temp = num
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10

while reversed_num > 0:
    print(reversed_num % 10)
    reversed_num //= 10





# 6.40
num = int(input("Число: "))
first_digit = int(str(num)[0])
count = 0
temp = num

while temp > 0:
    if temp % 10 == first_digit:
        count += 1
    temp //= 10

print(f"Первая цифра {first_digit} встречается {count} раз")
