# 10.11
import random

def task_10_11():
    result = random.randint(1, 6)
    print(f"Выпало: {result}")

# 10.12
import random

def task_10_12():
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)
    
    print(f"Игрок 1: {player1}")
    print(f"Игрок 2: {player2}")
    
    if player1 > player2:
        print("Игрок 1 выиграл!")
    elif player2 > player1:
        print("Игрок 2 выиграл!")
    else:
        print("Ничья!")

# 10.13
import random

def task_10_13_v1():
    player1_wins = 0
    player2_wins = 0
    draws = 0
    
    for _ in range(2):
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        
        print(f"Бросок: Игрок 1 - {player1}, Игрок 2 - {player2}")
        
        if player1 > player2:
            player1_wins += 1
        elif player2 > player1:
            player2_wins += 1
        else:
            draws += 1
    
    print(f"\nИтог: Игрок 1 - {player1_wins} побед, Игрок 2 - {player2_wins} побед, Ничьих - {draws}")
    
    if player1_wins > player2_wins:
        print("Игрок 1 выиграл матч!")
    elif player2_wins > player1_wins:
        print("Игрок 2 выиграл матч!")
    else:
        print("Матч закончился вничью!")

def task_10_13_v2():
    n = int(input("Сколько бросков сделает каждый игрок? "))
    
    player1_wins = 0
    player2_wins = 0
    draws = 0
    
    for i in range(n):
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        
        print(f"Бросок {i+1}: Игрок 1 - {player1}, Игрок 2 - {player2}")
        
        if player1 > player2:
            player1_wins += 1
            print("  Выиграл Игрок 1")
        elif player2 > player1:
            player2_wins += 1
            print("  Выиграл Игрок 2")
        else:
            draws += 1
            print("  Ничья")
    
    print(f"\nИтог за {n} бросков:")
    print(f"Игрок 1: {player1_wins} побед")
    print(f"Игрок 2: {player2_wins} побед")
    print(f"Ничьих: {draws}")
    
    if player1_wins > player2_wins:
        print("Игрок 1 выиграл матч!")
    elif player2_wins > player1_wins:
        print("Игрок 2 выиграл матч!")
    else:
        print("Матч закончился вничью!")

# Выберите вариант:
# task_10_13_v1()  # 2 броска каждый
# task_10_13_v2()  # N бросков



# 10.14
import random

def task_10_14():
    players = []
    for i in range(3):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        players.append((i+1, total))
        print(f"Игрок {i+1}: {dice1} + {dice2} = {total}")
    
    max_score = max(players, key=lambda x: x[1])
    winners = [p for p in players if p[1] == max_score[1]]
    
    if len(winners) == 1:
        print(f"\nПобедил Игрок {winners[0][0]} с суммой {winners[0][1]}!")
    else:
        print(f"\nНичья между игроками: {', '.join([f'Игрок {w[0]}' for w in winners])} с суммой {winners[0][1]}")




# 10.15
import random

def task_10_15():
    print("100 бросков:")
    counts_100 = {i: 0 for i in range(1, 7)}
    
    for _ in range(100):
        dice = random.randint(1, 6)
        counts_100[dice] += 1
    
    for i in range(1, 7):
        print(f"{i}: {counts_100[i]} раз ({counts_100[i]/100:.3f})")
    
    print("\n1000 бросков:")
    counts_1000 = {i: 0 for i in range(1, 7)}
    
    for _ in range(1000):
        dice = random.randint(1, 6)
        counts_1000[dice] += 1
    
    for i in range(1, 7):
        print(f"{i}: {counts_1000[i]} раз ({counts_1000[i]/1000:.3f})")





# 10.16
import random

def task_10_16():
    # Все возможные кости домино от 0-0 до 6-6
    all_dominoes = [(i, j) for i in range(7) for j in range(i, 7)]
    
    chosen = random.choice(all_dominoes)
    print(f"Выпала кость: {chosen[0]}-{chosen[1]}")



# 10.17
import random

def task_10_17():
    all_dominoes = [(i, j) for i in range(7) for j in range(i, 7)]
    
    # Выбираем две разные кости
    domino1 = random.choice(all_dominoes)
    remaining = [d for d in all_dominoes if d != domino1]
    domino2 = random.choice(remaining)
    
    print(f"Кость 1: {domino1[0]}-{domino1[1]}")
    print(f"Кость 2: {domino2[0]}-{domino2[1]}")
    
    # Проверяем, можно ли приставить кости друг к другу
    can_connect = (
        domino1[0] == domino2[0] or 
        domino1[0] == domino2[1] or 
        domino1[1] == domino2[0] or 
        domino1[1] == domino2[1]
    )
    
    if can_connect:
        print("Кости можно приставить друг к другу.")
    else:
        print("Кости нельзя приставить друг к другу.")





# 10.18
import random

def task_10_18_a():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    
    print(f"Чему равно произведение {a} × {b}?")
    answer = int(input("Ответ: "))
    
    if answer == a * b:
        print("Правильно!")
    else:
        print(f"Неправильно! Правильный ответ: {a * b}")

def task_10_18_b():
    correct = 0
    incorrect = 0
    
    for i in range(20):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        
        print(f"\nВопрос {i+1}: Чему равно произведение {a} × {b}?")
        answer = int(input("Ответ: "))
        
        if answer == a * b:
            correct += 1
            print("Правильно!")
        else:
            incorrect += 1
            print(f"Неправильно! Правильный ответ: {a * b}")
    
    print(f"\nИтог: Правильно - {correct}, Неправильно - {incorrect}")

def task_10_18_c():
    question_num = 1
    
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        
        print(f"\nВопрос {question_num}: Чему равно произведение {a} × {b}?")
        answer = int(input("Ответ (0 для выхода): "))
        
        if answer == 0:
            print("Игра окончена.")
            break
        
        if answer == a * b:
            print("Правильно!")
        else:
            print(f"Неправильно! Правильный ответ: {a * b}")
        
        question_num += 1

# Выберите вариант:
# task_10_18_a()  # Один вопрос
# task_10_18_b()  # 20 вопросов
# task_10_18_c()  # До ввода 0





# 10.19
import random

def task_10_19():
    cards = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    
    chosen = random.choice(cards)
    print(f"Выпала карта: {chosen}")




# 10.20
import random

def task_10_20():
    suits = ['пик', 'треф', 'бубен', 'червей']
    ranks = ['шестерка', 'семерка', 'восьмерка', 'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
    
    suit = random.choice(suits)
    rank = random.choice(ranks)
    
    # Склонение масти для правильного окончания
    if suit == 'бубен':
        suit_word = 'бубей'
    elif suit == 'червей':
        suit_word = 'червей'
    else:
        suit_word = suit
    
    print(f"Выпала {rank} {suit_word}")

