# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Enter the number indicating the day of the week = '))

while 0 < a < 8:
    if a == 1:
        print('Monday is a working day')
        break
    elif a == 2:
        print('Tuesday is a working day')
        break
    elif a == 3:
        print('Wednesday is a working day')
        break
    elif a == 4:
        print('Thursday is a working day')
        break
    elif a == 5:
        print('Friday is a working day')
        break
    elif a == 6:
        print('Saturday is a day off')
        break
    else:
        print('Sunday is a day off')
        break
else:
    print('There is no such day of the week')
