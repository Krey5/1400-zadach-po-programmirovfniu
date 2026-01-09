h = int(input("Часы (0 < h ≤ 12): "))
m = int(input("Минуты (0 ≤ m ≤ 59): "))
# Угол часовой стрелки: 30*h + 0.5*m
# Угол минутной стрелки: 6*m
# Разница углов
def minutes_until(condition):
    for t in range(1, 720):  # до 12 часов вперед
        new_h = (h + (m + t) // 60) % 12
        new_m = (m + t) % 60
        angle_h = 30 * new_h + 0.5 * new_m
        angle_m = 6 * new_m
        diff = abs(angle_h - angle_m) % 360
        if condition(diff):
            return t
    return None

# a) Совпадут (разница 0° или 360°)
t1 = minutes_until(lambda d: d < 0.001 or abs(d - 360) < 0.001)
# б) Перпендикулярны (разница 90° или 270°)
t2 = minutes_until(lambda d: abs(d - 90) < 0.001 or abs(d - 270) < 0.001)

print("До совпадения:", t1, "мин")
print("До перпендикулярного положения:", t2, "мин")
