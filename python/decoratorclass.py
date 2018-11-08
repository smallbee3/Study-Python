
# Decorator Class

# __init__ method in DecoratorClass works as the arguments of decorator function.
# And __call__ method works as a wrapper function of decorator function.


class DecoratorClass:  #1
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# @DecoratorClass  #2
# def display():
#     print('display 함수가 실행됐습니다.')
#
#
# @DecoratorClass  #3
# def display_info(name, age):
#     print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


def display():
    print('display 함수가 실행됐습니다.')


def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display = DecoratorClass(display)
display_info = DecoratorClass(display_info)


display()
print()
display_info('John', 25)
