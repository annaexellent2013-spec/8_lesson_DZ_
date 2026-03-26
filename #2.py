import logging

logging.basicConfig(level=logging.ERROR, format='%(level name)s: %(message)s')

try:
    x = int(input("Введіть число: "))
    result = 10 / x
    print(f"Результат: {result}")
except Exception as e:
    logging.error(f"Виникла помилка: {e}")