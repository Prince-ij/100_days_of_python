import time


def speed_calc_decorator(func):
    def wrapper():
        current_time = time.time()
        print(f"Starting {func.__name__} at {current_time:.2f}")
        func()
        print(f"It took {time.time() - current_time:.2f}secs to run")

    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
