monitor = float(input("Стоимость монитора: "))
system_unit = float(input("Стоимость системного блока: "))
keyboard = float(input("Стоимость клавиатуры: "))
mouse = float(input("Стоимость мыши: "))

one_pc = monitor + system_unit + keyboard + mouse

three_pc = one_pc * 3
print(three_pc)

n = int(input("Введите количество компьютеров: "))
n_pc = one_pc * n
print(n_pc)
