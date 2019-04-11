# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution ( object ):
    def binaryTreePaths(self , root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = [ ]

        def DFS(root , path):
            if not root:
                return
            if not root.left and not root.right:
                path = path + str ( root.val )
                self.res.append ( path )
            path = path + str ( root.val ) + '->'
            if root.left:
                DFS ( root.left , path )
            if root.right:
                DFS ( root.right , path )

        DFS ( root , '' )
        return self.res