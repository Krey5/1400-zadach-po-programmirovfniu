num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

digit_sum = hundreds + tens + units
digit_product = hundreds * tens * units

if 10 <= digit_sum <= 99:
    print("Сумма цифр — двузначное число")
else:
    print("Сумма цифр — не двузначное число")

if 100 <= digit_product <= 999:
    print("Произведение цифр — трехзначное число")
else:
    print("Произведение цифр — не трехзначное число")

a = int(input("Введите число a: "))
if digit_product > a:
    print("Произведение цифр больше a")
else:
    print("Произведение цифр не больше a")

if digit_sum % 5 == 0:
    print("Сумма цифр кратна 5")
else:
    print("Сумма цифр не кратна 5")

if digit_sum % a == 0:
    print(f"Сумма цифр кратна {a}")
else:
    print(f"Сумма цифр не кратна {a}")
