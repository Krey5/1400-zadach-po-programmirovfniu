num = int(input("Трехзначное число: "))
units = num % 10
tens = (num // 10) % 10
hundreds = num // 100
sum_digits = units + tens + hundreds
product = units * tens * hundreds
print("Единицы:", units, "Десятки:", tens, "Сумма:", sum_digits, "Произведение:", product)
