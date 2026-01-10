num = int(input("Двузначное число: "))
tens = num // 10
units = num % 10

if num ** 2 == 4 * (tens ** 3 + units ** 3):
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")
