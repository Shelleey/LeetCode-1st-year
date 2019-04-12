# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution ( object ):
    def recoverTree(self , root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.n1 = None
        self.n2 = None
        self.pre = None

        def finderror(root):
            if not root:
                return
            finderror ( root.left )
            if self.pre and self.pre.val > root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.pre
            self.pre = root
            finderror ( root.right )

        finderror ( root )
        self.n1.val , self.n2.val = self.n2.val , self.n1.val
        return root
