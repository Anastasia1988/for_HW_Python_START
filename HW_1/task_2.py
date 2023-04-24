# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("Введите трехзначное число: ")
if int(number) < 100 or int(number) > 999:
    print("Введено не трехзначное число!") 
else:
    sum = 0
    for i in number:
        sum += int(i)
    print(sum)

