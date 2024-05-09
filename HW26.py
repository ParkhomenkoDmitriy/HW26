class Calculator:
    def add(self, x, y):
        try:
            return x + y
        except Exception as e:
            return f"Ошибка: {e}"

    def subtract(self, x, y):
        try:
            return x - y
        except Exception as e:
            return f"Ошибка: {e}"

    def multiply(self, x, y):
        try:
            return x * y
        except Exception as e:
            return f"Ошибка: {e}"

    def divide(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Деление на 0 невозможно")
            return x / y
        except ZeroDivisionError as e:
            return f"Ошибка: {e}"
        except Exception as e:
            return f"Ошибка: {e}"

    def power(self, x, y=2):
        try:
            if y < 0:
                return "Ошибка: Возведение в отрицательную степень"
            return x ** y
        except Exception as e:
            return f"Ошибка: {e}"

    def square_root(self, x, y=2):
        try:
            if x < 0:
                return "Ошибка: Извлечение корня из отрицательного числа"
            return x ** (1 / y)
        except Exception as e:
            return f"Ошибка: {e}"


calc = Calculator()

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Извлечение корня")

choice = input("Введите номер операции: ")

if choice in ["1", "2", "3", "4"]:
    try:
        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y: "))
    except ValueError as e:
        print("Ошибка ввода данных. Пожалуйста, вводите числовые значения.")
    else:
        if choice == "1":
            print("Сложение:", calc.add(x, y))
        elif choice == "2":
            print("Вычитание:", calc.subtract(x, y))
        elif choice == "3":
            print("Умножение:", calc.multiply(x, y))
        elif choice == "4":
            print("Деление:", calc.divide(x, y))
elif choice == "5":
    try:
        x = float(input("Введите значение x: "))
        power = float(input("Введите значение степени (по умолчанию 2): "))
        print("Возведение в степень:", calc.power(x, power))
    except ValueError as e:
        print("Ошибка ввода данных. Пожалуйста, введите числовые значения.")
elif choice == "6":
    try:
        x = float(input("Введите значение x: "))
        root_power = float(input("Введите значение корня степени (по умолчанию 2): "))
        print("Извлечение корня x:", calc.square_root(x, root_power))
    except ValueError as e:
        print("Ошибка ввода данных. Пожалуйста, введите числовые значения.")
else:
    print("Некорректный выбор операции. Пожалуйста, выберите снова.")
