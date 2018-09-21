
from collections import deque


# 6-2

graph = dict()
graph['CAB'] = ['CAT', 'CAR']
graph['CAT'] = ['MAT', 'BAT']
graph['CAR'] = ['CAT', 'BAR']
graph['MAT'] = ['BAT']
graph['BAR'] = ['BAT']
graph['BAT'] = []


def search(name):
    q = deque()
    q += graph[name]
    searched = []
    shortest = []
    while q:
        # print(searched)
        # print(q)
        node = q.popleft()
        # print(node)
        if node not in searched:
            if node == 'BAT':
                print('도착 최단 경로 : ')
                print(node)
                print()
                return True
            else:
                # q += graph[node]
                for n in graph[node]:
                    if n not in q and n not in searched:
                        q.append(n)
                searched.append(node)

    print('BAT까지 가는 길이 존재하지 않습니다.')
    return False


search('CAB')


# 6-3
# 올바른 것 : B
# 올바르지 않은 것 : A, C

# 6-4
# 1. 기상
# 2. 운동
# 3. 샤워
# 4. 옷 입기
# 5. 양치질
# 6. 아침 식사
# 7. 점심 도시락 싸기

# 6-5
# A - O
# B - X (가장 우측 위로가는 선 때문)
# C - O
