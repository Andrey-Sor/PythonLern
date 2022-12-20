# Задача 4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Enter the quarter number from 1 to 4: '))
if quarter == 1:
    print('All possible coordinates of points: x ∈ (0; +∞), y ∈ (0; +∞)')
if quarter == 2:
    print('All possible coordinates of points: x ∈ (-∞; 0), y ∈ (0; +∞)')
if quarter == 3:
    print('All possible coordinates of points: x ∈ (-∞; 0), y ∈ (-∞; 0)')
if quarter == 4:
    print('All possible coordinates of points: x ∈ (0; +∞), y ∈ (-∞; 0)')
else:
    print('Wrong data!')