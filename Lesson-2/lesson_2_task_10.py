def bank(X, Y):
    """Вычисляет сумму на счету пользователя спустя Y лет под 10% годовых."""
    total_amount = X
    for year in range(Y):
        total_amount += total_amount * 0.10  # Увеличиваем сумму на 10%
    return total_amount

# Пример использования функции
initial_deposit = 1000  # Сумма вклада
years = 5  # Срок вклада в годах

final_amount = bank(initial_deposit, years)

# Выводим результат
print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")