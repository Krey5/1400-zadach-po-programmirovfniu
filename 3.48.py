y = float(input("Угол поворота часовой стрелки (0 ≤ y ≤ 360): "))
# 360° = 12 часов, 1 час = 30°
full_hours = int(y // 30)
full_minutes = int((y % 30) * 2)  # 30° = 60 минут
print("Полных часов:", full_hours, "Полных минут:", full_minutes)
