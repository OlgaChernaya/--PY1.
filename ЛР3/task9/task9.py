salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# Используем цикл с кол-вом шагов, так как мы заранее знаем кол-во месяцев,
# т.е. накопительный эффект в подушку безопасности будет складываться из дельты каждого месяца с учетом роста цен

for _ in range(1, months + 1):
    delta = spend - salary  # находим дельту - нехватка средств
    money_capital += delta  # увеличиваем подушку безопасности на дельту
    spend *= 1 + increase  # учитываем рост цен для следующего месяца

print(round(money_capital))
