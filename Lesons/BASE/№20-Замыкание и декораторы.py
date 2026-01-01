

def count_calls(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} было вызвана:{count} раз')
        return func(*args)

    return wrapper



@count_calls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
greet("Charlie")
