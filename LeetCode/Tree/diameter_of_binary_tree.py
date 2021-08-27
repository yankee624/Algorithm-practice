from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calc_height(node: TreeNode):
            if node is None:
                return -1
            left_height = calc_height(node.left)
            right_height = calc_height(node.right)
            diameter = left_height + 1 + right_height + 1
            nonlocal max_diameter # To perform re-assign on the "outer variable"
            if diameter > max_diameter:
                max_diameter = diameter
            height = max(left_height, right_height) + 1
            return height

        if root is None:
            return 0
        max_diameter = 0
        calc_height(root)
        return max_diameter


s = Solution()
print(s.diameterOfBinaryTree(
    TreeNode(1,
             TreeNode(2,
                      TreeNode(4),
                      TreeNode(5)),
             TreeNode(3))))
