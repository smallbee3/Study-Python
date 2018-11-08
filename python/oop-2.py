

def my_function():
    """
    my_function에 대한 설명입니다~!
    """
    pass


# my_function의 속성 확인
print('dir(my function)')
print(dir(my_function), '\n' )

# my_function의 docstring 출력
print( 'my_function.__doc__' )
print( my_function.__doc__, '\n' )

# my_function에 새로운 속성 추가
my_function.new_variable = '새로운 변수입니다.'

# 추가된 속성 확인
print( 'dir(my_function)' )
print( dir(my_function), '\n' )

# 추가한 속성값 출력
print( 'my_function.new_variable' )
print( my_function.new_variable, '\n' )
