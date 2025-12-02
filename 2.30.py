import math

def triangle_area(x1, y1, x2, y2, x3, y3):
    
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

def quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4):

    area1 = triangle_area(x1, y1, x2, y2, x3, y3)
    area2 = triangle_area(x1, y1, x3, y3, x4, y4)
    
    return area1 + area2

print("Введите координаты вершин выпуклого четырехугольника:")
x1, y1 = map(float, input("A(x y): ").split())
x2, y2 = map(float, input("B(x y): ").split())
x3, y3 = map(float, input("C(x y): ").split())
x4, y4 = map(float, input("D(x y): ").split())

S = quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4)


print(S)
