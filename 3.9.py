n = int(input("Введите количество секунд: "))
h = n // 3600
m = (n % 3600) // 60
s = n % 60
print(h)
print(m)
print(s)
