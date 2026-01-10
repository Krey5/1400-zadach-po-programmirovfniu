num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10

if tens > units:
    print("Первая цифра больше")
elif units > tens:
    print("Вторая цифра больше")
else:
    print("Цифры одинаковы")
