# Задание №5
def my_sum ():
    sum_res = 0
    exit_sum = False
    while exit_sum == False:
        number = input('Введите числа или $ для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '$':
                exit_sum = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел {sum_res}')
    print(f'Итого {sum_res}')
my_sum()

