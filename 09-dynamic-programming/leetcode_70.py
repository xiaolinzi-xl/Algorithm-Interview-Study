class Solution:

    def climbStairs_1(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbStairs_1(n-1) + self.climbStairs_1(n-2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 1
        memo = [-1] * (n+1)
        memo[0] = 1
        memo[1] = 1

        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n]


if __name__ == "__main__":
    print(Solution().climbStairs_1(3))
