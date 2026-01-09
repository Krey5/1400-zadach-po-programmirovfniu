num = int(input("Трехзначное число: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
new_num = a * 100 + c * 10 + b
print("Новое число:", new_num)
