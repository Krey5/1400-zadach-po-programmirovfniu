km_h = float(input("Скорость в км/ч: "))
m_s = float(input("Скорость в м/с: "))

km_h_to_m_s = km_h * 1000 / 3600

if km_h_to_m_s > m_s:
    print("Скорость в км/ч больше")
else:
    print("Скорость в м/с больше")
