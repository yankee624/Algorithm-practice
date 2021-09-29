N, M = map(int, input().split())

board = [[0 for _ in range(M+1)] for _ in range(N+1)]

answer = 0
def dfs(idx):
    if idx == N * M:
        global answer
        answer += 1
        return

    r = idx // M + 1
    c = idx % M + 1
    if board[r][c-1] == 0 or board[r-1][c] == 0 or board[r-1][c-1] == 0:
        board[r][c] = 1
        dfs(idx + 1)
        board[r][c] = 0
    dfs(idx + 1)


dfs(0)
print(answer)
