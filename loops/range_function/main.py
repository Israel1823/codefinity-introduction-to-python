# Lista de dias da semana
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Lista de promoções
weekly_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# Percorre os índices de 0 até o tamanho da lista
for day in range(len(weekdays)):
    Promotion = weekly_promotions[day]
    weekday = weekdays[day]
    print(f"{weekday} promotion: {Promotion}")
