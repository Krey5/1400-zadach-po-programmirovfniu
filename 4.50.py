num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10

if tens == 4 or units == 4 or tens == 7 or units == 7:
    print("В число входит цифра 4 или 7")
else:
    print("В число не входят цифры 4 и 7")

if tens == 3 or units == 3 or tens == 6 or units == 6 or tens == 9 or units == 9:
    print("В число входит цифра 3, 6 или 9")
else:
    print("В число не входят цифры 3, 6, 9")
