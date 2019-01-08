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
    def __init__(self):
        self.res = []

    def preorder(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    # 使用递归法进行先序遍历
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return self.res
        self.preorder(root)
        return self.res

    # 使用迭代的方式进行先序遍历
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while len(stack) != 0:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

    #   模拟系统栈的执行
    def preorderTraversal_2(self, root):
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
                if node.left:
                    stack.append(Command('go', node.left))
                stack.append(Command('print', node))
            else:
                res.append(command.node.val)
        return res


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    print(Solution().preorderTraversal_1(root))
    print(Solution().preorderTraversal_2(root))
