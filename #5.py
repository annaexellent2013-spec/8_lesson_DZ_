def process_list(input_list):
    try:
        assert len(input_list) >= 3
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError:
        print("Список повинен містити принаймні 3 елементи")


process_list([1, 2, 3, 4])
process_list([1, 2])