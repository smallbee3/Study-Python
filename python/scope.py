
# (1)
# https://github.com/Fastcampus-WPS-7th/Python/blob/master/lecture/09.%20함수.md#로컬-스코프에서-글로벌-스코프의-변수를-사용
#
# champion = 'Lux'
#
# def change_global_champion():
#     champion = 'Ahri'
#     print('after change_global_champion : {}'.format(champion))
#
# change_global_champion()
# print('print global champion : {}'.format(champion))


# (2)
# https://github.com/Fastcampus-WPS-7th/Python/blob/master/lecture/09.%20함수.md#내부함수에서의-로컬-스코프-nonlocal

# champion = 'Lux'
#
# def change_global_champion():
#     global champion
#     champion = 'Ahri'
#     print('after change_global_champion : {}'.format(champion))
#
# change_global_champion()
# print('print global champion : {}'.format(champion))


# (3)
# https://github.com/Fastcampus-WPS-7th/Python/blob/master/lecture/09.%20함수.md#내부함수에서의-로컬-스코프-nonlocal

# champion = 'Lux'
#
# def local1():
#     champion = 'Ahri'
#     print('local1 locals() : {}'.format(locals()))
#
#     def local2():
#         champion = 'Ezreal'
#         print('local2 locals() : {}'.format(locals()))
#     local2()
#     print('local1 locals() : {}'.format(locals()))
#
#
# print('global locals() : {}'.format(locals()))
# local1()


# champion = 'Lux'
#
# def local1():
#     champion = 'Ahri'
#     print('local1 locals() : {}'.format(locals()))
#
#     def local2():
#         nonlocal champion
#         champion = 'Ezreal'
#         print('local2 locals() : {}'.format(locals()))
#     local2()
#     print('local1 locals() : {}'.format(locals()))
#
# print('global locals() : {}'.format(locals()))
# local1()
# print('global locals() : {}'.format(locals()))


# (4)
# https://github.com/Fastcampus-WPS-7th/Python/blob/master/lecture/09.%20함수.md#global키워드와-인자argument전달의-차이

# global_level = 100
# def level_add(value):
#     value += 30
#     print(value)
#
# level_add(global_level)
# print(global_level)


# global_level = 100
# def level_add():
#     global global_level
#     global_level += 30
#     print(global_level)
#
# level_add()
# print(global_level)


# 아래코드는 불가
# Name 'value' used both as a parameter and as a global
# global_level = 100
# def level_add(value):
#     global value
#     value += 30
#     print(value)
#
# level_add(global_level)
# print(global_level)


# 하지만 리스트 변수가 전달된다면?
# SyntaxError: name 'value' is assigned to before global declaration
global_level = 100
def level_add(list):
    value = list[0]
    global value
    value += 30
    print(value)

level_add([global_level])
print(global_level)
