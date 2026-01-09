k = int(input("День года (1-365): "))
d = int(input("День недели 1 января (1-7): "))
day_of_week = (k + d - 2) % 7 + 1
print(day_of_week)
