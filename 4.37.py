a = int(input("a: "))
b = int(input("b: "))

if a % b == 0:
    print(f"{a} делитель {b}")
else:
    print(f"{a} не делитель {b}")

if b % a == 0:
    print(f"{b} делитель {a}")
else:
    print(f"{b} не делитель {a}")
