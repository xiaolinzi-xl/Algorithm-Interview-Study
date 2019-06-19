ans = []


def rebot(l, r, n, res):
    if l == n and r == n:
        ans.append(res)
        return
    if l > r:
        if l < n:
            rebot(l + 1, r, n, res + '(')
        rebot(l, r + 1, n, res + ')')
    elif l == r:
        rebot(l + 1, r, n, res + '(')


class Solution:
    def generateParenthesis(self, n):
        ans.clear()
        rebot(1, 0, n, '(')
        return ans
