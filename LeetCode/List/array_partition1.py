from typing import *

class Solution:
    # Pythonic way
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    # Naive
    # def arrayPairSum(self, nums: List[int]) -> int:
    #     nums.sort()
    #     result = 0
    #     for idx, num in enumerate(nums):
    #         if idx % 2 == 0:
    #             result += num
    #     return result

s = Solution()
print(s.arrayPairSum([1,4,3,2]))