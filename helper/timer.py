import time


def my_timer(original_function):
    def wrapper(*args, **kwargs):

        t1 = time.time()
        print(time.time())
        result = original_function(*args, **kwargs)
        print(t1)
        print(time.time())
        t2 = time.time() - t1
        print(t2)
        print('{}함수가 실행된 총 시간: {}초'.format(original_function.__name__, t2))
        return result
    return wrapper
