# Timing function execution

"""
Write a decorator that measures the time a function takes to execute.
"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time}")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)