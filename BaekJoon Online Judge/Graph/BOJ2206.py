import collections

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
# Don't do [[0,0]]*M ! It will shallow copy the same [0,0] object M times.
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # NxMx2 : visited (N,M) with broke=0, broke=1
visited[0][0][0] = 1
Q = collections.deque([(0,0,0)]) # (row, column, broke wall)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while Q:
        r, c, broke = Q.popleft()
        if r == N-1 and c == M-1:
            print(visited[r][c][broke])
            return
        for i in range(4):
            next_r = r + dy[i]
            next_c = c + dx[i]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            # Node shouldn't have been visited before with equal or more "break chance" than now
            if visited[next_r][next_c][0] > 0 or (visited[next_r][next_c][1] > 0 and broke == 1):
                continue

            if graph[next_r][next_c] == '0':
                visited[next_r][next_c][broke] = visited[r][c][broke] + 1
                Q.append((next_r, next_c, broke))
            else:
                if broke == 0:
                    visited[next_r][next_c][1] = visited[r][c][broke] + 1
                    Q.append((next_r, next_c, 1))
    print(-1)


bfs()






