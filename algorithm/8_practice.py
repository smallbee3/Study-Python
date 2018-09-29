# 8-1
# -> 집합 커버링 문제, set_covering problem

# box size
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7

# truck size
truck_size = 20


def min_box(list):

    if len(list) == 0:
        return
    elif len(list) == 1:
        return list[0]
    else:
        # if list[0] < list[1]:
        #     min = list[0]
        # else:
        #     min = list[1]
        min = list[0] if list[0] < list[1] else list[1]

        sub_min = None
        if len(list) != 2:
            sub_min = min_box(list[2:])
        if sub_min != None and sub_min < min:
            min = sub_min
        return min


def max_box(list):

    if len(list) == 0:
        return
    elif len(list) == 1:
        return list[0]
    else:
        # if list[0] < list[1]:
        #     min = list[0]
        # else:
        #     min = list[1]
        max = list[0] if list[0] > list[1] else list[1]

        sub_max = None
        if len(list) != 2:
            sub_max = max_box(list[2:])
        if sub_max != None and sub_max > max:
            max = sub_max
        return max


def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def greedy():

    box_needed = [a, b, c, d, e, f, g]

    truck_occupied_space = 0
    truck_stuff = []

    while truck_size - truck_occupied_space > min_box(box_needed):
        # for box in box_needed:
            # if biggest_box < box:
            #     biggest_box = box
        biggest_box = max_box(box_needed)
        biggest_box_index = binary_search(box_needed, biggest_box)

        if biggest_box <= truck_size - truck_occupied_space:
            truck_occupied_space += biggest_box
            truck_stuff.append(biggest_box)
        del box_needed[biggest_box_index]

    return truck_stuff


print(greedy())
