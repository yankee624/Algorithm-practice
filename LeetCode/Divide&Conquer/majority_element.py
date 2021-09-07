from typing import *
import collections


class Solution:
    # Divide and Conquer 2: keep track of count... doesn't improve speed
    # def majorityElement(self, nums: List[int]) -> int:
    #     def div_n_conq(partial_list: List[int]):
    #         if len(partial_list) == 1:
    #             return partial_list[0], 1
    #         left_list, right_list = partial_list[:len(partial_list)//2], partial_list[len(partial_list)//2:]
    #         left_cand, left_count = div_n_conq(left_list)
    #         right_cand, right_count = div_n_conq(right_list)
    #
    #         left_count += right_list.count(left_cand)
    #         if left_count > len(partial_list)//2:
    #             return left_cand, left_count
    #         else:
    #             return right_cand, right_count + left_list.count(right_cand)
    #     maj, _ = div_n_conq(nums)
    #     return maj

    # Divide and Conquer
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left_maj = self.majorityElement(nums[:len(nums)//2])
        right_maj = self.majorityElement(nums[len(nums)//2:])
        print(nums, left_maj, right_maj)
        if nums.count(left_maj) > len(nums)//2:
            return left_maj
        else:
            return right_maj

    # Dynamic programming
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = collections.defaultdict(int)
    #     majority = len(nums) // 2
    #     for num in nums:
    #         count[num] += 1
    #         if count[num] > majority:
    #             return num
    #     return max(count, key=count.get)


s = Solution()
print(s.majorityElement([8, 9, 8, 9, 8]))

