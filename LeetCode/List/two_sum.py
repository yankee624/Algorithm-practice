from typing import *

class Solution:
    # one-pass hash table
    # Don't have to put everything in dict at the beginning. (May be waste if end early)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            if target - num in num_dict and num_dict[target - num] != idx:
                return [idx, num_dict[target - num]]
            num_dict[num] = idx

    # two-pass hash table
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     num_dict = {}
    #     for idx, num in enumerate(nums):
    #         num_dict[num] = idx
    #
    #     for i in range(len(nums)):
    #         if target - nums[i] in num_dict and num_dict[target-nums[i]] != i:
    #             return [i, num_dict[target-nums[i]]]

    # brute-force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]+nums[j] == target:
    #                 return [i, j]

s = Solution()
print(s.twoSum([2,7,11,15], 9))