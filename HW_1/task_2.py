# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Введите трехзначное число: ")
number = input()
if int(number) < 100 and int(number) > 999:
    print("Введено не трехзначное число!")
i = 0
sum = 0
while i < len(number):    
    sum += int(number[i])
    i += 1
print(sum)

