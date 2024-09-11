import math

center_circle = tuple(int(x.strip()) for x in input("Введите координаты окружности: ").split(' '))
radius = int(input("Введите радиус окружности: "))
point = tuple(int(x.strip()) for x in input("Введите координаты точки: ").split(' '))

def check_point_in_circle(center_circle, radius, point):
    distance = math.sqrt((point[0] - center_circle[0])**2 + (point[1] - center_circle[1])**2)
    
    if distance == radius:
        return "0 - точка лежит на окружности"
    elif distance < radius:
        return "1 - точка внутри"
    else:
        return "2 - точка снаружи"

result = check_point_in_circle(center_circle, radius, point)
print(result)