# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root is None:
            return res

        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res

        left_s = self.binaryTreePaths(root.left)
        for ele in left_s:
            res.append(str(root.val) + '->' + ele)

        right_s = self.binaryTreePaths(root.right)
        for ele in right_s:
            res.append(str(root.val) + '->' + ele)

        return res
