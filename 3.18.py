num = int(input("Двузначное число: "))
reversed_num = (num % 10) * 10 + num // 10
print("Число после перестановки:", reversed_num)
