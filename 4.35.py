num = int(input("Четырехзначное число: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

if d1 + d2 == d3 + d4:
    print("Сумма первых двух цифр равна сумме последних двух")
else:
    print("Суммы не равны")

digit_sum = d1 + d2 + d3 + d4
if digit_sum % 3 == 0:
    print("Сумма цифр кратна 3")
else:
    print("Сумма цифр не кратна 3")

digit_product = d1 * d2 * d3 * d4
if digit_product % 4 == 0:
    print("Произведение цифр кратно 4")
else:
    print("Произведение цифр не кратно 4")

a = int(input("Введите число a: "))
if digit_product % a == 0:
    print(f"Произведение цифр кратно {a}")
else:
    print(f"Произведение цифр не кратно {a}")
