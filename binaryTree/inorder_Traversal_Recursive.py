# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root,res)
        return res
    def inorder(self,root,res):
        if not root:
            return res
        if root.left:
            self.inorder(root.left,res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right,res)