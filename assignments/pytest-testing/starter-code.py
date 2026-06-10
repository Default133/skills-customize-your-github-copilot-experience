def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def is_even(number):
    return number % 2 == 0


def format_greeting(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(add(2, 3))
    print(multiply(4, 5))
    print(divide(10, 2))
    print(is_even(8))
    print(format_greeting("Student"))
