from time import time

def time_test(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'total time: {end_time - start_time}')
        return result
    return wrapper

@time_test
def time_gen():
    return sum(i for i in range(5000000))

@time_test
def time_list():
    return sum([i for i in range(5000000)])

print(time_gen())
print(time_list())