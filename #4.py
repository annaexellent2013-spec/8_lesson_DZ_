def check_age():
    age = int(input("Введіть свій вік: "))

    try:
        assert age >= 18
        print("Ви можете використовувати цей сервіс")
    except AssertionError:
        print("Вам має бути 18 років або більше")

check_age()