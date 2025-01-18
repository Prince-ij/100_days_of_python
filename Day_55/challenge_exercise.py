# create logging decorator function

def logging(func):
    def wrapper(*args):
        print(f"Function name is {func.__name__}.")
        print("The arguments are :")
        for arg in args:
            print(arg)
        print(f"The return value of the function is {func(*args)}.")

    return wrapper

@logging
def add(a, b, c):
    return a + b + c

add(1, 2, 4)
