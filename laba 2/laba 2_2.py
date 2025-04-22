salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
podushka = 0
i=1
for i in range(months):
    podushka=podushka+spend-salary
    spend=spend+spend*increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(podushka))
