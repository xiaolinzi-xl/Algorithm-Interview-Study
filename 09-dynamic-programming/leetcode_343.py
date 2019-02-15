class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1

        res = 0
        for i in range(1, n):
            res = max(res, self.integerBreak(n-i) * i, (n-i) * i)
            # print(n, i, res)
        return res

    def integerBreak_1(self, n):
        assert n >= 2
        if n <= 2:
            return 1

        memo = [0] * (n+1)
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                memo[i] = max(memo[i-j]*j, (i-j)*j, memo[i])

        return memo[n]


if __name__ == "__main__":
    print(Solution().integerBreak(10))
    print(Solution().integerBreak_1(10))
