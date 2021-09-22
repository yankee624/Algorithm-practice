R, C, N = map(int, input().split())

board = []

for i in range(R):
    board.append(list(input()))


def put_bomb(bomb):
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = bomb


def explode(bomb):
    for i in range(R):
        for j in range(C):
            if board[i][j] == bomb:
                board[i][j] = '.'
                if i-1 >= 0 and board[i-1][j] != bomb: board[i-1][j] = '.'
                if j-1 >= 0 and board[i][j-1] != bomb: board[i][j-1] = '.'
                if i+1 < R and board[i+1][j] != bomb: board[i+1][j] = '.'
                if j+1 < C and board[i][j+1] != bomb: board[i][j+1] = '.'


for i in range(N-1):
    if i % 4 == 0:
        # X 설치
        put_bomb("X")
    if i % 4 == 2:
        # O 설치
        put_bomb("O")
    if i % 4 == 1:
        # O 폭파
        explode("O")
    if i % 4 == 3:
        # X 폭파
        explode("X")


for i in range(R):
    print("".join(board[i]).replace("X", "O"))
