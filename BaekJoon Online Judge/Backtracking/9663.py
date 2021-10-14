N = int(input())

cnt = 0
board = [-1 for _ in range(N)]


def possible(board, row, col):
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(board[i] - col):
            return False
    return True


def nqueen(n): # n: row number
    if n == N:
        global cnt
        cnt += 1
        return

    for col in range(N):
        if possible(board, n, col):
            board[n] = col
            nqueen(n+1)


nqueen(0)
print(cnt)
