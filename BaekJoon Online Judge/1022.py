# 소용돌이 예쁘기 출력하기
# https://www.acmicpc.net/problem/1022

def num(r, c):
    n = max(abs(r), abs(c))
    if r == c == n:
        return (2*n+1)**2
    if r == n:
        return (2*n+1)**2 - (n-c)
    if c == -n:
        return (2*n+1)**2 - (2*n) - (n-r)
    if r == -n:
        return (2*n+1)**2 - 2*(2*n) - (n+c)
    if c == n:
        return (2*n+1)**2 - 3*(2*n) - (n+r)
    return n

r1, c1, r2, c2 = map(int, input().split())
max_num = max(num(r1,c1), num(r1,c2), num(r2,c1), num(r2,c2)) # 최대값은 항상 꼭짓점에서 발생
max_length = len(str(max_num))

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print('{:>{width}}'.format(num(i, j), width=max_length), end=' ')
    print()
