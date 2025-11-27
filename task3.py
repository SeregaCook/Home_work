import random

def generate_name():
    """Генерирует случайное имя"""
    names = ['Анна', 'Иван', 'Мария', 'Петр', 'Ольга', 'Сергей', 'Елена', 'Алексей']
    return random.choice(names)

def generate_email(name):
    """Создает email на основе имени"""
    # Убираем кириллицу и добавляем случайные цифры
    name_latin = name.lower().translate(str.maketrans('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'abvgdeejziyklmnoprstufhzcss_y_euya'))
    return f"{name_latin}{random.randint(100, 999)}@example.com"

def generate_age():
    """Генерирует случайный возраст от 18 до 65 лет"""
    return random.randint(18, 65)

def create_user():
    """Создает словарь с данными пользователя"""
    name = generate_name()
    email = generate_email(name)
    age = generate_age()
    
    return {
        'name': name,
        'email': email,
        'age': age
    }

# Пример использования
print("\n=== Генератор пользовательских данных ===")
user = create_user()
print(f"Сгенерированный пользователь: {user}")

# Можно создать несколько пользователей
print("\nНесколько пользователей:")
for i in range(3):
    user = create_user()
    print(f"Пользователь {i+1}: {user}")
