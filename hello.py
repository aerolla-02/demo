def hello_world_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello World")
        result = func(*args, **kwargs)
        print("Hello World")
        return result
    return wrapper

@hello_world_decorator
def sample_function():
    print("Executing the main program...")

sample_function()
 