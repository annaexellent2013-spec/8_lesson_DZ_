import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
user_date = input("Введіть дату у форматі рік-місяць-день: ")
message = f"Повідомлення рівня INFO на дату {user_date}"

logging.info(message)