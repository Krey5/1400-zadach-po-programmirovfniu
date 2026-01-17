# 9.11
salaries = []
for worker in range(12):
    row = []
    for month in range(3):
        salary = float(input(f"Зарплата работника {worker+1} за месяц {month+1}: "))
        row.append(salary)
    salaries.append(row)

# а) Для каждого работника — месяц с наибольшей зарплатой
for i, row in enumerate(salaries, start=1):
    best_month = row.index(max(row)) + 1
    print(f"Работник {i}: лучший месяц {best_month}")

# б) Для каждого месяца — работник с наибольшей зарплатой
for month in range(3):
    month_salaries = [salaries[worker][month] for worker in range(12)]
    best_worker = month_salaries.index(max(month_salaries)) + 1
    print(f"Месяц {month+1}: лучший работник {best_worker}")




# 9.12
# Ввод данных
students = []
for grade in range(11):
    row = []
    for class_letter in range(4):
        count = int(input(f"Учеников в {grade+1} классе, буква {chr(65+class_letter)}: "))
        row.append(count)
    students.append(row)

# а) Самый малочисленный класс в школе
min_class = min(min(row) for row in students)
print("Самый малочисленный класс:", min_class, "учеников")

# б) Минимальное общее количество учеников в одной параллели
min_parallel = min(sum(row) for row in students)
print("Минимальное количество в параллели:", min_parallel)

# в) Минимальное общее количество учеников в классах А, Б, В, Г
class_totals = [sum(students[grade][letter] for grade in range(11)) for letter in range(4)]
min_class_total = min(class_totals)
print("Минимальное количество в букве:", min_class_total)






# 9.13
students = []
for grade in range(11):
    row = []
    for class_letter in range(4):
        count = int(input(f"Учеников в {grade+1} классе, буква {chr(65+class_letter)}: "))
        row.append(count)
    students.append(row)

# а) Самый малочисленный класс в каждой параллели
for grade, row in enumerate(students, start=1):
    min_in_grade = min(row)
    print(f"{grade} класс: самый маленький класс - {min_in_grade} учеников")

# б) Самый малочисленный класс среди каждой буквы
for letter in range(4):
    letter_counts = [students[grade][letter] for grade in range(11)]
    min_letter = min(letter_counts)
    print(f"Буква {chr(65+letter)}: самый маленький класс - {min_letter} учеников")




# 9.14
income = []
for shop in range(3):
    row = []
    for day in range(10):
        profit = float(input(f"Доход магазина {shop+1} за день {day+1}: "))
        row.append(profit)
    income.append(row)

# а) Магазин с максимальным общим доходом
shop_totals = [sum(row) for row in income]
best_shop = shop_totals.index(max(shop_totals)) + 1
print(f"Магазин с максимальным доходом: №{best_shop}")

# б) День с максимальным общим доходом фирмы
day_totals = [sum(income[shop][day] for shop in range(3)) for day in range(10)]
best_day = day_totals.index(max(day_totals)) + 1
print(f"День с максимальным доходом фирмы: {best_day}")

# в) Магазин и день с максимальным дневным доходом
max_daily = 0
best_shop_day = (0, 0)
for shop in range(3):
    for day in range(10):
        if income[shop][day] > max_daily:
            max_daily = income[shop][day]
            best_shop_day = (shop+1, day+1)
print(f"Максимальный дневной доход: магазин {best_shop_day[0]}, день {best_shop_day[1]}")





# 9.15
income = []
for shop in range(3):
    row = []
    for day in range(10):
        profit = float(input(f"Доход магазина {shop+1} за день {day+1}: "))
        row.append(profit)
    income.append(row)

# а) Для каждого магазина — день с максимальным доходом
for shop, row in enumerate(income, start=1):
    best_day = row.index(max(row)) + 1
    print(f"Магазин {shop}: лучший день {best_day}")

# б) Для каждого дня — магазин с максимальным доходом
for day in range(10):
    day_incomes = [income[shop][day] for shop in range(3)]
    best_shop = day_incomes.index(max(day_incomes)) + 1
    print(f"День {day+1}: лучший магазин {best_shop}")





# 9.16
students = []
for year in range(5):
    row = []
    for group in range(6):
        count = int(input(f"Студентов на курсе {year+1}, группа {group+1}: "))
        row.append(count)
    students.append(row)

# а) Курс с наименьшим количеством студентов
year_totals = [sum(row) for row in students]
min_year = year_totals.index(min(year_totals)) + 1
print(f"Наименьшее количество студентов на курсе: {min_year}")

# б) Самая малочисленная группа (курс и номер)
min_count = float('inf')
min_group_info = (0, 0)
for year, row in enumerate(students, start=1):
    for group, count in enumerate(row, start=1):
        if count < min_count:
            min_count = count
            min_group_info = (year, group)
print(f"Самая малочисленная группа: курс {min_group_info[0]}, группа {min_group_info[1]}")

# в) Самая малочисленная группа на каждом курсе
for year, row in enumerate(students, start=1):
    min_in_year = min(row)
    group_num = row.index(min_in_year) + 1
    print(f"Курс {year}: самая маленькая группа {group_num} ({min_in_year} чел.)")




# 9.17
prices = [float(input(f"Стоимость товара вида {i+1}: ")) for i in range(5)]
quantities = []
for product in range(5):
    row = []
    for day in range(6):
        qty = int(input(f"Продано товара вида {product+1} за день {day+1}: "))
        row.append(qty)
    quantities.append(row)

# а) Общий доход от каждого вида товара
for i in range(5):
    total_qty = sum(quantities[i])
    revenue = total_qty * prices[i]
    print(f"Товар {i+1}: доход {revenue}")

# б) Общий доход за каждый день
for day in range(6):
    day_revenue = sum(quantities[product][day] * prices[product] for product in range(5))
    print(f"День {day+1}: доход {day_revenue}")

# в) Общий доход магазина за 6 дней
total_revenue = sum(
    quantities[product][day] * prices[product]
    for product in range(5)
    for day in range(6)
)
print("Общий доход за 6 дней:", total_revenue)

# г) Вид товара с максимальным общим доходом
product_revenues = [
    sum(quantities[product][day] for day in range(6)) * prices[product]
    for product in range(5)
]
best_product = product_revenues.index(max(product_revenues)) + 1
print(f"Товар с максимальным доходом: вид {best_product}")

# д) День с максимальным общим доходом
day_revenues = [
    sum(quantities[product][day] * prices[product] for product in range(5))
    for day in range(6)
]
best_day = day_revenues.index(max(day_revenues)) + 1
print(f"День с максимальным доходом: {best_day}")

# е) Количество дней, в которые доход превысил a
a = float(input("Введите порог a: "))
count_days_above_a = sum(1 for revenue in day_revenues if revenue > a)
print(f"Дней с доходом > {a}: {count_days_above_a}")









# 9.18
group_scores = []
for group in range(3):
    scores = []
    for student in range(20):
        for exam in range(3):
            grade = int(input(f"Группа {group+1}, студент {student+1}, экзамен {exam+1}: "))
            scores.append(grade)
    group_scores.append(scores)

# Средний балл каждой группы
averages = [sum(scores) / len(scores) for scores in group_scores]
best_group = averages.index(max(averages)) + 1
print(f"Лучшая группа по среднему баллу: №{best_group}")






# 9.19
def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

for num in range(120, 141):
    print(f"Число {num}: {count_divisors(num)} делителей")






# 9.20
n = int(input("Введите n: "))
for num in range(1, n+1):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    print(f"{num} {'+' * divisors}")

