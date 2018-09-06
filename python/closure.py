# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()
#
# my_function = outer_func()
#
# my_function
# print(my_function)         # -> None 출력
# print(type(my_function))   # -> <class 'NoneType'>
# # my_function()            # -> NoneType object is not callable.


# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()

# outer_func()
# print(outer_func())
# print(type(outer_func()))

# my_function = outer_func()
# my_function()
# my_function()
# my_function()


# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# my_func = outer_func()
#
# print(my_func)
# print()
# print(dir(my_func))
# print()
# print(type(my_func.__closure__))
# print()
# print(my_func.__closure__)
# print()
# print(my_func.__closure__[0])
# print()
# print(dir(my_func.__closure__[0]))
# print()
# print(my_func.__closure__[0].cell_contents)

# def outer_func(tag):
#     text = 'Some text'
#     tag = tag
#
#     def inner_func():
#         print('<{}>{}<{}>'.format(tag, text, tag))
#
#     return inner_func
#
#
# outer_func('h1')()
# outer_func('p')()
#
# h1_func = outer_func('h1')
# p1_func = outer_func('p')
#
# h1_func()
# p1_func()


def outer_func(tag):
    tag = tag

    def inner_func(txt):
        print('<{}>{}<{}>'.format(tag, txt, tag))

    return inner_func


outer_func('h1')('이게뭣이냐')
outer_func('p')('몰라나')

h1_func = outer_func('h1')
p1_func = outer_func('p')

h1_func('h1태그의 안입니다.')
p1_func('p태그의 안입니다.')
