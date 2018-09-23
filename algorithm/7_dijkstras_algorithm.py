
# (1) Graph
graph = {}
# node start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# node a
graph['a'] = {}
graph['a']['final'] = 1
# node b
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['final'] = 5
# node final
graph['final'] = {}

# (2) Cost
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['final'] = infinity

# (3) Parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# (4) Processed
processed = []


def closest(node):

    key_list = list(graph[node].keys())
    close_key = key_list[0]
    close_value = graph[node][close_key]
    for key in key_list[1:]:
        if close_value > graph[node][key]:
            close_value = graph[node][key]
            close_key = key
    return close_key


def update_costs_and_parents(node):
    neighbor_list = list(graph[node].keys())
    for i in neighbor_list:
        print(costs[i])
        print(graph[node][i] + costs[node])
        if costs[i] > graph[node][i] + costs[node]:
            costs[i] = graph[node][i] + costs[node]
            parents[i] = node


def next_node(fin):
    node_dict = graph
    for i in processed:
        if i in node_dict:
            del node_dict[i]
    if fin in node_dict:
        del node_dict[fin]
    print(node_dict)
    min_key = list(node_dict.keys())[0]
    min_value = costs[min_key]
    for key in list(node_dict.keys())[1:]:
        if min_value > costs[key]:
            min_value = costs[key]
            min_key = key
    return min_key


def dijkstra(str, fin):

    node = str
    while len(graph.keys()) > len(processed):
        # for i in len(graph[node]):
        #     key = graph[node][i]
        #     graph['start'][key]
        closest_node = closest(node)

        update_costs_and_parents(closest_node)

        processed.append(node)
        node = next_node(fin)

    print(f'최종가격: {costs[fin]}')

    shortest_list = [fin]
    node = fin
    while parents[node] != 'start':
        shortest_list.insert(0, parents[node])
        node = parents[node]
    shortest_list.insert(0, str)
    print(f'경로 : {shortest_list}')


dijkstra('start', 'final')
