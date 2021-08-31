from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # post-order traversal
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


s = Solution()
print(s.invertTree(
    TreeNode(2, TreeNode(1), TreeNode(3))
).val)