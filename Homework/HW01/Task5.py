# Задача 5 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Введите координаты точки A, x = '))
y1 = float(input('Введите координаты точки A, y = '))
x2 = float(input('Введите координаты точки B, x = '))
y2 = float(input('Введите координаты точки B, y = '))
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
d = d * 100 // 1 /100
print(f'Расстояние между точками: {d}')