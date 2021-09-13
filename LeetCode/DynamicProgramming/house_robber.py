from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0] * len(nums)
        for idx in range(len(nums)):
            cand1 = money[idx-2] if idx >= 2 else 0
            cand2 = money[idx-3] if idx >= 3 else 0
            money[idx] = max(cand1, cand2) + nums[idx]
        return max(money)

s = Solution()
print(s.rob([1,2,3,1]))
