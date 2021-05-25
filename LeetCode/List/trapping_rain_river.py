from typing import *

class Solution:
    # Stack based: O(n)
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume

    # O(N^2)
    # def trap(self, height: List[int]) -> int:
    #     trapped = 0
    #     # Start from the idx where the first decrease of height occurs.
    #     # Before this, no rain will be trapped.
    #     curr_idx = 1 # curr_idx is the first idx where height decreases
    #     while curr_idx < len(height) and height[curr_idx - 1] <= height[curr_idx]:
    #         curr_idx += 1
    #     start_idx = curr_idx - 1
    #
    #     for idx in range(curr_idx+1, len(height)):
    #         prev_height = height[idx-1]
    #         curr_height = height[idx]
    #         # rain is trapped when height increases
    #         if prev_height < curr_height:
    #             # search backward for height that was higher than prev_height
    #             for backward_idx in range(idx-2, start_idx-1, -1):
    #                 if height[backward_idx] > prev_height:
    #                     new_prev_height = min(curr_height, height[backward_idx])
    #                     trapped += (new_prev_height - prev_height) * (idx-1 - backward_idx)
    #                     # previous height became higher than current height: No more trap is possible
    #                     if new_prev_height == curr_height: break
    #                     # update prev_height
    #                     prev_height = height[backward_idx]
    #     return trapped


s = Solution()
print(s.trap([4,2,0,3,2,5]))