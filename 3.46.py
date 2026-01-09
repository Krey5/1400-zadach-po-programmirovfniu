k = int(input("Введите k (1 ≤ k ≤ 150): "))
# Последовательность: 101102103...149150
# Каждое трехзначное число занимает 3 цифры
num_index = (k - 1) // 3  # индекс числа в последовательности (с 0)
digit_in_num = (k - 1) % 3 + 1  # 1, 2, 3
number = 101 + num_index
digit = int(str(number)[digit_in_num - 1])
print("k-я цифра:", digit)
