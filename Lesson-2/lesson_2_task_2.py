def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    return year % 4 == 0

# Выбираем год для проверки
year_to_check = 2023  #тут надо менять год
# Вызываем функцию и сохраняем результат
is_leap = is_year_leap(year_to_check)

# Выводим результат
print(f"Год {year_to_check}: {is_leap}")