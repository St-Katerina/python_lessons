# Задание №7
a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
day = 1
while a <= b:
    print(day, "-й день:", round(a, 2))
    a = a + a / 10
    day = day+1
print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км".format(day, b))
