k = int(input("Введите k (1 ≤ k ≤ 180): "))
# Последовательность: 10 11 12 ... 99
# Каждое двузначное число занимает 2 цифры
pair_num = (k + 1) // 2  # номер пары (двузначного числа)
digit_in_pair = 2 - (k % 2) if k % 2 != 0 else 2  # 1 — первая цифра, 2 — вторая цифра
two_digit_num = 9 + pair_num  # 10 → 9+1, 11 → 9+2, ...
if digit_in_pair == 1:
    digit = two_digit_num // 10
else:
    digit = two_digit_num % 10

print("Номер пары:", pair_num)
print("Двузначное число:", two_digit_num)
print("k-я цифра:", digit)
