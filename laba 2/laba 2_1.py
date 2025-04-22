money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

k=1
while money_capital>spend:
    money_capital=money_capital+salary
    money_capital=money_capital-spend
    spend=spend+spend*increase
    k=k+1
print("Количество месяцев, которое можно протянуть без долгов:", k)
