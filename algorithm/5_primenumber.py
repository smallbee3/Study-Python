# # Prime number Special


# (1) Prime number check
def prime_check(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print(prime_check(7))


# (2) Return prime number list
def prime_list(num):
    count = 0
    start = 1
    list = []
    while count < num:
        if prime_check(start):
            list.append(start)
            count += 1
        start += 1
    return list


# print(prime_list(5))


# (3) Return nth prime number
# def prime_nth(num):
#     count = 0
#     start = 1
#     while count < num:
#         if prime_check(start):
#             count += 1
#         start += 1
#     return start-1
#
#
# print(prime_nth(52))
