# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите число N: "))
degree = 2
count = 1

while degree <= number:
    degree *= 2
    count += 1
print(count -1, degree // 2)



    