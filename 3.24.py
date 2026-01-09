num = int(input("Трехзначное число: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
new_num = b * 100 + a * 10 + c
print("Новое число:", new_num)
