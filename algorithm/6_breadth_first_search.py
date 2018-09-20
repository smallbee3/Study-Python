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
