# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function
#
# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
#
# hi_func()
# bye_func()


# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
# def display():
#     print('display 함수가 실행됐습니다.')
#
# decorated_display = decorator_function(display)
#
# decorated_display()


# def decorator_function(original_function):
#     def wrapper_function():
#         print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function
#
# @decorator_function   # 1
# def display_1():
#     print('display_1 함수가 실행됐습니다.')
#
# @decorator_function   # 2
# def display_2():
#     print('display 함수가 실행됐습니다.')
#
# # display_1 = decorator_function(display_1)
# # display_2 = decorator_function(display_2)
#
# display_1()
# print()
# display_2()




# def decorator_function(original_function):
#     def wrapper_function(*args):
#         print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
#         return original_function(*args)
#
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display 함수가 실행됐습니다.')
#
#
# @decorator_function
# def display_info(name, age):
#     print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))
#
#
# display()
# print()
# display_info('John', 25)


# -*- coding: utf-8 -*-
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):  # 1
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result
        # return original_function(*args, **kwargs)

    return wrapper


@my_timer  # 2
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display_info('John', 25)
