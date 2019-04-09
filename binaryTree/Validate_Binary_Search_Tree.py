# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution ( object ):
    def isValidBST(self , root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = [ ]

        def in_order(root):
            if not root:
                return
            if root.left:
                in_order ( root.left )
            self.res.append ( root.val )
            if root.right:
                in_order ( root.right )

        in_order ( root )
        if len ( self.res ) <= 0:
            return True
        for i in range ( len ( self.res ) ):
            if i < len ( self.res ) - 1 and self.res[ i ] < self.res[ i + 1 ]:
                continue
            elif i >= len ( self.res ) - 1:
                return True
            return False

