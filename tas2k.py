def calculate_total(price, quantity):
    """Вычисляет общую стоимость без скидки"""
    return price * quantity

def apply_discount(total, discount_percent):
    """Применяет скидку к общей сумме"""
    discount_amount = total * (discount_percent / 100)
    return total - discount_amount

def final_price(price, quantity, discount_percent):
    """Вычисляет итоговую цену со скидкой"""
    total = calculate_total(price, quantity)
    return apply_discount(total, discount_percent)

# Пример использования
print("=== Калькулятор скидок ===")
result = final_price(1000, 3, 15)  # Товар: 1000 руб, 3 шт, скидка 15%
print(f"Итоговая цена со скидкой: {result:.2f} руб.")
