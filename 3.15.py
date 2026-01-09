n = int(input("Номер места: "))
section = (n - 1) // (10 * 15) + 1
tier = ((n - 1) % (10 * 15)) // 15 + 1
print("Секция:", section, "Ярус:", tier)
