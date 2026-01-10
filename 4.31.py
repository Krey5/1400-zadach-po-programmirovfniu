num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if hundreds > units:
    print("Первая цифра больше последней")
elif units > hundreds:
    print("Последняя цифра больше первой")

if hundreds > tens:
    print("Первая цифра больше второй")
elif tens > hundreds:
    print("Вторая цифра больше первой")

if tens > units:
    print("Вторая цифра больше последней")
elif units > tens:
    print("Последняя цифра больше второй")
