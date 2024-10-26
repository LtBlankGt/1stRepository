salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0 #необходимая подушка
dif_ft = spend - salary #необходимая подушка в первый месяц

for months_vsego in range(months - 1): # -1 т.к один (первый) месяц без процента
    spend = spend * (1 + increase)
    money_capital = money_capital + (spend - salary)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital + dif_ft))
