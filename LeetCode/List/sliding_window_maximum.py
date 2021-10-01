import collections
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque(nums[:k])
        max_val = max(window)
        result = [max_val]
        for i in range(k, len(nums)):
            window.append(nums[i])
            if max_val == window.popleft():
                max_val = None
            if max_val is None:
                max_val = max(window)
            else:
                if max_val < nums[i]:
                    max_val = nums[i]
            result.append(max_val)
        return result


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

