# 5.51
area = 100
yield_per_ha = 20
print("Урожайность по годам:")
for year in range(2, 9):
    yield_per_ha *= 1.02
    print(f"Год {year}: {yield_per_ha:.2f} ц/га")

area = 100
print("\nПлощадь участка:")
for year in range(4, 8):
    area *= 1.05
    print(f"Год {year}: {area:.2f} га")

area = 100
yield_per_ha = 20
total_harvest = 0
for year in range(1, 7):
    total_harvest += area * yield_per_ha
    area *= 1.05
    yield_per_ha *= 1.02
print(f"\nУрожай за 6 лет: {total_harvest:.2f} ц")




# 5.52
import math
thickness = 0.5  # см
inner_diameter = 10  # см
total_volume = 0
for i in range(12):
    radius = (inner_diameter + i * thickness * 2) / 2
    volume = (4/3) * math.pi * radius ** 3
    total_volume += volume
    inner_diameter += thickness * 2
print(f"Суммарный объем 12 шаров: {total_volume:.2f} см³")



# 5.53
total = 0
power = 2
for _ in range(2, 11):
    total += power
    power *= 2
print("2^2 + 2^3 + ... + 2^10 =", total)




# 5.54
a = float(input("a: "))
n = int(input("n: "))
result = 1
for i in range(1, n + 1):
    result *= a
    print(f"a^{i} = {result}")




# 5.56
import math
# Приближенное вычисление интеграла sin(x) от 0 до π
n = 1000
step = math.pi / n
area = 0
for i in range(n):
    x = i * step
    area += math.sin(x) * step
print(f"Площадь одной арки синусоиды ≈ {area:.4f}")




# 5.57
# Площадь под кривой y = 0.3(x-1)^2 + 3 от x=2 до x=4
n = 1000
x_start = 2
x_end = 4
step = (x_end - x_start) / n
area = 0
for i in range(n):
    x = x_start + i * step
    y = 0.3 * (x - 1) ** 2 + 3
    area += y * step
print(f"Площадь фигуры ≈ {area:.4f}")




# 5.58
# Площадь под кривой y = 0.4(x+2)^2 + 1 от x=0 до x=2
n = 1000
x_start = 0
x_end = 2
step = (x_end - x_start) / n
area = 0
for i in range(n):
    x = x_start + i * step
    y = 0.4 * (x + 2) ** 2 + 1
    area += y * step
print(f"Площадь фигуры ≈ {area:.4f}")



# 5.59
n = int(input("n: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")




# 5.60
n = int(input("Целое число n: "))
a = float(input("Вещественное число a: "))
product = 0
for _ in range(abs(n)):
    product += a
if n < 0:
    product = -product
print(f"{a} * {n} = {product}")
