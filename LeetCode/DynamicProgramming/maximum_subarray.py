from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for idx in range(1, len(nums)):
            sums[idx] = sums[idx-1] + nums[idx] if sums[idx-1] > 0 else nums[idx]
        return max(sums)


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
