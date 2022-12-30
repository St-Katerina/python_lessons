# Задание №4
def my_func(x, y):
    return x ** y
print(f'Ответ: {my_func(int(input("Введите x: ")), int(input("Введите y: ")))}')


def my_func(x, y):
    i = 1
    divider = x
    while i < abs(y):
        divider = divider*x
        i = i+1
    return 1/divider
print(f'Ответ: {my_func(int(input("Введите x: ")), int(input("Введите y: ")))}')
