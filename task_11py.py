import datetime
import inspect


def deco(func):
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} was called in {datetime.datetime.now()}")
        return func(*args, **kwargs)

    return wrapper


@deco
def my_function():
    print("This is my function")

my_function()
