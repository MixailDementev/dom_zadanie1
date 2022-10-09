# Задача 5: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

x1 = float(input('enter the x coordinate of point A = '))
y1 = float(input('enter the y coordinate of point A = '))
x2 = float(input('enter the x coordinate of point B = '))
y2 = float(input('enter the y coordinate of point B = '))

# result = round(((x1-x2)**2+(y1-y2)**2)**0.5, 2)
# result = round(math.sqrt(math.pow((x1-x2), 2)+math.pow((y1-y2), 2)), 3)
# print(result)


# def distance(x1, y1, x2, y2):
    # result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    # return result

# result = round(distance(x1, y1, x2, y2), 3)
# print('Distance between A and B: ', result)

print('Distance between A and B: ', round(math.sqrt(math.pow((x1-x2), 2)+math.pow((y1-y2), 2)), 3))
