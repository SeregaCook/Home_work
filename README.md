from __future__ import annotations

from statistics import mean
from random import randint
from typing import Iterable, List


def is_valid_email(email: str) -> bool:
    """
    Simple email validator.

    A valid email for this task must contain an "@" symbol and have a domain
    part that includes at least one "." (e.g. "example@domain.com").
    """
    if "@" not in email:
        return False

    local_part, _, domain_part = email.partition("@")
    if not local_part or "." not in domain_part:
        return False

    domain_labels = domain_part.split(".")
    if any(label == "" for label in domain_labels):
        return False

    return True


def generate_sequence(start: int, end: int, step: int = 1) -> List[int]:
    """
    Generate a list of integers from start to end (exclusive) with a given step.
    """
    if step == 0:
        raise ValueError("step must not be zero")

    sequence = []
    current = start
    if step > 0:
        while current < end:
            sequence.append(current)
            current += step
    else:
        while current > end:
            sequence.append(current)
            current += step
    return sequence


def list_stats(numbers: Iterable[float]) -> dict:
    """
    Calculate basic statistics for a list of numbers.

    Returns a dictionary containing:
    - min
    - max
    - mean
    - median
    """
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers must not be empty")

    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    if n % 2 == 1:
        med = sorted_nums[n // 2]
    else:
        mid = n // 2
        med = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

    return {
        "min": min(sorted_nums),
        "max": max(sorted_nums),
        "mean": mean(sorted_nums),
        "median": med,
    }


def rectangle_area(width: float, height: float) -> float:
    """Compute the area of a rectangle."""
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def is_even(number: int) -> bool:
    """Return True if a number is even, False otherwise."""
    return number % 2 == 0


def greet(name: str | None = None) -> str:
    """
    Return a greeting message.

    If no name is provided, "Гость" (Guest) is used by default.
    """
    if not name:
        name = "Гость"
    return f"Привет, {name}!"


def find_max(a: float, b: float, c: float) -> float:
    """
    Return the maximum of three numbers without using the built-in max().
    """
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value


def calculator(a: float, b: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Supported operations: +, -, *, /.
    Returns "Неизвестная операция" for unsupported operations.
    """
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        return a / b
    return "Неизвестная операция"


def count_chars(text: str) -> dict[str, int]:
    """
    Count occurrences of each character in the given text.
    """
    counts: dict[str, int] = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def is_palindrome(word: str) -> bool:
    """
    Check whether a word is a palindrome, ignoring letter case.
    """
    normalized = word.casefold()
    return normalized == normalized[::-1]


def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_and_product_from_input() -> None:
    """
    Request a space-separated list of numbers and print their sum and product.
    """
    raw = input("Введите числа через пробел: ").split()
    numbers = [float(item) for item in raw]

    total = 0.0
    for num in numbers:
        total += num

    product = 1.0
    for num in numbers:
        product *= num

    print(f"Сумма: {total}")
    print(f"Произведение: {product}")


def primes_up_to_n() -> None:
    """
    Request a number N and print all primes in range [2, N].
    """
    n = int(input("Введите N: "))
    primes: list[int] = []

    for candidate in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)

    print("Простые числа:", " ".join(str(num) for num in primes))


def guess_the_number() -> None:
    """
    Guess-the-number game with attempt counter.
    """
    secret = randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Угадайте число (1-100): "))
        attempts += 1

        if guess == secret:
            print(f"Верно! Количество попыток: {attempts}")
            break
        if guess < secret:
            print("Больше")
        else:
            print("Меньше")


def deposit_simulator() -> None:
    """
    Simulate a deposit growth until it reaches the target amount.
    """
    principal = float(input("Начальная сумма: "))
    rate = float(input("Годовая ставка (в %): "))
    target = float(input("Желаемая сумма: "))

    years = 0
    amount = principal
    while amount < target:
        amount += amount * rate / 100
        years += 1

    print(f"Потребуется {years} лет. Итоговая сумма: {amount:.2f}")


def input_validator() -> int:
    """
    Request a positive integer until the user provides a valid value.
    Returns the validated number.
    """
    while True:
        raw = input("Введите положительное целое число: ")
        if not raw.isdigit():
            print("Некорректный ввод, попробуйте снова.")
            continue
        value = int(raw)
        if value <= 0:
            print("Число должно быть > 0.")
            continue
        print(f"Принято: {value}")
        return value


def calculator_with_stop() -> None:
    """
    Simple calculator that stops when the user enters 'стоп'.
    """
    print("Введите 'стоп' в любом поле, чтобы выйти.")
    while True:
        first_raw = input("Первое число: ")
        if first_raw.lower() == "стоп":
            break

        operator = input("Оператор (+, -, *, /): ")
        if operator.lower() == "стоп":
            break

        second_raw = input("Второе число: ")
        if second_raw.lower() == "стоп":
            break

        if operator not in {"+", "-", "*", "/"}:
            print("Неизвестный оператор.")
            continue

        try:
            a = float(first_raw)
            b = float(second_raw)
        except ValueError:
            print("Введите корректные числа.")
            continue

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        else:
            if b == 0:
                print("Деление на ноль запрещено.")
                continue
            result = a / b

        print(f"Результат: {result}")


def sequence_analyzer() -> None:
    """
    Keep reading numbers until two identical in a row or sum exceeds 100.
    """
    last_value = None
    total = 0.0
    count = 0

    while True:
        raw = input("Введите число: ")
        try:
            value = float(raw)
        except ValueError:
            print("Некорректное число, попробуйте снова.")
            continue

        total += value
        count += 1

        if last_value is not None and value == last_value:
            print("Введены два одинаковых числа подряд. Остановка.")
            break
        if total > 100:
            print("Сумма превысила 100. Остановка.")
            break

        last_value = value

    print(f"Количество чисел: {count}")
    print(f"Сумма: {total}")


def min_max_with_flag() -> None:
    """
    Read positive numbers until 0 is entered. Ignore negatives.
    """
    min_value = None
    max_value = None

    while True:
        raw = input("Введите число (0 для завершения): ")
        try:
            value = float(raw)
        except ValueError:
            print("Некорректное число, попробуйте снова.")
            continue

        if value == 0:
            break
        if value < 0:
            print("Отрицательное число игнорируется.")
            continue

        if min_value is None or value < min_value:
            min_value = value
        if max_value is None or value > max_value:
            max_value = value

    if min_value is None:
        print("Не было введено ни одного положительного числа.")
    else:
        print(f"Минимум: {min_value}, максимум: {max_value}")


