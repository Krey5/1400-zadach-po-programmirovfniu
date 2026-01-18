# 10.21
import random

def task_10_21():
    suits = ['пики', 'трефы', 'бубны', 'червы']
    ranks = ['шестерка', 'семерка', 'восьмерка', 'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
    
    # Выбор карт для двух игроков
    card1 = (random.randint(0, 3), random.randint(0, 8))  # (масть, достоинство)
    card2 = (random.randint(0, 3), random.randint(0, 8))
    
    print(f"Игрок 1: {ranks[card1[1]]} {suits[card1[0]]}")
    print(f"Игрок 2: {ranks[card2[1]]} {suits[card2[0]]}")
    
    # Определение победителя
    if card1[0] > card2[0]:  # Сравниваем масти
        print("Победил Игрок 1 (старшая масть)")
    elif card2[0] > card1[0]:
        print("Победил Игрок 2 (старшая масть)")
    else:  # Масти равны, сравниваем достоинства
        if card1[1] > card2[1]:
            print("Победил Игрок 1 (старшая карта в масти)")
        elif card2[1] > card1[1]:
            print("Победил Игрок 2 (старшая карта в масти)")
        else:
            print("Ничья (одинаковые карты)")



# 10.22
import random

def task_10_22():
    suits = ['пики', 'трефы', 'бубны', 'червы']
    ranks = ['шестерка', 'семерка', 'восьмерка', 'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
    
    rounds = int(input("Сколько раундов сыграем? "))
    player1_wins = 0
    player2_wins = 0
    draws = 0
    
    for round_num in range(1, rounds + 1):
        print(f"\nРаунд {round_num}:")
        
        card1 = (random.randint(0, 3), random.randint(0, 8))
        card2 = (random.randint(0, 3), random.randint(0, 8))
        
        print(f"Игрок 1: {ranks[card1[1]]} {suits[card1[0]]}")
        print(f"Игрок 2: {ranks[card2[1]]} {suits[card2[0]]}")
        
        if card1[0] > card2[0]:
            print("Выиграл Игрок 1")
            player1_wins += 1
        elif card2[0] > card1[0]:
            print("Выиграл Игрок 2")
            player2_wins += 1
        else:
            if card1[1] > card2[1]:
                print("Выиграл Игрок 1")
                player1_wins += 1
            elif card2[1] > card1[1]:
                print("Выиграл Игрок 2")
                player2_wins += 1
            else:
                print("Ничья")
                draws += 1
    
    print(f"\nИтог за {rounds} раундов:")
    print(f"Игрок 1: {player1_wins} побед")
    print(f"Игрок 2: {player2_wins} побед")
    print(f"Ничьих: {draws}")
    
    if player1_wins > player2_wins:
        print("Общий победитель: Игрок 1!")
    elif player2_wins > player1_wins:
        print("Общий победитель: Игрок 2!")
    else:
        print("Общая ничья!")





# 10.23
import random

def task_10_23():
    suits = ['пики', 'трефы', 'бубны', 'червы']
    ranks = ['шестерка', 'семерка', 'восьмерка', 'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
    
    # Случайно выбираем козырную масть
    trump_suit = random.randint(0, 3)
    print(f"Козырная масть: {suits[trump_suit]}")
    
    # Выбираем карту
    suit = random.randint(0, 3)
    rank = random.randint(0, 8)
    
    # Проверяем, козырная ли карта
    if suit == trump_suit:
        print(f"Выпала козырная {ranks[rank]} {suits[suit]}")
    else:
        print(f"Выпала {ranks[rank]} {suits[suit]}")






# 10.24
import random

def task_10_24():
    while True:
        a = random.randint(1, 8)
        b = random.randint(1, 8)
        c = random.randint(1, 8)
        d = random.randint(1, 8)
        
        # a) Ладья не угрожает полю (c,d)
        if not (a == c or b == d):
            # б) Слон не угрожает полю (c,d)
            if abs(a - c) != abs(b - d):
                # в) Король может попасть на поле (c,d) одним ходом
                if abs(a - c) <= 1 and abs(b - d) <= 1:
                    # г) Ферзь не угрожает полю (c,d)
                    if not (a == c or b == d or abs(a - c) == abs(b - d)):
                        print(f"a={a}, b={b}, c={c}, d={d}")
                        print(f"Поле ({a},{b}) и поле ({c},{d})")
                        return






# 10.25
import random

def task_10_25_a():
    # Белая пешка
    while True:
        a = random.randint(1, 8)
        b = random.randint(1, 7)  # Не может быть на 8 горизонтали
        c = random.randint(1, 8)
        d = random.randint(1, 8)
        
        # Обычный ход (на 1 клетку вперед)
        if c == a and d == b + 1:
            print(f"Белая пешка с ({a},{b}) может пойти на ({c},{d}) обычным ходом")
            return
        # Взятие (на 1 клетку вперед по диагонали)
        elif abs(a - c) == 1 and d == b + 1:
            print(f"Белая пешка с ({a},{b}) может пойти на ({c},{d}) взятием")
            return

def task_10_25_b():
    # Черная пешка
    while True:
        a = random.randint(1, 8)
        b = random.randint(2, 8)  # Не может быть на 1 горизонтали
        c = random.randint(1, 8)
        d = random.randint(1, 8)
        
        # Обычный ход (на 1 клетку назад)
        if c == a and d == b - 1:
            print(f"Черная пешка с ({a},{b}) может пойти на ({c},{d}) обычным ходом")
            return
        # Взятие (на 1 клетку назад по диагонали)
        elif abs(a - c) == 1 and d == b - 1:
            print(f"Черная пешка с ({a},{b}) может пойти на ({c},{d}) взятием")
            return

def task_10_25_c():
    # Конь угрожает полю
    while True:
        a = random.randint(1, 8)
        b = random.randint(1, 8)
        c = random.randint(1, 8)
        d = random.randint(1, 8)
        
        # Ход коня (буквой Г)
        if (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2):
            print(f"Конь на ({a},{b}) угрожает полю ({c},{d})")
            return

# Выберите вариант:
# task_10_25_a()  # Белая пешка
# task_10_25_b()  # Черная пешка
# task_10_25_c()  # Конь






# 10.26
import random

def can_rook_move(a, b, e, f):
    return a == e or b == f

def can_bishop_move(a, b, e, f):
    return abs(a - e) == abs(b - f)

def can_queen_move(a, b, e, f):
    return a == e or b == f or abs(a - e) == abs(b - f)

def can_knight_move(a, b, e, f):
    return (abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2)

def can_king_move(a, b, e, f):
    return abs(a - e) <= 1 and abs(b - f) <= 1

def is_under_attack(fig_type, x, y, a, b):
    if fig_type == 'rook':
        return can_rook_move(x, y, a, b)
    elif fig_type == 'bishop':
        return can_bishop_move(x, y, a, b)
    elif fig_type == 'queen':
        return can_queen_move(x, y, a, b)
    elif fig_type == 'knight':
        return can_knight_move(x, y, a, b)
    elif fig_type == 'king':
        return can_king_move(x, y, a, b)
    return False

def task_10_26():
    white_pieces = ['rook', 'queen', 'knight', 'bishop', 'king']
    black_pieces = ['rook', 'queen', 'knight', 'bishop']
    
    for white in white_pieces:
        for black in black_pieces:
            while True:
                a = random.randint(1, 8)
                b = random.randint(1, 8)
                c = random.randint(1, 8)
                d = random.randint(1, 8)
                e = random.randint(1, 8)
                f = random.randint(1, 8)
                
                # Поля должны быть разными
                if (a, b) == (c, d) or (a, b) == (e, f) or (c, d) == (e, f):
                    continue
                
                # Белая фигура может пойти на (e,f)
                white_can_move = False
                if white == 'rook':
                    white_can_move = can_rook_move(a, b, e, f)
                elif white == 'queen':
                    white_can_move = can_queen_move(a, b, e, f)
                elif white == 'knight':
                    white_can_move = can_knight_move(a, b, e, f)
                elif white == 'bishop':
                    white_can_move = can_bishop_move(a, b, e, f)
                elif white == 'king':
                    white_can_move = can_king_move(a, b, e, f)
                
                # Черная фигура не угрожает полю (e,f)
                black_not_attack = not is_under_attack(black, c, d, e, f)
                
                if white_can_move and black_not_attack:
                    print(f"Белая {white} на ({a},{b}) может пойти на ({e},{f})")
                    print(f"Черная {black} на ({c},{d}) не угрожает полю ({e},{f})")
                    return






# 10.27
import random
import math

def task_10_27_a():
    hits = 0
    total = 1000000
    
    for _ in range(total):
        x = random.uniform(0, math.pi)
        y = random.uniform(0, 1)
        
        if y <= math.sin(x):
            hits += 1
    
    area = (math.pi * 1) * (hits / total)
    print(f"Площадь под синусоидой (метод Монте-Карло): {area:.6f}")
    print(f"Точное значение: {2:.6f}")

def task_10_27_b():
    hits = 0
    total = 1000000
    
    for _ in range(total):
        x = random.uniform(0, 3)
        y = random.uniform(0, 9)
        
        if y <= x**2:
            hits += 1
    
    area = (3 * 9) * (hits / total)
    print(f"Площадь под параболой y=x² от 0 до 3 (метод Монте-Карло): {area:.6f}")
    print(f"Точное значение: {9:.6f}")

# Выберите вариант:
# task_10_27_a()  # Синусоида
# task_10_27_b()  # Парабола





# 10.28
import random

def task_10_28():
    hits = 0
    total = 0
    pi_estimate = 0
    error = 1
    
    while error > 0.0001:
        total += 10000
        for _ in range(10000):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            
            if x**2 + y**2 <= 1:
                hits += 1
        
        pi_estimate = 4 * hits / total
        error = abs(pi_estimate - math.pi)
    
    print(f"Вычисленное значение π: {pi_estimate:.6f}")
    print(f"Точное значение π: {math.pi:.6f}")
    print(f"Погрешность: {error:.6f}")
    print(f"Количество испытаний: {total}")

# Не забудьте импортировать math
import math
