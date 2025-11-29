def my_decorator(func):
    def wrapper():
        print("Something before function runs")
        func()
        print("Something after function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
