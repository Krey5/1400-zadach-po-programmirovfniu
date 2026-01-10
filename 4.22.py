m = int(input("m: "))
n = int(input("n: "))

if m % n == 0:
    print("Частное:", m // n)
else:
    print(f"{m} на {n} нацело не делится")
