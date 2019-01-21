import bisect
import random
import time

SIZE = 7

random.seed(1729)
# random.seed(time.time())

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
