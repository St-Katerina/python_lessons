# Задание №5-6

revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = revenue - costs
if profit > costs:
    print("Предприятие работает с прибылью")
    profitability = profit / revenue * 100
    employees = int(input("Введите численность сотрудникоф фирмы: "))
    profit_employees = profitability / employees
    print("Прибыль фирмы в расчете на одного сотрудника: ", round(profit_employees, 2))
else:
    print("Предприятие работает убыточно")
