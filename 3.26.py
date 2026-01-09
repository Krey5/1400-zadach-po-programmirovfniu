from itertools import permutations
num = input("Трехзначное число с разными цифрами: ")
perms = set(permutations(num))
for p in perms:
    print(''.join(p))
