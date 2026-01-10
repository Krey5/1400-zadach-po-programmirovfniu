num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10

if tens == 3 or units == 3:
    print("Цифра 3 входит в число")
else:
    print("Цифра 3 не входит в число")

a = int(input("Введите цифру a: "))
if tens == a or units == a:
    print(f"Цифра {a} входит в число")
else:
    print(f"Цифра {a} не входит в число")
