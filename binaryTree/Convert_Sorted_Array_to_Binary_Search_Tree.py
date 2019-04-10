# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def iteraterTree(nums,low,high):
            if low>high:
                return None
            mid = int((high+low)/2)
            root = TreeNode(nums[mid])
            root.left = iteraterTree(nums,low,mid-1)
            root.right = iteraterTree(nums,mid+1,high)
            return root
        return iteraterTree(nums,0,len(nums)-1)