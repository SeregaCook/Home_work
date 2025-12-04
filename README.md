# ===========================
# Home_work - Python Tasks
# ===========================

# 1. Температурный конвертер
def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value

    # Переводим в Цельсий
    if from_scale == 'F':
        value = (value - 32) * 5 / 9
    elif from_scale == 'K':
        value = value - 273.15
    elif from_scale != 'C':
        raise ValueError("Неверная шкала")

    # Из Цельсия в нужную шкалу
    if to_scale == 'F':
        return value * 9 / 5 + 32
    elif to_scale == 'K':
        return value + 273.15
    elif to_scale == 'C':
        return value
    else:
        raise ValueError("Неверная шкала")

# Пример:
# print(convert_temperature(100, 'C', 'F'))  # 212.0

# 2. Статистика оценок
def grades_statistics(grades):
    return {
        'average': sum(grades) / len(grades),
        'best': max(grades),
        'worst': min(grades),
        'passed': sum(1 for g in grades if g >= 5),
        'failed': sum(1 for g in grades if g < 5)
    }

# Пример:
# grades = [3, 5, 8, 2, 10, 6]
# print(grades_statistics(grades))

# 3. Слияние списков с условием
def merge_lists(list1, list2, condition='common'):
    set1 = set(list1)
    set2 = set(list2)

    if condition == 'common':
        return list(set1 & set2)
    elif condition == 'unique':
        return list(set1 ^ set2)
    elif condition == 'all':
        return list(set1 | set2)
    else:
        raise ValueError("Неверное условие")

# Пример:
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# print(merge_lists(a, b, 'common'))  # [3, 4]

# 4. Таблица умножения (только четные числа)
def multiplication_table(N):
    for i in range(2, N + 1, 2):
        print(f"\nТаблица для {i}:")
        for j in range(1, 11):
            print(f"{i:2} × {j:2} = {i * j:3}")

# Пример:
# multiplication_table(6)

# 5. Симуляция банкомата
def atm_simulation():
    balance = 10000
    while True:
        print("\n1. Проверить баланс")
        print("2. Снять деньги")
        print("3. Пополнить счет")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            print(f"Ваш баланс: {balance} руб.")
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            if amount <= 0:
                print("Сумма должна быть положительной!")
            elif amount > 10000:
                print("За одну операцию можно снять не более 10000!")
            elif amount > balance:
                print("Недостаточно средств!")
            else:
                balance -= amount
                print("Снятие успешно!")
        elif choice == '3':
            amount = int(input("Введите сумму для пополнения: "))
            if amount <= 0:
                print("Сумма должна быть положительной!")
            elif amount > 50000:
                print("За одну операцию можно пополнить не более 50000!")
            else:
                balance += amount
                print("Пополнение успешно!")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор!")

# ===========================
# README.md (кратко)
# ===========================

readme_text = """
# Учебные задачи по Python

В проекте реализованы:
1. Температурный конвертер (C, F, K)
2. Статистика оценок
3. Слияние списков с условиями (common, unique, all)
4. Таблица умножения для четных чисел
5. Симуляция банкомата

## Запуск
- Python 3.x
- Запуск функций через `python main.py`
- Для банкомата: вызов `atm_simulation()`

## GitHub Push
1. git add .
2. git commit -m "Your message"
3. git push
"""

# Пример записи README (можно сохранить в файл)
# with open("README.md", "w") as f:
#     f.write(readme_text)
