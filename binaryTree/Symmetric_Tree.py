# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursiveTree(root.left,root.right)
    def recursiveTree(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val==right.val) and self.recursiveTree(left.left,right.right) and self.recursiveTree(left.right,right.left)