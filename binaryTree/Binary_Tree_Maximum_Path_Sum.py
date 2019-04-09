# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution ( object ):
    def maxPathSum(self , root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.curr_max = float ( '-inf' )

        def get_max(root):
            if not root:
                return 0
            left = max ( 0 , get_max ( root.left ) )
            right = max ( 0 , get_max ( root.right ) )
            self.curr_max = max ( self.curr_max , left + right + root.val )
            return max ( left , right ) + root.val

        get_max ( root )
        return self.curr_max
