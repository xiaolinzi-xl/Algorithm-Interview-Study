class Solution:
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = []

    def search(self, grid, start_x, start_y):
        Solution.visited[start_x][start_y] = True

        # 从(start_x,start_y) 开始 floodfill
        for i in range(len(Solution.d)):
            new_x = start_x + Solution.d[i][0]
            new_y = start_y + Solution.d[i][1]

            if new_x >= 0 and new_y >= 0 and new_x < len(grid) and new_y < len(grid[0]) and not Solution.visited[new_x][new_y] and grid[new_x][new_y] == '1':
                self.search(grid, new_x, new_y)

        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        Solution.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not Solution.visited[i][j]:
                    res += 1
                    self.search(grid, i, j)

        return res
