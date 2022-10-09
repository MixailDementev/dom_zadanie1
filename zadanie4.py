# Задача 4: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

a = int(input('Enter quarter number = '))

while 0 < a < 5:
    if a == 1:
        print('x > 0 and y > 0')
        break
    elif a == 2:
        print('x < 0 and y > 0')
        break
    elif a == 3:
        print('x < 0 and y < 0')
        break
    else:
        print('x > 0 and y < 0')
        break
else:
    print('There is no such quarter in the coordinate system')
