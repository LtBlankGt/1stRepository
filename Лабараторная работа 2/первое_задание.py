money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


bes_dolga = 1 #переменная для подсчета, будет увеличиваться с каждым месяцем


while money_capital >= 0:
    spend = spend * (1 + increase)
    money_capital = money_capital + salary - spend
    if money_capital <= 0:
        break
    else:
        bes_dolga += 1


print("Количество месяцев, которое можно протянуть без долгов:", bes_dolga)
