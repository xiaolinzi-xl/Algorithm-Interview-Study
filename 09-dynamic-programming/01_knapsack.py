
class Knapsack01:

    def rebot(self, w, v, index, c):
        if c <= 0:
            return 0

        if index == len(w) - 1:
            return v[index] if c >= w[index] else 0

        if c >= w[index]:
            return max(self.rebot(w, v, index+1, c-w[index])+v[index], self.rebot(w, v, index+1, c))

        return self.rebot(w, v, index+1, c)

    def knapsack01(self, w, v, c):
        '''
        :type w: List[int]
        :type v: List[int]
        :type c: int
        :rtype: int
        '''
        return self.rebot(w, v, 0, c)

    def knapsack01_1(self, w, v, c):
        assert len(w) == len(v)
        n = len(w)
        if n == 0:
            return 0

        memo = [[0] * (c+1) for _ in range(n)]

        for i in range(w[-1], c+1):
            memo[-1][i] = v[-1]

        for i in range(n-2, -1, -1):
            for j in range(c+1):
                memo[i][j] = memo[i+1][j]
                if j >= w[i]:
                    memo[i][j] = max(memo[i][j], memo[i+1][j-w[i]] + v[i])

        # self.print_array(memo)
        return memo[0][c]

    def print_array(self, arr):
        for i in range(len(arr)):
            print(arr[i])


if __name__ == "__main__":
    w = [1, 2, 3]
    v = [6, 10, 12]
    c = 5
    print(Knapsack01().knapsack01(w, v, c))
    print(Knapsack01().knapsack01_1(w, v, c))
