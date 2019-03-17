# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root,res)
        return res
    def preorder(self,root,res):
        if not root:
            return res
        res.append(root.val)
        if root.left:
            self.preorder(root.left,res)
        if root.right:
            self.preorder(root.right,res)