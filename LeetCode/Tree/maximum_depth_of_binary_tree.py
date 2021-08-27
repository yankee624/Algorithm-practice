from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        Q = collections.deque([root])
        while Q:
            depth += 1
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
        return depth


s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxDepth(root))

