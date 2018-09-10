# fibonachi by recursion
from helper import my_timer


def fibo(num):
    # arr = [1, 1]
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(7))


# fibonacchi arr 출력(1)
@my_timer
def fibo_arr(num):

    fibo_list = []
    # fibo_list = [1, 1]
    #
    # if num == 1:
    #     return fibo_list[0]
    # elif num == 2:
    #     return fibo_list[1]
    # else:
    # for i in range(1, num+1):
    for i in range(num):
        fibo_list.append(fibo(i+1))
    return fibo_list


print(fibo_arr(5))


# fibonacchi arr 출력(2) - without recursion
@my_timer
def fibo_arr2(num):

    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fibo_list = [1, 1]
        for i in range(2, num):
            result = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.append(result)
        return fibo_list


print(fibo_arr2(10))


# fibonachi without recursion
def fibo2(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, num):
            c = a + b
            print(a, b, c)
            a = b
            b = c
        return c


print(fibo2(3))
