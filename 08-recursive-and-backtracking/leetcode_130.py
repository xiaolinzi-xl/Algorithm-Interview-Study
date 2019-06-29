class Solution:
    direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def search(self, grid, start_x, start_y):
        self.flag[start_x][start_y] = True
        for i in range(4):
            new_x = start_x + self.direction[i][0]
            new_y = start_y + self.direction[i][1]

            if len(grid) - 1 > new_x >= 1 and len(grid[start_x]) - 1 > new_y >= 1 and grid[new_x][new_y] == 'O' and not \
                    self.flag[new_x][new_y]:
                self.search(grid, new_x, new_y)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        self.flag = [[False] * len(board[i]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1:
                    self.flag[i][j] = True
                elif board[i][j] == 'X':
                    self.flag[i][j] = True

        for i in (0, len(board) - 1):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.search(board, i, j)

        for j in (0, len(board[0]) - 1):
            for i in range(len(board)):
                if board[i][j] == 'O':
                    self.search(board, i, j)

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if not self.flag[i][j]:
                    board[i][j] = 'X'


if __name__ == '__main__':
    board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]
    Solution().solve(board)
    print(board)
