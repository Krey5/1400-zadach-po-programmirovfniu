num = int(input("Трехзначное число: "))
hundreds = num // 100
units = num % 10

if hundreds == units:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
