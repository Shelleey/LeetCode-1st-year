# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self , root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str ( root.val ) + ',' + self.serialize ( root.left ) + ',' + self.serialize ( root.right )

    def deserialize(self , data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        li = data.split ( ',' )
        return self._deser ( li )

    def _deser(self , li):
        if len ( li ) <= 0:
            return None
        val = li.pop ( 0 )
        root = None
        if val != '#':
            root = TreeNode ( int ( val ) )
            root.left = self._deser ( li )
            root.right = self._deser ( li )
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))