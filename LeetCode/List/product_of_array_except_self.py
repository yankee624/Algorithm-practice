from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        # product of numbers in the left of the current number
        left_prod = []
        for num in nums:
            left_prod.append(prod)
            prod *= num

        prod = 1
        # multiply by numbers in the right of the current number
        for i in range(len(nums)-1, -1, -1):
            left_prod[i] *= prod
            prod *= nums[i]
        return left_prod

s = Solution()
print(s.productExceptSelf([1,2,3,4]))

