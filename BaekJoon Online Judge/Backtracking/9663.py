# Faster but still timeout:
# For each row, find which column queen can be placed.
# Check if each column is possible on-demand
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



# Very slow method: Whenever put a queen, block the places where the queen can reach
# N = int(input())
#
# answer = 0
# board = [[0 for _ in range(N)] for _ in range(N)]
#
#
# def nqueen(idx, cnt):
#     if cnt == N:
#         global answer
#         answer += 1
#         return
#     if idx == N * N:
#         return
#
#     row = idx // N
#     col = idx % N
#     if board[row][col] == 0:
#         # put queen
#         block_idxs = {(row, col)}
#         for r in range(N):
#             if board[r][col] == 0:
#                 block_idxs.add((r,col))
#             c = r - row + col
#             if 0 <= c < N and board[r][c] == 0:
#                 block_idxs.add((r, c))
#             c = -r + row + col
#             if 0 <= c < N and board[r][c] == 0:
#                 block_idxs.add((r, c))
#         for c in range(N):
#             if board[row][c] == 0:
#                 block_idxs.add((row, c))
#
#         for (r, c) in block_idxs:
#             board[r][c] = 1
#         nqueen(idx+1, cnt+1)
#         for (r, c) in block_idxs:
#             board[r][c] = 0
#     nqueen(idx+1, cnt)
#
# nqueen(0, 0)
# print(answer)

