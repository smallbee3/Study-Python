from collections import deque

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# (1) q 중복 제거 전

# def func(q):
#     while q.queue:
#         print(q.queue)
#         person = q.get()
#
#         if person.endswith('y'):
#             return print(f'{person} is mango sales person.')
#         for person in graph[person]:
#             q.put(person)
#     return print("There is no mango sales person.")
#
#
# q = queue.Queue()
#
# for person in graph['you']:
#     q.put(person)
# func(q)


# (2) q 중복제거 후



def func(name):
    import queue
    searched = []

    q = queue.Queue()
    q.queue += graph[name]

    # while q:
    # -> q는 참이기 때문에 CLI 에서 확인하면 무한 loop를 도는 것으로 확인할 수 있음.
    while q.queue:
        print(q.queue)
        print(searched)
        person = q.get()

        if person not in searched:
            if person.endswith('m'):
                return print(f'{person} is mango sales person.')

        # check_list += person
        # -> ['a','l','i','c','e'] 가 들어가는 문제 발생.

            else:
                for p in graph[person]:
                    if p not in searched:
                        q.put(p)
                searched.append(person)

    return print("There is no mango sales person.")


func('you')


# Book answer (1)

def person_is_seller(name):
    return name[-1] == 'y'


def func2(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f'{person} is a mango seller!')
            return True
        else:
            search_queue += graph[person]
    return False


search_queue = deque()
search_queue += graph['you']
func2(search_queue)


# Book answer (2)

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
