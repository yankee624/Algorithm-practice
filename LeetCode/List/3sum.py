from typing import *


class Solution:
    # Fix one number & Find the others with two-pointer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            # skip same number
            if i > 0 and nums[i-1] == nums[i]: continue
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Move pointers until there is different number
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


    # Fix two numbers & Find the other with dictionary
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     nums.sort()
    #
    #     num_dict = {}
    #     for idx, num in enumerate(nums):
    #         num_dict[num] = idx
    #     prev_first_num = None
    #     prev_second_num = None
    #     for i in range(len(nums)):
    #         if nums[i] == prev_first_num: continue
    #         prev_first_num = nums[i]
    #         for j in range(i+1, len(nums)):
    #             if nums[j] == prev_second_num: continue
    #             prev_second_num = nums[j]
    #             target = -(nums[i] + nums[j])
    #             if target in num_dict and num_dict[target] > j:
    #                 result.append([nums[i], nums[j], target])
    #                 continue
    #     return result

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
