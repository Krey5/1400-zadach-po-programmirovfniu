# 4.121
x = float(input("Введите x: "))
y = float(input("Введите y: "))

if x < 1:
    region = "I"
elif x < 5:
    region = "II"
else:
    region = "III"
print("Точка попадает в область:", region)



# 4.122
x = float(input("Введите x: "))
y = float(input("Введите y: "))

if y > 5.0:
    region = "I"
elif y > 2.5:
    region = "II"
else:
    region = "III"
print("Точка попадает в область:", region)



# 4.123
points = int(input("Количество очков: "))

if points == 3:
    result = "выигрыш"
elif points == 1:
    result = "ничья"
else:
    result = "проигрыш"
print("Результат игры:", result)




# 4.124
age_mitya = int(input("Возраст Мити: "))
age_vasya = int(input("Возраст Васи: "))

if age_mitya > age_vasya:
    print("Митя старше")
elif age_vasya > age_mitya:
    print("Вася старше")
else:
    print("Они одного возраста")




# 4.125
weight = float(input("Вес боксера (кг): "))

if weight < 60:
    category = "легкий вес"
elif weight < 64:
    category = "первый полусредний вес"
elif weight < 69:
    category = "полусредний вес"
else:
    category = "тяжелее полусреднего"
print("Категория:", category)




# 4.126
a = int(input("a (не ноль): "))
b = int(input("b (не ноль): "))

if a % b == 0:
    print(f"{a} делитель {b}")
elif b % a == 0:
    print(f"{b} делитель {a}")
else:
    print("Ни одно число не является делителем другого")




# 4.127
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

# a) Самое большое
if a >= b and a >= c:
    print("Самое большое: первое")
elif b >= a and b >= c:
    print("Самое большое: второе")
else:
    print("Самое большое: третье")

# б) Самое маленькое
if a <= b and a <= c:
    print("Самое маленькое: первое")
elif b <= a and b <= c:
    print("Самое маленькое: второе")
else:
    print("Самое маленькое: третье")

# в) Среднее
if (b <= a <= c) or (c <= a <= b):
    print("Среднее: первое")
elif (a <= b <= c) or (c <= b <= a):
    print("Среднее: второе")
else:
    print("Среднее: третье")




# 4.128
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

maximum = max(a, b, c)
minimum = min(a, b, c)
print("Максимум:", maximum, "Минимум:", minimum)




# 4.129
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

# Сумма двух наибольших
sorted_nums = sorted([a, b, c])
sum_two_largest = sorted_nums[1] + sorted_nums[2]
print("Сумма двух наибольших:", sum_two_largest)



# 4.130
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

# Произведение двух наименьших
sorted_nums = sorted([a, b, c])
product_two_smallest = sorted_nums[0] * sorted_nums[1]
print("Произведение двух наименьших:", product_two_smallest)
