class Solution:
    res = []
    col = []
    dia1 = []
    dia2 = []

    def generateBoard(self, n, row):
        board = []
        for i in range(n):
            tmp = ''
            for j in range(n):
                if j != row[i]:
                    tmp += '.'
                else:
                    tmp += 'Q'
            board.append(tmp)
        return board

    # 摆放第 index 行的位置
    def putQueen(self, n, index, row):
        if index == n:
            Solution.res.append(self.generateBoard(n, row))
            return

        for i in range(n):
            # 将第index行的皇后摆在第i列
            if not Solution.col[i] and not Solution.dia1[index+i] and not Solution.dia2[index-i+n-1]:
                row.append(i)
                Solution.col[i] = True
                Solution.dia1[index+i] = True
                Solution.dia2[index-i+n-1] = True

                self.putQueen(n, index+1, row)
                
                Solution.col[i] = False
                Solution.dia1[index+i] = False
                Solution.dia2[index-i+n-1] = False
                row.pop()

        return

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        Solution.col = [False for _ in range(n)]
        Solution.dia1 = [False for _ in range(2*n-1)]
        Solution.dia2 = [False for _ in range(2*n-1)]

        Solution.res.clear()

        self.putQueen(n, 0, [])

        return Solution.res
