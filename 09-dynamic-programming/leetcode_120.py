class Solution:
    memo = []

    def rebot(self, triangle, x, y):
        if x == len(triangle) - 1:
            return triangle[x][y]
        return min(self.rebot(triangle, x+1, y), self.rebot(triangle, x+1, y+1)) + triangle[x][y]

    def rebot_1(self, triangle, x, y):
        if x == len(triangle) - 1:
            Solution.memo[x][y] = triangle[x][y]
            return Solution.memo[x][y]

        if Solution.memo[x][y] == -1:
            Solution.memo[x][y] = min(self.rebot(
                triangle, x+1, y), self.rebot(triangle, x+1, y+1)) + triangle[x][y]

        return Solution.memo[x][y]

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # return self.rebot(triangle, 0, 0)
        Solution.memo = [[-1] * len(i) for i in triangle]

        self.rebot_1(triangle, 0, 0)

        return Solution.memo[0][0]

    def minimumTotal_1(self, triangle):
        memory = [[-1] * len(i) for i in triangle]
        memory[-1] = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                memory[i][j] = min(
                    memory[i+1][j], memory[i+1][j+1]) + triangle[i][j]

        return memory[0][0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

    print(Solution().minimumTotal_1(triangle))
