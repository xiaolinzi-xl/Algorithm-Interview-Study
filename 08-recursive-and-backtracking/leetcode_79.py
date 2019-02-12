class Solution:
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = []

    def searchWorld(self, board, word, index, start_x, start_y):
        if index == len(word) - 1:
            return word[index] == board[start_x][start_y]

        if board[start_x][start_y] == word[index]:
            Solution.visited[start_x][start_y] = True
            # (start_x,start_y)开始四个方向找
            for i in range(len(Solution.d)):
                new_x = start_x + Solution.d[i][0]
                new_y = start_y + Solution.d[i][1]

                if new_x >= 0 and new_y >= 0 and new_x < len(board) and new_y < len(board[0]) and not Solution.visited[new_x][new_y]:
                    if self.searchWorld(board, word, index+1, new_x, new_y):
                        return True

            Solution.visited[start_x][start_y] = False

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        Solution.visited.clear()
        for i in range(len(board)):
            Solution.visited.append([False for _ in range(len(board[0]))])

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.searchWorld(board, word, 0, i, j):
                    return True

        return False
