import queue

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def func(q):
    while q:
        print(q.queue)
        person = q.get()

        if person.endswith('y'):
            return print(f'{person} is mango sales person.')
        for person in graph[person]:
            q.put(person)
    return print("There is no mango sales person.")


q = queue.Queue()

for person in graph['you']:
    q.put(person)
func(q)


# Book answer

def person_is_seller(name):
    return name[-1] == 'y'


def fun2(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f'{person} is a mango seller!')
            return True
        else:
            search_queue += graph[person]
    return False


from collections import deque
search_queue = deque()
search_queue += graph['you']
fun2(search_queue)
