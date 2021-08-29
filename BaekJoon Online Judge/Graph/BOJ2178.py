import collections

# Keep track of visited nodes in a boolean list
# Keep track of distances in a single "cnt" variable (increment it in each step)
# N, M = map(int, input().split())
# graph = [list(input().strip()) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
# visited[0][0] = True
# Q = collections.deque([(0,0)]) # (row, column)
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
#
#
# def bfs():
#     cnt = 0
#     while Q:
#         cnt += 1
#         for _ in range(len(Q)):
#             r, c = Q.popleft()
#             if r == N-1 and c == M-1:
#                 return cnt
#             for i in range(len(dy)):
#                 next_r = r + dy[i]
#                 next_c = c + dx[i]
#                 if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M \
#                         or visited[next_r][next_c] \
#                         or graph[next_r][next_c] == '0':
#                     continue
#                 visited[next_r][next_c] = True
#                 Q.append((next_r, next_c))
#     return -1
#
#
# print(bfs())


# Keep track of visited nodes, path lengths in a single integer list
N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
Q = collections.deque([(0,0)]) # (row, column)
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs():
    while Q:
        r, c = Q.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c]
        for i in range(len(dy)):
            next_r = r + dy[i]
            next_c = c + dx[i]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M \
                    or visited[next_r][next_c] > 0 \
                    or graph[next_r][next_c] == '0':
                continue
            visited[next_r][next_c] = visited[r][c] + 1
            Q.append((next_r, next_c))
    return -1


print(bfs())


# Keep track of "visited nodes" in boolean list and
# "path lengths" in integer list
# N, M = map(int, input().split())
# graph = [list(input().strip()) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
# visited[0][0] = True
# dist = [[0 for _ in range(M)] for _ in range(N)]
# dist[0][0] = 1
# Q = collections.deque([(0,0)]) # (row, column)
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
#
#
# def bfs():
#     while Q:
#         r, c = Q.popleft()
#         if r == N-1 and c == M-1:
#             return dist[r][c]
#         for i in range(len(dy)):
#             next_r = r + dy[i]
#             next_c = c + dx[i]
#             if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M \
#                     or visited[next_r][next_c] \
#                     or graph[next_r][next_c] == '0':
#                 continue
#             visited[next_r][next_c] = True
#             dist[next_r][next_c] = dist[r][c] + 1
#             Q.append((next_r, next_c))
#     return -1
#
#
# print(bfs())



# Keep track of path lengths in the Queue -> Out of Memory
# N, M = map(int, input().split())
# graph = [list(input().strip()) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
# visited[0][0] = True
# Q = collections.deque([(0,0,1)]) # (row, column, path length)
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
#
#
# def bfs():
#     while Q:
#         r, c, length = Q.popleft()
#         if r == N-1 and c == M-1:
#             return length
#         for i in range(len(dy)):
#             next_r = r + dy[i]
#             next_c = c + dx[i]
#             if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M \
#                     or visited[next_r][next_c] \
#                     or graph[next_r][next_c] == '0':
#                 continue
#             Q.append((next_r, next_c, length+1))
#     return -1
#
#
# print(bfs())

