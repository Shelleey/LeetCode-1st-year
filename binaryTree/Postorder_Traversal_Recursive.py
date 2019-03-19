# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.postorder(root)
        return self.res
    def postorder(self,root):
        if not root:
            return
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        self.res.append(root.val)