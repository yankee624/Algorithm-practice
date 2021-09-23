from typing import *
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1: str, n2: str) -> int:
            a = n1 + n2
            b = n2 + n1
            if a > b:
                return -1
            elif a == b:
                return 0
            else:
                return 1

        nums = map(str, nums)
        nums = sorted(nums, key=cmp_to_key(compare))
        print(nums)
        return str(int("".join(nums)))


s = Solution()
print(s.largestNumber([3,30,34,5,9]))

