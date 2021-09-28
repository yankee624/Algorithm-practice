N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0


def search(idx, curr_sum):
    if idx == N:
        return
    if curr_sum + nums[idx] == S:
        global cnt
        cnt += 1
    search(idx+1, curr_sum)
    search(idx+1, curr_sum + nums[idx])


search(0, 0)
print(cnt)
