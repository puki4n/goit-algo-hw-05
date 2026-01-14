def caching_fibonacci():
    # 1. Створюємо вільну змінну (кеш)
    cache = {}

    # 2. Визначаємо внутрішню функцію
    def fibonacci(n):
        # Базові випадки (щоб рекурсія не була нескінченною)
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # 3. Перевіряємо, чи є вже обчислене значення в кеші
        if n in cache:
            return cache[n]

        # 4. Якщо немає в кеші — обчислюємо рекурсивно
        # і одразу записуємо результат у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    # 5. Повертаємо внутрішню функцію
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(f"Fib(10): {fib(10)}")
print(f"Fib(15): {fib(15)}")

#print(fib.__closure__[0].cell_contents)
