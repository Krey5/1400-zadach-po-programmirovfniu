# Даны цифры трехзначного a3 a2 a1 и двузначного b2 b1, сумма — трехзначное число
a3 = int(input("Сотни трехзначного: "))
a2 = int(input("Десятки трехзначного: "))
a1 = int(input("Единицы трехзначного: "))
b2 = int(input("Десятки двузначного: "))
b1 = int(input("Единицы двузначного: "))

sum_units = (a1 + b1) % 10
carry = (a1 + b1) // 10
sum_tens = (a2 + b2 + carry) % 10
carry2 = (a2 + b2 + carry) // 10
sum_hundreds = a3 + carry2

print("Цифры суммы (сотни, десятки, единицы):", sum_hundreds, sum_tens, sum_units)
