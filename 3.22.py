num = int(input("Трехзначное число: "))
first = num // 100
rest = num % 100
new_num = rest * 10 + first
print("Новое число:", new_num)
