import math
from itertools import combinations

### Combination
N = int(input())
if N > 1023:
    print(-1)
else:
    reducing_nums = []
    digits = list(map(str, range(10)))
    for i in range(1, 11):
        reducing_nums.extend(sorted(list(map(lambda x: ''.join(x[::-1]), combinations(digits, i)))))
        if len(reducing_nums) >= N:
            break
    print(reducing_nums[N-1])

### Brute force
# N = int(input())
# num = 0
# count = 0
# while count < N:
#     # check if reducing number
#     is_reducing_num = True
#     fail_idx = 0
#     temp = num
#     prev = -1
#     while temp > 0:
#         curr = temp % 10
#         if curr <= prev:
#             is_reducing_num = False
#             break
#         fail_idx += 1
#         prev = curr
#         temp = temp // 10
#
#     if is_reducing_num:
#         # jump to next candidate (십의자릿수 증가시키기)
#         ones = num % 10
#         tens = int(num / 10) % 10
#         if tens == 0:
#             tens = 10
#         if count + tens-ones < N:
#             count = count + tens-ones
#             num += 10-ones
#         else:
#             num += N - count - 1
#             count = N
#
#     else:
#         # jump to next candidate (십의자릿수 증가시키기)
#         num = math.ceil(num / 10**fail_idx) * 10**fail_idx
#
# print(num)
