class Solution:
    res = []

    def generateCombine(self, n, k, index, a):
        if k == 0:
            Solution.res.append(list(a))
            return

        for i in range(index, n-k+2):
            a.append(i)
            self.generateCombine(n, k-1, i+1, a)
            a.pop()

        return

    def generateCombine_1(self, n, k, index, a):
        if len(a) == k:
            Solution.res.append(list(a))
            return

        for i in range(index, n+1):
            a.append(i)
            self.generateCombine_1(n, k, i+1, a)
            a.pop()

        return

    def generateCombine_2(self, n, k, index, a):
        if len(a) == k:
            Solution.res.append(list(a))
            return

        # 还有 k - len(a) 个空位，i最大为 n - (k-len(a)) + 1
        for i in range(index, n - (k-len(a)) + 2):
            a.append(i)
            self.generateCombine_2(n, k, i+1, a)
            a.pop()

        return

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        Solution.res.clear()
        # self.generateCombine(n, k, 1, [])
        self.generateCombine(n, k, 1, [])

        return Solution.res


if __name__ == "__main__":
    print(Solution().combine(4, 2))
