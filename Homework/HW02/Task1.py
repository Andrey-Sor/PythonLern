# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

a = abs(float(input()))
sum = 0
while a != int(a):
    a = a * 10
while a > 0:
    sum = sum + a % 10
    a //= 10
print(int(sum))
