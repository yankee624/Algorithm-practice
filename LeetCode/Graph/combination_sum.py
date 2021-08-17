from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr_list: List[int], curr_sum: int, start_idx: int):
            if curr_sum == target:
                result.append(curr_list[:])
                return
            if curr_sum > target:
                return
            for i in range(start_idx, len(candidates)):
                num = candidates[i]
                curr_list.append(num)
                dfs(curr_list, curr_sum + num, i)
                curr_list.pop()

        result = []
        dfs([], 0, 0)

        return result


s = Solution()
print(s.combinationSum([2,3,6,7], 7))