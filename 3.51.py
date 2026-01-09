a = int(input("a: "))
b = int(input("b: "))
# Если a делится на b или b делится на a → вывести 1, иначе любое другое
result = 1 if (a % b == 0) or (b % a == 0) else 0
print(result)
