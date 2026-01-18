# 10.1
import random

def task_10_1():
    # а)
    print("8 случайных чисел от 0 до 1:")
    for _ in range(8):
        print(random.random())
    
    # б)
    k = int(input("\nВведите k: "))
    print(f"{k} случайных чисел от 0 до 1:")
    for _ in range(k):
        print(random.random())
    
    # в)
    print("\n15 случайных чисел от 25 до 26:")
    for _ in range(15):
        print(25 + random.random())
    
    # г)
    print("\n20 случайных чисел от 0 до 15:")
    for _ in range(20):
        print(15 * random.random())
    
    # д)
    a = int(input("\nВведите a: "))
    b = float(input("Введите b: "))
    k = random.randint(1, a)
    print(f"k = {k} случайных чисел от 0 до {b}:")
    for _ in range(k):
        print(b * random.random())
    
    # е)
    print("\n10 случайных чисел от -40 до 40:")
    for _ in range(10):
        print(-40 + 80 * random.random())
    
    # ж)
    m = int(input("\nВведите m: "))
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    k = random.randint(1, m)
    print(f"k = {k} случайных чисел от {a} до {b}:")
    for _ in range(k):
        print(a + (b - a) * random.random())





# 10.2
import random

def task_10_2():
    # а)
    print("10 случайных целых от 0 до 10:")
    for _ in range(10):
        print(random.randint(0, 10))
    
    # б)
    k = int(input("\nВведите k: "))
    a = int(input("Введите a: "))
    print(f"{k} случайных целых от 0 до {a}:")
    for _ in range(k):
        print(random.randint(0, a))
    
    # в)
    print("\n20 случайных целых от 10 до 20:")
    for _ in range(20):
        print(random.randint(10, 20))
    
    # г)
    k = int(input("\nВведите k: "))
    a = int(input("Введите a: "))
    print(f"{k} случайных целых от -10 до {a}:")
    for _ in range(k):
        print(random.randint(-10, a))
    
    # д)
    a = int(input("\nВведите a: "))
    b = int(input("Введите b: "))
    k = random.randint(1, 15)
    print(f"k = {k} случайных целых от {a} до {b}:")
    for _ in range(k):
        print(random.randint(a, b))




# 10.3
import random

def task_10_3():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    
    m = random.randint(1, 20)
    n = random.randint(1, 20)
    
    print(f"m = {m}, n = {n}")
    
    print(f"\n{n} целых чисел от {a} до {b}:")
    for _ in range(n):
        print(random.randint(a, b))
    
    print(f"\n{m} вещественных чисел от 0 до {n}:")
    for _ in range(m):
        print(n * random.random())




# 10.4
import random

def task_10_4():
    print("50 чисел (0-5), выводятся только 0 и 1:")
    zeros_ones = 0
    for _ in range(50):
        num = random.randint(0, 5)
        if num == 0 or num == 1:
            print(num)
            zeros_ones += 1
    print(f"Всего выведено 0 и 1: {zeros_ones}")

# 10.5
import random

def task_10_5():
    print("30 чисел (0-5), выводятся только нечетные:")
    odd_count = 0
    for _ in range(30):
        num = random.randint(0, 5)
        if num % 2 != 0:
            print(num)
            odd_count += 1
    print(f"Всего выведено нечетных: {odd_count}")



# 10.6
import random

def task_10_6():
    ones = 0
    zeros = 0
    print("50 случайных чисел (0 или 1):")
    for _ in range(50):
        num = random.randint(0, 1)
        print(num)
        if num == 1:
            ones += 1
        else:
            zeros += 1
    
    print(f"Единиц: {ones}")
    print(f"Нулей: {zeros}")





# 10.7
import random

def task_10_7():
    # а)
    a = random.randint(0, 1)
    b = random.randint(0, 2)
    while b == a:
        b = random.randint(0, 2)
    print(f"a = {a}, b = {b} (разные числа)")
    
    # б)
    a = random.randint(1, 2)
    b = random.randint(0, 2)
    c = random.randint(1, 3)
    while b == a:
        b = random.randint(0, 2)
    while c == a or c == b:
        c = random.randint(1, 3)
    print(f"a = {a}, b = {b}, c = {c} (все разные)")
    
    # в)
    numbers = [2] * 7 + [3] * 8
    random.shuffle(numbers)
    print("15 чисел (7 двоек и 8 троек):")
    print(numbers)





# 10.8
import random

def task_10_8():
    # 0 - решка, 1 - орел
    result = random.randint(0, 1)
    if result == 0:
        print("Выпала решка (0)")
    else:
        print("Выпал орел (1)")






# 10.9
import random

def task_10_9():
    # Для 100 подбрасываний
    heads = 0
    tails = 0
    
    for _ in range(100):
        if random.randint(0, 1) == 0:
            tails += 1
        else:
            heads += 1
    
    print("100 подбрасываний:")
    print(f"Орлов: {heads} ({heads/100:.3f})")
    print(f"Решек: {tails} ({tails/100:.3f})")
    
    # Для 1000 подбрасываний
    heads = 0
    tails = 0
    
    for _ in range(1000):
        if random.randint(0, 1) == 0:
            tails += 1
        else:
            heads += 1
    
    print("\n1000 подбрасываний:")
    print(f"Орлов: {heads} ({heads/1000:.3f})")
    print(f"Решек: {tails} ({tails/1000:.3f})")





# 10.10
import random

def task_10_10_a():
    print("Чет (введите 2) или нечет (введите 1)?")
    user_choice = int(input("Ваш выбор: "))
    
    computer_choice = random.choice([1, 2])
    
    print(f"Компьютер выбрал: {'нечет' if computer_choice == 1 else 'чет'}")
    
    if user_choice == computer_choice:
        print("Вы угадали!")
    else:
        print("Вы не угадали.")

def task_10_10_b():
    n = int(input("Сколько раз играем? "))
    user_wins = 0
    computer_wins = 0
    
    for i in range(n):
        print(f"\nИгра {i+1}:")
        print("Чет (2) или нечет (1)?")
        user_choice = int(input("Ваш выбор: "))
        
        computer_choice = random.choice([1, 2])
        print(f"Компьютер выбрал: {'нечет' if computer_choice == 1 else 'чет'}")
        
        if user_choice == computer_choice:
            user_wins += 1
        else:
            computer_wins += 1
    
    print(f"\nСчет {user_wins}:{computer_wins}")
    if user_wins > computer_wins:
        print("Вы выиграли!")
    elif computer_wins > user_wins:
        print("Вы проиграли!")
    else:
        print("Ничья!")

def task_10_10_c():
    user_wins = 0
    computer_wins = 0
    
    while True:
        print("\nЧет (2) или нечет (1)?")
        user_choice = int(input("Ваш выбор: "))
        
        computer_choice = random.choice([1, 2])
        print(f"Компьютер выбрал: {'нечет' if computer_choice == 1 else 'чет'}")
        
        if user_choice == computer_choice:
            user_wins += 1
            print("Вы угадали!")
        else:
            computer_wins += 1
            print("Вы не угадали.")
        
        again = input("Продолжить еще раз? (да/нет): ")
        if again.lower() in ['нет', 'no', 'n']:
            break
    
    print(f"\nВерных ответов: {user_wins}")
    print(f"Неверных ответов: {computer_wins}")

# Выберите вариант игры:
# task_10_10_a()  # Один раз
# task_10_10_b()  # N раз
# task_10_10_c()  # До отказа
