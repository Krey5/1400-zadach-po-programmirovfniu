num = int(input("Трехзначное число: "))
last = num % 10
rest = num // 10
new_num = last * 100 + rest
print("Новое число:", new_num)
