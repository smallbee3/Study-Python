
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


def square_numbers(nums):
    for i in nums:
        yield i * i


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)


# 1) next() 함수를 통해 리스트 값 출력
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))


# 2) StopIteration 예외가 발생
# print(next(my_nums))


# 3) 제너레이터는 일반적으로 for 루프를 통해서 호출하여 사용
for i in my_nums:
    # print(next(i))
    print(i)


# 4) for complehension -> generator
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)

my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)
