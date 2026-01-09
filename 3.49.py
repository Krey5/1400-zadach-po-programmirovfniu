import math
y = float(input("Угол часовой стрелки (0 < y ≤ 2π): "))
# y в радианах
hours = y / (math.pi / 6)  # 2π = 12 часов, π/6 = 1 час
full_hours = int(hours)
full_minutes = int((hours - full_hours) * 60)
# Минутная стрелка: угол от 12 часов
minute_angle = (hours * 60) * (2 * math.pi / 60)  # в радианах
print("Полных часов:", full_hours, "Полных минут:", full_minutes)
print("Угол минутной стрелки (рад):", minute_angle)
