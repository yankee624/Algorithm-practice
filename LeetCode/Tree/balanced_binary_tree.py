from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_height(node: Optional[TreeNode]):
            if node is None:
                return 0
            left_height = calc_height(node.left)
            right_height = calc_height(node.right)
            if abs(left_height - right_height) > 1:
                self.result = False
            return max(left_height+1, right_height+1)

        calc_height(root)
        return self.result


s = Solution()
print(s.isBalanced(
    TreeNode(1,
             TreeNode(2,
                      TreeNode(3,
                               TreeNode(4), TreeNode(4)),
                      TreeNode(3)),
             TreeNode(2))
))