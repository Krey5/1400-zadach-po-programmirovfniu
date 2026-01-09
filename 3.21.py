num = int(input("Трехзначное число: "))
reversed_num = (num % 10) * 100 + ((num // 10) % 10) * 10 + num // 100
print("Число справа налево:", reversed_num)
