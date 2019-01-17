# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        res = self.findPath(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)

        return res

    def findPath(self, root, sum):
        if root is None:
            return 0

        res = 0
        if root.val == sum:
            res += 1
        res += self.findPath(root.left, sum - root.val)
        res += self.findPath(root.right, sum - root.val)

        return res
