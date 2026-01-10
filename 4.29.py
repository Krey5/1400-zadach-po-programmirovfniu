num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10
digit_sum = tens + units

if digit_sum % 3 == 0:
    print("Сумма цифр кратна трем")
else:
    print("Сумма цифр не кратна трем")

a = int(input("Введите число a: "))
if digit_sum % a == 0:
    print(f"Сумма цифр кратна {a}")
else:
    print(f"Сумма цифр не кратна {a}")
