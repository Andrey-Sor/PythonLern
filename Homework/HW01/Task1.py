# Задача 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter the day (digit) of the week: '))

if(day == 6 or day == 7):
    print('Yes, this day is a day off') 
elif(day >= 1 and day <=5):
    print('No, this day is weekdays')
else:
    print('Your entered wrong day of week')
