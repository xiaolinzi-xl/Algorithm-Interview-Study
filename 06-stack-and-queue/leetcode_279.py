from math import sqrt


class NumNode:
    def __init__(self, step, num):
        self.step = step
        self.num = num


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n > 0
        queue = []
        record = set()
        queue.append(NumNode(0, n))
        while True:
            node = queue.pop(0)

            i = int(sqrt(node.num))
            if i * i == node.num:
                return node.step + 1
            while i > 0:
                tmp = node.num - i * i
                if tmp == 0:
                    return node.step + 1
                if tmp not in record:
                    queue.append(NumNode(node.step+1, tmp))
                    record.add(tmp)
                i -= 1


if __name__ == "__main__":
    print(Solution().numSquares(-12))
