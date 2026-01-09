num = int(input("Четырехзначное число: "))
# a)
reversed_num = int(str(num)[::-1])
print("Справа налево:", reversed_num)

# б)
s = str(num)
swapped = s[1] + s[0] + s[3] + s[2]
print("После перестановки пар:", swapped)

# в)
swapped2 = s[0] + s[2] + s[1] + s[3]
print("После перестановки 2-й и 3-й цифр:", swapped2)

# г)
swapped3 = s[2] + s[3] + s[0] + s[1]
print("После перестановки двух пар:", swapped3)
