# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self , root: TreeNode) -> bool:
        self.flag = True
        self.recursiveTree ( root )
        return self.flag

    def recursiveTree(self , root):
        if not root or not self.flag:
            return 0
        left = self.recursiveTree ( root.left )
        right = self.recursiveTree ( root.right )
        if abs ( left - right ) > 1:
            self.flag = False
        return left + 1 if left > right else right + 1
