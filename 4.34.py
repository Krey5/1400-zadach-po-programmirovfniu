num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if hundreds == tens == units:
    print("Все цифры одинаковые")
else:
    print("Не все цифры одинаковые")

if hundreds == tens or tens == units or hundreds == units:
    print("Есть одинаковые цифры")
else:
    print("Нет одинаковых цифр")
