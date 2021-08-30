from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest_length = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def calc_path(node: Optional[TreeNode]):
            if node is None:
                return -1
            left = calc_path(node.left) + 1
            right = calc_path(node.right) + 1
            if node.left is None or node.left.val != node.val:
                left = 0
            if node.right is None or node.right.val != node.val:
                right = 0
            length = left + right
            self.longest_length = max(self.longest_length, length)
            return max(left, right)

        if root is None:
            return 0
        calc_path(root)
        return self.longest_length


s = Solution()
print(s.longestUnivaluePath(
    TreeNode(5,
             TreeNode(4,
                      TreeNode(1), TreeNode(1)),
             TreeNode(5,
                      None, TreeNode(5)))
))