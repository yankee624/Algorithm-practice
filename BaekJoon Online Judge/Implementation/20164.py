N = input()


def odds_in_num(num: str) -> int:
    cnt = 0
    for char in num:
        if int(char) % 2 == 1:
            cnt += 1
    return cnt


# Keep track of current cnt with function parameter
# Recursion will end when len(num) == 1 and update global Min, Max value
Min = float('inf')
Max = float('-inf')
def total_odds(num: str, cnt: int):
    curr_odds = odds_in_num(num)
    if len(num) == 1:
        cnt += curr_odds
        global Min
        global Max
        Min = min(Min, cnt)
        Max = max(Max, cnt)
    elif len(num) == 2:
        first = int(num[0])
        second = int(num[1])
        total_odds(str(first + second), curr_odds + cnt)
    else:
        for div1 in range(1, len(num)-1):
            for div2 in range(div1+1, len(num)):
                first = int(num[:div1])
                second = int(num[div1:div2])
                third = int(num[div2:])
                total_odds(str(first+second+third), cnt+curr_odds)


total_odds(N, 0)
print(Min, Max)


# def total_odds(num: str) -> tuple:
#     curr_odds = odds_in_num(num)
#     if len(num) == 1:
#         return curr_odds, curr_odds
#
#     if len(num) == 2:
#         first = int(num[0])
#         second = int(num[1])
#         min_odds, max_odds = total_odds(str(first + second))
#         return curr_odds + min_odds, curr_odds + max_odds
#
#     max_odds = float('-inf')
#     min_odds = float('inf')
#     for div1 in range(1, len(num)-1):
#         for div2 in range(div1+1, len(num)):
#             first = int(num[:div1])
#             second = int(num[div1:div2])
#             third = int(num[div2:])
#             min_odds_cand, max_odds_cand = total_odds(str(first+second+third))
#             if max_odds_cand > max_odds:
#                 max_odds = max_odds_cand
#             if min_odds_cand < min_odds:
#                 min_odds = min_odds_cand
#     return curr_odds + min_odds, curr_odds + max_odds
#
#
# Min, Max = total_odds(N)
# print(Min, Max)
