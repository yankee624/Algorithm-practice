import itertools
from typing import *

class Solution:
    # Find the last increasing number pair -> Get next permutation
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     def next_permutation(perm):
    #         i = len(perm) - 1
    #         while i - 1 >= 0 and perm[i-1] >= perm[i]:
    #             i -= 1
    #         # All decreasing - last permutation
    #         if i == 0:
    #             return False
    #
    #         # Insert next larger number into position i-1
    #         j = len(perm) - 1
    #         while perm[j] < perm[i-1]:
    #             j -= 1
    #         perm[i-1], perm[j] = perm[j], perm[i-1]
    #
    #         j = len(perm) - 1
    #         while i < j:
    #             perm[i], perm[j] = perm[j], perm[i]
    #             i += 1
    #             j -= 1
    #         return True
    #
    #     result = [nums[:]]
    #     while next_permutation(nums):
    #         result.append(nums[:]) # copy
    #
    #     return result


    # Use itertools
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return list(itertools.permutations(nums))

    # Reuse list of current numbers (append&pop) + Make list of remaining numbers every time
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def search(remaining: List[int]):
            if len(remaining) == 0:
                result.append(curr[:]) # copy
                return
            for num in remaining:
                new_remaining = remaining[:] # copy
                new_remaining.remove(num)
                curr.append(num)
                search(new_remaining)
                curr.pop()
        search(nums)
        return result

    # Make list of current numbers every time + Search remaining numbers every time
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     def search(curr: List[int]):
    #         if len(curr) == len(nums):
    #             result.append(curr)
    #             return
    #         for num in nums:
    #             if num not in curr:
    #                 search(curr + [num])
    #     search([])
    #     return result

s = Solution()
print(s.permute([1, 2, 3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]