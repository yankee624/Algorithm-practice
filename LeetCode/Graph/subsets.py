from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr: List[int], start_idx):
            result.append(curr[:])
            for i in range(start_idx, len(nums)):
                num = nums[i]
                curr.append(num)
                dfs(curr, i+1)
                curr.pop()

        result = []
        dfs([], 0)
        return result


s = Solution()
print(s.subsets([1, 2, 3]))
