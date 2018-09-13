# 4-1 처음 나왔던 sum 함수를 작성해 보세요.
# -> 2_recursion.py 에서 풀이


# 4-2 리스트에 포함된 원소의 숫자를 세는 재귀 함수를 작성해 보세요.
def count_num(arr):
    if arr == []:
        return 0
    else:
        del arr[0]
        return 1 + count_num(arr)


print(count_num([1, 2, 3, 4, 5, 100]))


# 4-3 리스트에서 가장 큰 수를 찾아보세요.
def find_big_element(arr):
    max = arr[0]
    for i in range(len(arr)-1):
        if max < arr[i+1]:
            max = arr[i+1]

    return max


print(find_big_element([3, 10, -33, 100000, 1, 100, 2, 3]))
