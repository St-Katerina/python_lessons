# Задание №1
my_func = lambda arg_1, arg_2: arg_1/arg_2
arg_1 = float(input('Введите делимое: '))
arg_2 = float(input('Введите делитель: '))
if arg_2 == 0:
    print('На ноль делить нельзя!')
    arg_2 = float(input('Введите делитель: '))
print(my_func(arg_1, arg_2))