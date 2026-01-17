# 9.1 а)
for _ in range(5):
    print("8 8 8")

# б)
for i in range(1, 8):
    print(f"{i} {i} {i} {i} {i}")

# в)
for i in range(1, 9):
    print(f"{i*10} {i*10} {i*10} {i*10}")

# г)
for i in range(1, 9):
    print(f"{i*10+2} {i*10+2} {i*10+2} {i*10+2}")

# д)
for _ in range(5):
    for j in range(2, 21):
        print(j, end=' ')
    print()

# е)
for _ in range(4):
    for j in range(15, 2, -1):
        print(j, end=' ')
    print()

#ж)
for i in range(5, 0, -1):
    print("0 " * i)

# з)
for i in range(8, 0, -1):
    for j in range(8, 8-i, -1):
        print(j, end=' ')
    print()

# и)
for i in range(2, 10):
    for j in range(i, 11):
        print(j, end=' ')
    print()

# й)
for i in range(1, 10):
    for j in range(2, 2+i):
        print(j, end=' ')
    print()

# к)
for i in range(3, 7):
    print(f"{i} " * i)

# л)
for i in range(1, 6):
    print(f"{20+i} " * i)

# м)
for i in range(1, 6):
    print(f"{i} " * (9 - i))

# н)
for i in range(1, 6):
    print(f"{i*10} " * i)

# о)
for i in range(5, 10):
    print(f"{i} " * (10 - i))

# п)
for i in range(1, 6):
    print(f"{i*5} " * (6 - i))

# р)
for i in range(0, 7):
    for j in range(1, 6):
        print(f"{100 + i*10 + j}", end=' ')
    print()

# с)
for i in range(5, 0, -1):
    for j in range(1, 5):
        print(f"{i*10 + j}", end=' ')
    print()




# 9.2 а)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} + {i} = {j+i}", end='   ')
    print()

# б)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} + {j} = {i+j}", end='   ')
    print()




# 9.3 а)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end='   ')
    print()

# б)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} * {i} = {j*i}", end='   ')
    print()



# 9.4
# 1) По строкам
total = 0
for student in range(12):
    for subject in range(3):
        grade = int(input(f"Оценка ученика {student+1} по предмету {subject+1}: "))
        total += grade
print("Сумма всех оценок:", total)

# 2) По столбцам
total = 0
for subject in range(3):
    for student in range(12):
        grade = int(input(f"Оценка по предмету {subject+1} ученика {student+1}: "))
        total += grade
print("Сумма всех оценок:", total)





# 9.5
# Ввод данных
salaries = []
for worker in range(12):
    row = []
    for month in range(3):
        salary = float(input(f"Зарплата работника {worker+1} за месяц {month+1}: "))
        row.append(salary)
    salaries.append(row)

# а) Общая сумма за квартал всем работникам
total_all = sum(sum(row) for row in salaries)
print("Общая сумма за квартал:", total_all)

# б) Зарплата за квартал каждого работника
for i, row in enumerate(salaries, start=1):
    print(f"Работник {i}: {sum(row)}")

# в) Общая зарплата всех работников за каждый месяц
for month in range(3):
    month_total = sum(salaries[worker][month] for worker in range(12))
    print(f"Месяц {month+1}: {month_total}")





# 9.6
scores = []
for athlete in range(15):
    row = []
    for program in range(3):
        score = float(input(f"Баллы спортсмена {athlete+1} за программу {program+1}: "))
        row.append(score)
    scores.append(row)

# а) Среднее каждого спортсмена
for i, row in enumerate(scores, start=1):
    avg = sum(row) / len(row)
    print(f"Спортсмен {i}: среднее {avg:.2f}")

# б) Среднее по каждому виду программы
for program in range(3):
    program_scores = [scores[athlete][program] for athlete in range(15)]
    avg = sum(program_scores) / len(program_scores)
    print(f"Программа {program+1}: среднее {avg:.2f}")






# 9.7
grades = []
for student in range(15):
    row = []
    for subject in range(3):
        grade = int(input(f"Оценка ученика {student+1} по предмету {subject+1}: "))
        row.append(grade)
    grades.append(row)

# а) Общее количество пятерок
count_5 = sum(grade == 5 for row in grades for grade in row)
print("Пятерок в таблице:", count_5)

# б) Количество троек у каждого ученика
for i, row in enumerate(grades, start=1):
    count_3 = sum(grade == 3 for grade in row)
    print(f"Ученик {i}: троек - {count_3}")

# в) Количество двоек по каждому предмету
for subject in range(3):
    count_2 = sum(grades[student][subject] == 2 for student in range(15))
    print(f"Предмет {subject+1}: двоек - {count_2}")






# 9.8
grades = []
for student in range(14):
    row = []
    for subject in range(3):
        grade = int(input(f"Оценка студента {student+1} по предмету {subject+1}: "))
        row.append(grade)
    grades.append(row)

# а) Студенты без двоек
no_2_count = sum(2 not in row for row in grades)
print("Студентов без двоек:", no_2_count)

# б) Предметы, где только 5 и 4
for subject in range(3):
    subject_grades = [grades[student][subject] for student in range(14)]
    if all(g in (4, 5) for g in subject_grades):
        print(f"Предмет {subject+1}: только 5 и 4")

# в) Количество двоек по каждому предмету
for subject in range(3):
    count_2 = sum(grades[student][subject] == 2 for student in range(14))
    print(f"Предмет {subject+1}: двоек - {count_2}")






# 9.9
scores = []
for athlete in range(8):
    row = []
    for sport in range(5):
        score = int(input(f"Баллы спортсмена {athlete+1} в виде спорта {sport+1}: "))
        row.append(score)
    scores.append(row)

# а) Максимальная оценка в таблице
max_score = max(max(row) for row in scores)
print("Максимальный балл:", max_score)

# б) Сумма баллов победителя
winner_total = max(sum(row) for row in scores)
print("Баллы победителя:", winner_total)





# 9.10
salaries = []
for worker in range(12):
    row = []
    for month in range(3):
        salary = float(input(f"Зарплата работника {worker+1} за месяц {month+1}: "))
        row.append(salary)
    salaries.append(row)

# а) Максимальная зарплата
max_salary = max(max(row) for row in salaries)
print("Максимальная зарплата:", max_salary)

# б) Работник с наибольшей суммой за квартал
worker_totals = [sum(row) for row in salaries]
best_worker = worker_totals.index(max(worker_totals)) + 1
print(f"Работник с наибольшей суммой: №{best_worker}")

# в) Месяц с максимальной общей зарплатой
month_totals = [sum(salaries[worker][month] for worker in range(12)) for month in range(3)]
best_month = month_totals.index(max(month_totals)) + 1
print(f"Месяц с максимальной общей зарплатой: {best_month}")
