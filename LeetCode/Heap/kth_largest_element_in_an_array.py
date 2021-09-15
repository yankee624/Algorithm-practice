from typing import *
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

    # Slightly Faster... Python sorting implementation is very efficient!
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums, reverse=True)[k-1]


s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))

