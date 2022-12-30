# Задание №2
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthday = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите адрес электронной почты: ')
phone = input('Введите номер телефона: ')
def my_func(*args):
    return args
print(my_func(name, surname, birthday, town, email, phone))