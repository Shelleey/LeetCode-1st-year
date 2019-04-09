# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q1 = [root]
        q2 = []
        while len(q1)>0 or len(q2)>0:
            temp = []
            if len(q1)>0:
                for i in q1:
                    temp.append(i.val)
                    if i.left:
                        q2.append(i.left)
                    if i.right:
                        q2.append(i.right)
                q1=[]
            else:
                for i in q2:
                    temp.append(i.val)
                    if i.left:
                        q1.append(i.left)
                    if i.right:
                        q1.append(i.right)
                q2=[]
            res.append(temp)
        return res