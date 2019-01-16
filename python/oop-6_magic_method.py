# -*- coding: utf-8 -*-

# class Food(object):
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __lt__(self, other):
#         if self.price < other.price:
#             return True
#         else:
#             return False
#
#
# food_1 = Food('아이스크림', 3000)
# food_2 = Food('햄버거', 5000)
# food_3 = Food('콜라', 2000)
#
# # food_2가 food_1보다 큰지 확인
# print(food_1 < food_2)  # 3000 < 5000
# print(food_2 < food_3)  # 5000 < 2000


# -*- coding: utf-8 -*-

class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


food_1 = Food('아이스크림', 3000)
food_2 = Food('햄버거', 5000)

print(food_1 + food_2)



