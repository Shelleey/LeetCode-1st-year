# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self , root: TreeNode) -> List[ int ]:
        res = [ ]
        if not root:
            return res
        stack = [ root ]
        while len ( stack ) > 0:
            root = stack.pop ( )
            res.append ( root.val )
            if root.left:
                stack.append ( root.left )
            if root.right:
                stack.append ( root.right )
        return res[ ::-1 ]