# Задание №4

number = int(input("Введите число: "))
max_number = 0
while number > 0:
    i = number % 10
    if i > max_number:
        max_number = i
    number = number//10
print("Самая большая цифра в числе: ", max_number)



