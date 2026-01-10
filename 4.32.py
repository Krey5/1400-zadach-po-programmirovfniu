num = int(input("Трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if num ** 2 == hundreds ** 3 + tens ** 3 + units ** 3:
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")
