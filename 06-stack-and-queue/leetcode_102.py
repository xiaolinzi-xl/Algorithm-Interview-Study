# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LevelNode:
    def __init__(self, order, node):
        self.order = order
        self.node = node


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        res = []
        queue.append(LevelNode(1, root))

        while len(queue) != 0:
            levelNode = queue.pop(0)
            node = levelNode.node
            i = levelNode.order
            if len(res) < i:
                res.append([])
            res[i-1].append(node.val)
            if node.left:
                queue.append(LevelNode(i+1, node.left))
            if node.right:
                queue.append(LevelNode(i+1, node.right))

        return res
