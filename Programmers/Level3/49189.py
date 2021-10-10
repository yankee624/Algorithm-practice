import collections

def solution(n, edge):
    graph = collections.defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    farthest_nodes = graph[1]
    visited = set(farthest_nodes)
    visited.add(1)
    while len(visited) < n:
        new_farthest_nodes = []
        for farthest_node in farthest_nodes:
            for neighbor_node in graph[farthest_node]:
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    new_farthest_nodes.append(neighbor_node)
        farthest_nodes = new_farthest_nodes

    return len(farthest_nodes)
