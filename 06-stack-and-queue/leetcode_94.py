# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Command:
    def __init__(self, s, node):
        self.s = s
        self.node = node


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append(Command('go', root))

        while len(stack) != 0:
            command = stack.pop()
            if command.s == 'go':
                node = command.node
                if node.right:
                    stack.append(Command('go', node.right))
                stack.append(Command('print', node))
                if node.left:
                    stack.append(Command('go', node.left))
            else:
                res.append(command.node.val)

        return res
