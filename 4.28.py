num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10
digit_sum = tens + units

if digit_sum > 9:
    print("Сумма цифр — двузначное число")
else:
    print("Сумма цифр — не двузначное число")

a = int(input("Введите число a: "))
if digit_sum > a:
    print("Сумма цифр больше a")
else:
    print("Сумма цифр не больше a")
