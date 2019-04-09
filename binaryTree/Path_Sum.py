# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return (sum-root.val==0 and not root.left and not root.right) or self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)