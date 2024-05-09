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
                return "Ошибка: Деление на 0 невозможно"
            return x / y
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

while True:
    try:
        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y: "))
        power = input("Введите значение степени (по умолчанию 2): ")
        power = float(power) if power else 2
        root_power = input("Введите значение корня степени (по умолчанию 2): ")
        root_power = float(root_power) if root_power else 2

        print("Сложение:", calc.add(x, y))
        print("Вычитание:", calc.subtract(x, y))
        print("Умножение:", calc.multiply(x, y))
        print("Деление:", calc.divide(x, y))
        print("Возведение в степень:", calc.power(x, power))
        print("Извлечение корня x:", calc.square_root(x, root_power))
        break

    except ValueError as e:
        print("Ошибка ввода данных. Пожалуйста, введите числовые значения.")
