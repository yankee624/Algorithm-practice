import collections

N = int(input())
graph = collections.defaultdict(list)
for i in range(int(input())):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)


def dfs(node):
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)


visited = {1}
dfs(1)
print(len(visited)-1)