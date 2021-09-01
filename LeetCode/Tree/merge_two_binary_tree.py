from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self, level=0):
        print("  "*level + str(self.val))
        if self.left:
            self.left.printTree(level+1)
        if self.right:
            self.right.printTree(level+1)


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        # merge into first tree
        root1.val += root2.val
        root1.left, root1.right = self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right)

        return root1


s = Solution()
s.mergeTrees(
    TreeNode(1,
             TreeNode(3,
                      TreeNode(5), None),
             TreeNode(2)),
    TreeNode(2,
             TreeNode(1,
                      None, TreeNode(4)),
             TreeNode(3,
                      None, TreeNode(7)))
).printTree()