# Задача 2 Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = float(input('Введите x = '))
# y = float(input('Введите y = '))
# z = float(input('Введите z = '))

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]
            if(not(x or y or z) == (not x and not y and not z)):
                print(True)
            else:
                print(False)


x   y   z
t   t   t
t   t   f
t   f   t



# ???????